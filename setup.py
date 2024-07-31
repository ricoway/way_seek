from setuptools import setup, find_packages

setup(
    name='way_seek',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'way_seek = way_seek.app:main',
        ],
    },
)
