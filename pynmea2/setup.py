import importlib.machinery
import importlib.util
import os  # Added for path management
from setuptools import setup, find_packages

def load_source(modname, filename):
    """Load a source file and return its module object."""
    loader = importlib.machinery.SourceFileLoader(modname, filename)
    spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module

# Adjust path to always refer to the correct location of _version.py
here = os.path.abspath(os.path.dirname(__file__))
_version = load_source("_version", os.path.join(here, "_version.py"))

# Load the long description from README.md
with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pynmea2',
    version=_version.__version__,
    author='Tom Flanagan',
    author_email='tom@zkpq.ca',
    license='MIT',
    url='https://github.com/Knio/pynmea2',

    description='Python library for the NMEA 0183 protocol, with proprietary extensions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['pynmea2', 'pynmea2.*']),
    keywords='python nmea gps parse parsing nmea0183 0183 proprietary',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        "dev": ["pytest", "flake8"],
    },
    include_package_data=True,
    zip_safe=False,
)
