# Copyright 2020 Dalton Durst
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from requests.auth import HTTPBasicAuth
import requests
import os
from xml.etree import ElementTree
import sys

JAMF_URL = os.environ["JAMF_URL"]
JAMF_USERNAME = os.environ["JAMF_USERNAME"]
JAMF_PASSWORD = os.environ["JAMF_PASSWORD"]
JAMF_AUTH = HTTPBasicAuth(JAMF_USERNAME, JAMF_PASSWORD)
JAMF_SEARCH_ID = os.environ["JAMF_SEARCH_ID"]
SESSION = requests.Session()

def main():
    advanced_search = SESSION.get("{}/JSSResource/advancedmobiledevicesearches/id/{}".format(JAMF_URL, JAMF_SEARCH_ID), auth=JAMF_AUTH)

    tree = ElementTree.fromstring(advanced_search.text)

    device_ids = []
    for mobile_device in tree.find("mobile_devices"):
        device_id = mobile_device.find("id")
        if device_id is not None:
            device_ids.append(device_id.text)

    device_ids_commas = ",".join(device_ids)

    blank_push_command = SESSION.post("{}/JSSResource/mobiledevicecommands/command/BlankPush/id/{}".format(JAMF_URL, device_ids_commas), auth=JAMF_AUTH)

    try:
        blank_push_command.raise_for_status()
    except Exception as e:
        print(e)
        print(blank_push_command.text)
        print("Failed to create a blank push command for the devices in group {}.".format(JAMF_SEARCH_ID))
        sys.exit(1)
    else:
        print("Successfully created blank push command for {} devices.".format(len(device_ids)))
        sys.exit(0)

if __name__ == "__main__":
    main()
