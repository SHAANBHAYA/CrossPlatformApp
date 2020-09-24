"""
Installs dependencies for the project.
Supports the windows and osx operating systems.
"""

from pip._internal.cli import main
import sys

def install_packages(package_names):
    """
    Installs all the packages in the package_names
    :param package_names: list of all the packages
    """
    for package in package_names:
        ret=main.main(["install", package])
        if ret != 0:
            raise Exception("Installation failed.Check logs")

# Packages common in all the Operating systems.
common_packages=["requests","pywebview"]
# Packages specific for windows
Windows_packages=[]
# Pakcages specific for OSX
OSX_Packages=[]

if __name__ == '__main__':
    # Install the common packages
    install_packages(common_packages)
    # Install OS dependent packages
    if sys.platform == "win32":
        install_packages(Windows_packages)
    elif sys.platform == "darwin":
        install_packages(OSX_Packages)
    else:
        raise Exception("Platform not supported")