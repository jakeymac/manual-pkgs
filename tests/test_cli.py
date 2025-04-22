import subprocess

def test_cli_help():
    result = subprocess.run(['python3', 'get_manual_pkgs.py', '--help'], 
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "List packages explicitly installed by the user." in result.stdout

def test_cli_normal_files(normal_status_file, normal_extended_states_file, normal_history_log_file, normal_history_log_file_2):
    result = subprocess.run(['python3', 'get_manual_pkgs.py', 
                             '--status', str(normal_status_file), 
                             '--extended', str(normal_extended_states_file), 
                             '--history-logs', str(normal_history_log_file), str(normal_history_log_file_2)],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "Packages explicitly installed by the user:" in result.stdout
    assert "package-1" in result.stdout
    assert "package-2" in result.stdout
    assert "package-3" not in result.stdout
    assert "package-4" not in result.stdout
    assert "package-5" not in result.stdout
    assert "package-6" not in result.stdout
    assert "package-7" not in result.stdout
    assert "package-8" in result.stdout
    assert "package-9" in result.stdout
    assert "package-10" not in result.stdout

def test_cli_normal_files_verbose(normal_status_file, normal_extended_states_file, normal_history_log_file, normal_history_log_file_2):
    result = subprocess.run(['python3', 'get_manual_pkgs.py', 
                             '--status', str(normal_status_file), 
                             '--extended', str(normal_extended_states_file), 
                             '--history-logs', str(normal_history_log_file), str(normal_history_log_file_2),
                             '-v'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "Installed packages found: 8" in result.stdout
    assert "Manual packages from extended states: 3" in result.stdout
    assert "Manual packages from history logs: 6" in result.stdout
    assert "Final list of manually installed packages found: 4" in result.stdout
    
def test_cli_abnormal_files(abnormal_status_file, abnormal_extended_states_file, abnormal_history_log_file, abnormal_history_log_file_2):
    result = subprocess.run(['python3', 'get_manual_pkgs.py', 
                             '--status', str(abnormal_status_file), 
                             '--extended', str(abnormal_extended_states_file), 
                             '--history-logs', str(abnormal_history_log_file), str(abnormal_history_log_file_2)],
                            capture_output=True, text=True)
    assert result.returncode == 0
    print(result.stdout)

    assert "Packages explicitly installed by the user:" in result.stdout
    assert "package-1" not in result.stdout
    assert "package-2" not in result.stdout
    assert "package-3" not in result.stdout
    assert "package-4" in result.stdout
    assert "package-5" not in result.stdout
    assert "package-6" in result.stdout
    assert "package-7" not in result.stdout
    assert "package-8" not in result.stdout
    assert "package-9" not in result.stdout
    assert "package-10" not in result.stdout

def test_cli_abnormal_files_verbose(abnormal_status_file, abnormal_extended_states_file, abnormal_history_log_file, abnormal_history_log_file_2):
    result = subprocess.run(['python3', 'get_manual_pkgs.py', 
                             '--status', str(abnormal_status_file), 
                             '--extended', str(abnormal_extended_states_file), 
                             '--history-logs', str(abnormal_history_log_file), str(abnormal_history_log_file_2),
                             '-v'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "Installed packages found: 7" in result.stdout
    assert "Manual packages from extended states: 2" in result.stdout
    assert "Manual packages from history logs: 2" in result.stdout
    assert "Final list of manually installed packages found: 2" in result.stdout