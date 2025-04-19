#!/usr/bin/env python3

def get_installed_packages():
    """ Gets the full list of installed packages from the dpkg status file. """
    installed = set()
    
    # Read the status file and parse all installed packages
    with open("/var/lib/dpkg/status") as file:
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

def get_manual_from_extended_states():
    """ Parses the extended states file to find packages that were manually installed. """
    manual = set()

    # Read the extended states file and parse all manually installed packages
    with open("/var/lib/apt/extended_states") as file:
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

def get_manual_from_apt_history():
    """ Parses the apt history logs to find packages that the user manually installed. """
    manual = set()
    
    # Read the history logs and get all explicitly installed packages
    with open("/var/log/apt/history.log") as file:
        current_command_line = None
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

def get_manual_packages():
    """ Returns the list of currently installed packages that were explicitly installed by the user. """
    installed = get_installed_packages()
    manual_extended = get_manual_from_extended_states()
    manual_history = get_manual_from_apt_history()

    # Return all packages that are installed and are listed in the extended states or history logs
    return installed & (manual_extended | manual_history)

print(get_manual_packages())
