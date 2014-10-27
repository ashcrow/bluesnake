#!/usr/bin/env python
# The MIT License (MIT)
#
# Copyright (c) 2014 Steve Milner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Build script for bluesnake.
"""

import os.path
import sys

sys.path.insert(0, 'src')

from relent import __version__

# We MUST have setuptools and pip
try:
    from setuptools import setup, find_packages
    from pip.req import parse_requirements

    reqs = [str(ir.req) for ir in parse_requirements('requirements.txt')]
except ImportError, ie:
    print 'pip and setuptools must be installed. Error: %s' % ie
    raise SystemExit(1)


setup(
    name='bluesnake',
    version=__version__,
    author='See AUTHORS',
    url='https://github.com/ashcrow/bluesnake',
    license='MIT',
    zip_safe=False,
    packages=find_packages('src'),
    package_dir={
        'bluesnake': 'src/bluesnake',
    },
    install_requires=reqs,
    classifiers=[
        'License :: OSI Approved :: MIT License'
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
