from setuptools import find_packages, setup

setup(
    name='GraphicalBF',
    packages=find_packages(include='GraphicalBF'),
    version='0.1.0',
    description='An interpreter for GraphicalBF',
    author='Teagan Penland',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)