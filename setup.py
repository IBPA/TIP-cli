# -*- coding: utf-8 -*-
"""setup.py description.

This is a setup.py template for any project.

"""

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='tip-cli',
    version='1.0.0',
    description='The Toxicology Integrated Platform (TIP) command-line'
                'interface module.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # GitHub link.
    url='https://github.com/IBPA/TIP',
    author='Fangzhou Li',
    author_email='fzli@ucdavis.edu',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  # we use GPL-3.0 license, please check
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Chemistry'
    ],
    keywords='',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tip-cli=tip.views.main:main']
    },
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'requests'
    ]
)
