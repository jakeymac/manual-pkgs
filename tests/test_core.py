import pytest
from get_manual_pkgs import (
    get_installed_packages, 
    get_manual_from_extended_states, 
    get_manual_from_apt_history, 
    get_manual_packages)

def test_get_installed_packages_normal(normal_status_file):
    packages = get_installed_packages(str(normal_status_file))
    assert packages == {"package-1", "package-2", "package-3", "package-5", "package-7", "package-8", "package-9", "package-10"}
    assert "package-4" not in packages
    assert "package-6" not in packages

def test_get_manual_from_extended_states_normal(normal_extended_states_file):
    packages = get_manual_from_extended_states(str(normal_extended_states_file))
    assert packages == {"package-1", "package-2", "package-4"}
    assert "package-3" not in packages

def test_get_manual_from_apt_history_normal(normal_history_log_file, normal_history_log_file_2):
    packages = get_manual_from_apt_history([str(normal_history_log_file), str(normal_history_log_file_2)])
    assert packages == {"package-1", "package-2", "package-4", "package-6", "package-8", "package-9"}
    assert "package-3" not in packages
    assert "package-5" not in packages
    assert "package-7" not in packages
    assert "package-10" not in packages

def test_get_manual_packages_normal(
    normal_status_file, 
    normal_extended_states_file, 
    normal_history_log_file, 
    normal_history_log_file_2):
    
    packages = get_manual_packages(
        str(normal_status_file), 
        str(normal_extended_states_file), 
        [str(normal_history_log_file), str(normal_history_log_file_2)],
        verbose=False
    )
    
    assert packages == {"package-1", "package-2", "package-8", "package-9"}
    assert "package-3" not in packages
    assert "package-4" not in packages
    assert "package-5" not in packages
    assert "package-6" not in packages
    assert "package-7" not in packages
    assert "package-10" not in packages

def test_get_installed_packages_abnormal(abnormal_status_file):
    packages = get_installed_packages(str(abnormal_status_file))
    assert packages == {"package-2", "package-4", "package-5", "package-6", "package-7", "package-8", "package-10"}
    assert "package-1" not in packages
    assert "package-3" not in packages
    assert "package-9" not in packages

def test_get_manual_from_extended_states_abnormal(abnormal_extended_states_file):
    packages = get_manual_from_extended_states(str(abnormal_extended_states_file))
    assert packages == {"package-1", "package-4"}
    assert "package-2" not in packages
    assert "package-3" not in packages

def test_get_manual_from_apt_history_abnormal(abnormal_history_log_file, abnormal_history_log_file_2):
    packages = get_manual_from_apt_history([str(abnormal_history_log_file), str(abnormal_history_log_file_2)])
    assert packages == {"package-4", "package-6"}
    assert "package-1" not in packages
    assert "package-2" not in packages
    assert "package-3" not in packages
    assert "package-5" not in packages
    assert "package-7" not in packages
    assert "package-8" not in packages
    assert "package-9" not in packages
    assert "package-10" not in packages

def test_get_manual_packages_abnormal(
    abnormal_status_file, 
    abnormal_extended_states_file, 
    abnormal_history_log_file, 
    abnormal_history_log_file_2):
    
    packages = get_manual_packages(
        str(abnormal_status_file), 
        str(abnormal_extended_states_file), 
        [str(abnormal_history_log_file), str(abnormal_history_log_file_2)],
        verbose=False
    )
    
    assert packages == {"package-4", "package-6"}
    assert "package-1" not in packages
    assert "package-2" not in packages
    assert "package-3" not in packages
    assert "package-5" not in packages
    assert "package-7" not in packages
    assert "package-8" not in packages
    assert "package-9" not in packages
    assert "package-10" not in packages


