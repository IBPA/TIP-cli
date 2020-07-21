from setuptools import setup, find_packages

setup(
    name='tip-client-cli',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tip-cli=views.main:main']
    },
    install_requires=[
        'numpy>=1.19.0',
        'pandas>=1.0.5',
        'requests>=2.24.0'
    ],
    python_requires='>=3.6.1')
