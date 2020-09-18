Spam Blank Push
===============

Spam Blank Push is a script to quickly send a blank push command to an advanced mobile device search on Jamf Pro Server.

Prerequisites
-------------

To use jps-gsx-robot, you will need Python3 and pipenv installed.

Install Python
^^^^^^^^^^^^^^

macOS
"""""

To install Python3 on macOS, download the pkg from https://www.python.org/downloads/. Once you've run and installed the pkg, find "Python 3.*x*" in your Applications directory and run the `Update Shell Profile.command` file, then the `Install Certificates.command` file.

Windows
"""""""

To install Python3 on Windows, download its installer from https://www.python.org/downloads/. While installing, check the option to add Python to your PATH. Once the installation completes, reboot your computer so Python can be run from a command prompt.

Install Pipenv
^^^^^^^^^^^^^^

Pipenv is used to install the dependencies for jps-gsx-robot and keep them separate from any other Python projects on your computer. To install pipenv, run the following command in a terminal or command prompt::

    pip3 install --user pipenv

Usage
-----

Download spamblankpush
^^^^^^^^^^^^^^^^^^^^^^

You can download the script and its example configuration by selecting "Download ZIP" under the Clone or Download menu, clicking [this link](https://github.com/UniversalSuperBox/jps-gsx-robot/archive/master.zip), or cloning it with `git`.

Install dependencies
^^^^^^^^^^^^^^^^^^^^

Use pipenv to create the virtual environment that will be used to run the script::

    pipenv install --three

Configure spamblankpush
^^^^^^^^^^^^^^^^^^^^^^^

spamblankpush is configured via environment variables.

To set the configuration environment variables under most shells, type `export VARIABLE_NAME=value`. For example, to provide JAMF_USERNAME to the script from the environment, type::

    export JAMF_USERNAME='spamblankpush'


Under a Windows shell, replace `export` with `set`.

The required configuration variables follow.

JAMF_URL
""""""""

The base URL of your JPS server, with protocol and port. For example::

    https://jps.example.com:8443

JAMF_USERNAME and JAMF_PASSWORD
"""""""""""""""""""""""""""""""

Username and password of a JPS user account with the following permissions:

* Jamf Pro Server Objects
    * Advanced Mobile Device Searches: Read
    * Mobile Devices: Create, Read
* Jamf Pro Server Actions
    * Send Blank Pushes to Mobile Devices

JAMF_SEARCH_ID
""""""""""""""

The ID of the advanced mobile device search that you would like to send a blank push to. For example, the ID in this URL is '11'::

    https://jps.example.com:8443/advancedMobileDeviceSearches.html?id=11&o=r

You can find this URL by browsing to the advanced mobile device search in JPS.

Run  spamblankpush
^^^^^^^^^^^^^^^^^^

Change into the script's directory. With the current shell configured as specified and its dependencies installed, it can be run with::

    pipenv run python ./spamblankpush.py
