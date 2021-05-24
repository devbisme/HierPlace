#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

__author__ = 'XESS Corp.'
__email__ = 'info@xess.com'
__version__ = '0.3.6'

# if 'sdist' in sys.argv[1:]:
#     with open('kinet2pcb/pckg_info.py','w') as f:
#         for name in ['__version__','__author__','__email__']:
#             f.write("{} = '{}'\n".format(name,locals()[name]))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author=__author__,
    author_email=__email__,
    version=__version__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Groups and arranges KiCAD PCBNEW board parts so they reflect the design hierarchy.",
    # entry_points={
    #     'console_scripts': [
    #         'kinet2pcb=kinet2pcb.kinet2pcb:main',
    #     ],
    # },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='HierPlace KiCad EDA PCBNEW',
    name='hierplace',
    packages=find_packages(include=['hierplace']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/xesscorp/HierPlace',
    zip_safe=False,
)
