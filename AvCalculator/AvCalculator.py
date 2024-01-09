""" AvCalculator
This application allows you to calculate an average using
values given by the user.
"""

from utils.version import get_version
from utils.github_version_checker import get_latest_version
from app import AvCalculatorApp

REPOSITORY = "AvCalculator"

version = get_version((2, 0, 0, 'final', 0))
latest_version = get_latest_version(REPOSITORY, version)


if __name__ == '__main__':
    AvCalculatorApp(version, latest_version)
