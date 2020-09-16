from pip._internal.cli import main
import sys


def install(dep):
    """
    Installs the dependencies
    :param dep: name of the dependencies
    """
    ret = main.main(["install", dep])
    if ret != 0:
        raise Exception("Dependency %s not installed.Check stdout." % dep)


def install_from_list(list_of_dep):
    """
    Installs the dependencies in the list
    :param list_of_dep: list of dependencies
    """
    for dep in list_of_dep:
        install(dep)


common = ["pywebview", "requests"]

windows = []
osx = []

if __name__ == '__main__':
    # First install all the common dependencies
    install_from_list(common)
    if sys.platform == "win32":
        install_from_list(windows)
    elif sys.platform == "darwin":
        install_from_list(osx)
    else:
        sys.stderr.write("The current platform=%s is not supported" % sys.platform)
