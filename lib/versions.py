import sys
import requests
import pytest
import importlib.metadata as metadata

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return metadata.version("pytest")

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor >= 8

def test_requests_version():
    assert requests_version() == "2.27.1"

def test_pytest_version():
    assert pytest_version() == "7.1.3"
