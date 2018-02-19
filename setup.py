import os
from setuptools import setup, find_packages


def read(filename):
    """
    Returns the contents of the given package file.

    Args:
        filename (str): The name of the file to read, relative to the current
            directory.

    Returns:
        str: The contents of the given package file.
    """

    path = os.path.join(os.path.dirname(__file__), filename)

    with open(path) as f:
        return f.read()


def get_version():
    """ str: The package version. """

    global_vars = {}

    # Compile and execute the individual file to prevent
    # the package from being automatically loaded.
    source = read(os.path.join("test_python_package", "__version__.py"))
    code = compile(source, "version.py", "exec")
    exec(code, global_vars)

    return global_vars['__version__']


setup(
    name="elliterate-test-python-package",
    version=get_version(),
    description="Test Python package",
    long_description="Test Python package",
    url="https://github.com/elliterate/test-python-package",
    author="Ian Lesperance",
    author_email="ian@elliterate.com",
    license="MIT",
    keywords="",
    classifiers=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=[],
    extras_require={})
