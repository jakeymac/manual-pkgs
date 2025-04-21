# manual-pkgs 
![Release](https://github.com/jakeymac/manual-pkgs/actions/workflows/release.yml/badge.svg)
![License](https://img.shields.io/github/license/jakeymac/manual-pkgs)
![Latest Release](https://img.shields.io/github/v/release/jakeymac/manual-pkgs)

A command-line tool to list packages currently installed that were explicitly installed by the user

## How does it work?
`manual-pkgs` parses files that are generally found in the following file paths:
- `/var/lib/dpkg/status`
- `/var/lib/apt/extended_states`
- `/var/log/apt/history.log`

It then uses the information found in those files to determine what packages are currently installed and which were manually installed by the user rather than installed automatically by the system, or as dependencies of other packages.

## Installation
You can install `manual-pkgs` in two ways:

1. Downloading the prebuilt `.deb` file from the [Releases page](https://github.com/jakeymac/manual-pkgs/releases/) and picking the latest release.
2. Building the package yourself.

--- 
### Installing the prebuilt file

1. Go to the package's [Releases page](https://github.com/jakeymac/manual-pkgs/releases/)
2. Download the latest `.deb` file
3. Install it using this command:
    ```bash
    dpkg -i manual-pkgs_*.deb
    ```

### Building the package locally

1. First, clone the repository on your computer:
    ```bash
    git clone https://github.com/jakeymac/manual-pkgs.git
    ```
2. Make sure the build script is executable:
    ```bash
    cd manual-pkgs
    chmod +x build.sh
    ```
3. Now build the .deb package using the build script:
    ```bash
    ./build.sh
    ```
4. Install the package using the generated .deb file:
    ```bash
    dpkg -i dist/manual-pkgs_*.deb 
    ```

## Usage

Here are the optional flags for the `manual-pkgs` tool:

| Option | Description |
|--------|-------------|
| `-v`, `--verbose` | Enable verbose output with package counts from each source |
| `-o FILE`, `--output FILE` | Save the package list to a specified file |
| `--status PATH` | Path to a dpkg status file |
| `--extended PATH` | Path to a apt extended states file |
| `--history-logs PATHS` | One or more paths to apt history logs |

The `manual-pkgs` tool uses these system files by default:
- `/var/lib/dpkg/status`
- `/var/lib/apt/extended_states`
- `/var/log/apt/history.log`

--- 
### Examples

```bash
# Display all manually installed packages
manual-pkgs

# Verbose mode
manual-pkgs -v

# Output results to a file
manual-pkgs --output packages.txt

# Use a custom file path for extended states
manual-pkgs --extended /custom/path/extended_states

# Use custom file paths for history logs
manual-pkgs --history-logs /custom/path/history.log /custom/path/history.log.1

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute it with proper attribution.