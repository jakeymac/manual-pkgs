#!/usr/bin/env python3

import os
import sys
import argparse

# Color codes for terminal output
GREEN_TEXT = "\033[92m"
BLUE_TEXT = "\033[94m"
RED_TEXT = "\033[91m"
RESET_TEXT_COLOR = "\033[0m"

def get_installed_packages(status_path):
    """ Gets the full list of installed packages from the dpkg status file. """
    if not os.path.exists(status_path):
        print(f"{RED_TEXT}Error: Status file not found: {status_path}{RESET_TEXT_COLOR}")
        sys.exit(1)

    installed = set()
    
    # Read the status file and parse all installed packages
    with open(status_path) as file:
        current_package = None
        for line in file:
            # Check for the start of a new package entry, get the package name
            if line.startswith("Package: "):
                current_package = line.split("Package: ")[1].strip()
            # Check if the package is installed
            elif line.startswith("Status: ") and "install ok installed" in line:
                if current_package:
                    installed.add(current_package)
                    current_package = None
    return installed

def get_manual_from_extended_states(extended_path):
    """ Parses the extended states file to find packages that were manually installed. """
    if not os.path.exists(extended_path):
        print(f"{RED_TEXT}Error: Extended states file not found: {extended_path}{RESET_TEXT_COLOR}")
        sys.exit(1)

    manual = set()

    # Read the extended states file and parse all manually installed packages
    with open(extended_path) as file:
        current_package = None
        for line in file:
            # Check for the start of a new package entry, get the package name
            if line.startswith("Package: "):
                current_package = line.split("Package: ")[1].strip()
            # Make sure the package is not auto-installed
            elif line.startswith("Auto-Installed: 0") and current_package:
                manual.add(current_package)
                current_package = None
    return manual

def get_manual_from_apt_history(log_paths):
    """ Parses the apt history logs to find packages that the user manually installed. """
    for path in log_paths:
        if not os.path.exists(path):
            print(f"{RED_TEXT}Error: Log file not found: {path}{RESET_TEXT_COLOR}")
            sys.exit(1)
            
    manual = set()
    
    # Read the history logs and get all explicitly installed packages
    for path in log_paths:
        current_command_line = None

        with open(path) as file:
            for line in file:
                line = line.strip()
                # Check for the start of a new command line where a package was explicitly installed
                if line.startswith("Commandline:") and "install" in line and ("apt " in line or "apt-get " in line):
                    command_line = line.replace("Commandline: ", "").strip()
                    parts = command_line.split()
                    install_index = parts.index("install")

                    # Get the command line arguments after "install" without any flags
                    current_command_line = [ arg for arg in parts[install_index + 1:] if not arg.startswith("-") ]
                # After the "Commandline" look for "Install:" that signifies the actual command the user ran has ended
                elif line.startswith("Install:") and current_command_line:
                    for package in current_command_line:
                        manual.add(package)
                    current_command_line = None
    return manual

def get_manual_packages(status_path, extended_path, log_paths, verbose):
    """ Returns the list of currently installed packages that were explicitly installed by the user. """
    installed = get_installed_packages(status_path)
    manual_extended = get_manual_from_extended_states(extended_path)
    manual_history = get_manual_from_apt_history(log_paths)

    # Return all packages that are installed and are listed in the extended states or history logs
    manual_packages = installed & (manual_extended | manual_history)

    # If verbose is enabled, print the counts of each set of packages from each source
    if verbose:
        print(f"{BLUE_TEXT}Installed packages found: {len(installed)}{RESET_TEXT_COLOR}")
        print(f"{BLUE_TEXT}Manual packages from extended states: {len(manual_extended)}{RESET_TEXT_COLOR}")
        print(f"{BLUE_TEXT}Manual packages from history logs: {len(manual_history)}{RESET_TEXT_COLOR}")
        print(f"{BLUE_TEXT}Final list of manually installed packages found: {len(manual_packages)}{RESET_TEXT_COLOR}")

    return manual_packages

def main():
    parser = argparse.ArgumentParser(description="List packages explicitly intalled by the user.")
    parser.add_argument("--status", default="/var/lib/dpkg/status", 
                        help="Path to the dpkg status file.")
    parser.add_argument("--extended", default="/var/lib/apt/extended_states", 
                        help="Path to the apt extended_states file.")
    parser.add_argument("--history-logs", nargs="+", default=["/var/log/apt/history.log"], 
                        help="Paths to the apt history log files to check.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()
    manual_packages = get_manual_packages(args.status, args.extended, args.history_logs, args.verbose)

    if not manual_packages:
        print(f"{BLUE_TEXT}No packages found that were explicitly installed by the user.{RESET_TEXT_COLOR}")
    else:
        print(f"{GREEN_TEXT}Packages explicitly installed by the user:{RESET_TEXT_COLOR}")
        print("\n".join(manual_packages))

if __name__ == "__main__":
    main()