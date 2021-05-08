===============================
pyuarm-custom (based on pyuarm-2.2.5.1)
===============================

Overview
========

This module encapsulates the operations for uArm. It provides basic Movement on Python.
Also provides Firmware_helper and Calibration. The module named "pyuarm" makes the API more pythonic.

It was heavily modified and customized by Samuel Duclos to patch bugs and add useful features.

Other pages (online)

- `project page on Github`_
- `Download Page`_ with releases
- This page, when viewed online is at https://pyuarm.readthedocs.io.


Features
========
- Auto uArm Port detection
- Provide firmware_helper, firmware upgrade online
- Provide Auto Calibration tool

Requirements
============
- Python 2.7x or Python 3.4x above
- uArmProtocol Firmware (Please use ``uarm_helper firmware -d`` to upgrade your firmware)

Installation
============

pyuarm
------
This install a package that can be used from Python (``import pyuarm``).

To install for all users on the system, administrator rights (root) may be required.

From PyPI
~~~~~~~~~
pyuarm can be installed from PyPI, either manually downloading the files and installing as described below or using::

    pip install pyuarm

From source (tar.gz or checkout)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Download the archive from http://pypi.python.org/pypi/pyuarm.
Unpack the archive, enter the ``pyuarm-x.y`` directory and run::

    python setup.py install

.. _`project page on GitHub`: https://github.com/uArm-Developer/pyuarm
.. _`Download Page`: http://pypi.python.org/pypi/pyuarm
