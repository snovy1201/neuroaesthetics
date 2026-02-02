from setuptools import find_packages
from setuptools import setup

setup(
    name='mocap_optitrack_interfaces',
    version='0.0.1',
    packages=find_packages(
        include=('mocap_optitrack_interfaces', 'mocap_optitrack_interfaces.*')),
)
