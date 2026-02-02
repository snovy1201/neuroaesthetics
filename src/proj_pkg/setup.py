import os
from glob import glob
from setuptools import setup

package_name = 'proj_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Project package with mocap visualizer',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'mocap_visualizer = proj_pkg.visualizer:main',
        ],
    },
)