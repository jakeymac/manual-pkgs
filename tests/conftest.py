import pytest


@pytest.fixture
def normal_status_file(tmp_path):
    f = tmp_path / "status"
    f.write_text(
        "Package: package-1\nStatus: install ok installed\n"
        "Package: package-2\nStatus: install ok installed\n"
        "Package: package-3\nStatus: install ok installed\n"
        "Package: package-4\n Status: not-installed\n"
        "Package: package-5\nStatus: install ok installed\n"
        "Package: package-6\nStatus: not-installed\n"
        "Package: package-7\nStatus: install ok installed\n"
        "Package: package-8\nStatus: install ok installed\n"
        "Package: package-9\nStatus: install ok installed\n"
        "Package: package-10\nStatus: install ok installed\n"
    )
    return f


@pytest.fixture
def normal_extended_states_file(tmp_path):
    f = tmp_path / "extended_states"
    f.write_text(
        "Package: package-1\nAuto-Installed: 0\n"
        "Package: package-2\nAuto-Installed: 0\n"
        "Package: package-3\nAuto-Installed: 1\n"
        "Package: package-4\nAuto-Installed: 0"
    )
    return f


@pytest.fixture
def normal_history_log_file(tmp_path):
    f = tmp_path / "history.log"
    f.write_text(
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt install package-1 package-2\n"
        "Install: package-1 package-2 package-3\n"
        "End-Date: 2025-04-21  12:05:00\n"
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt-get install package-4\n"
        "Install: package-4 package-5\n"
        "End-Date: 2025-04-21  12:05:00\n"
    )
    return f


@pytest.fixture
def normal_history_log_file_2(tmp_path):
    f = tmp_path / "history.log.1"
    f.write_text(
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt install package-6\n"
        "Install: package-6 package-7\n"
        "End-Date: 2025-04-21  12:05:00\n"
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt-get install package-8 package-9\n"
        "Install: package-8 package-9 package-10\n"
        "End-Date: 2025-04-21  12:05:00\n"
    )
    return f


@pytest.fixture
def abnormal_status_file(tmp_path):
    f = tmp_path / "abnormal_status"
    f.write_text(
        "Package: package-1\n"
        "Package: package-2\nStatus: install ok installed\n"
        "Package: package-3\nStatus: not-installed\n"
        "Package: package-4\nStatus: install ok installed\n"
        "Package: package-5\nStatus: install ok installed\n"
        "Package: package-6\nStatus: install ok installed\n"
        "Package: package-7\nStatus: install ok installed\n"
        "Package: package-8\nStatus: install ok installed\n"
        "Package: package-9\nStatus: not-installed\n"
        "Package: package-10\nStatus: install ok installed\n"
    )
    return f


@pytest.fixture
def abnormal_extended_states_file(tmp_path):
    f = tmp_path / "abnormal_extended_states"
    f.write_text(
        "Package: package-1\nAuto-Installed: 0\n"
        "Package: package-2\n"
        "Package: package-3\nAuto-Installed: 1\n"
        "Package: package-4\nAuto-Installed: 0\n"
    )
    return f


@pytest.fixture
def abnormal_history_log_file(tmp_path):
    f = tmp_path / "abnormal_history.log"
    f.write_text(
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt install package-1 package-2\n"
        "End-Date: 2025-04-21  12:05:00\n"
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt-get install package-4\n"
        "Install: package-4 package-5\n"
        "End-Date: 2025-04-21  12:05:00\n"
    )
    return f


@pytest.fixture
def abnormal_history_log_file_2(tmp_path):
    f = tmp_path / "abnormal_history.log.1"
    f.write_text(
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt install package-6\n"
        "Install: package-6 package-7\n"
        "End-Date: 2025-04-21  12:05:00\n"
        "Start-Date: 2025-04-21  12:00:00\n"
        "Commandline: apt-get install package-8 package-9\n"
        "End-Date: 2025-04-21  12:05:00\n"
    )
    return f


@pytest.fixture
def no_packages_installed_status_file(tmp_path):
    f = tmp_path / "no_packages_installed_status"
    f.write_text(
        "Package: package-1\nStatus: not-installed\n"
        "Package: package-2\nStatus: not-installed\n"
        "Package: package-3\nStatus: not-installed\n"
    )
    return f
