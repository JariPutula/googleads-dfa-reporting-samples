#!/usr/bin/python
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example illustrates how to download a report file."""

import argparse
import sys

from apiclient import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'report_id', type=int,
    help='The ID of the report to get a file for')
argparser.add_argument(
    'file_id', type=int,
    help='The ID of the file to get')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'dfareporting', 'v2.3', __doc__, __file__, parents=[argparser],
      scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

  report_id = flags.report_id
  file_id = flags.file_id

  try:
    # Construct the request.
    request = service.files().get_media(reportId=report_id, fileId=file_id)

    # Execute request and print the file contents
    print request.execute()

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')


if __name__ == '__main__':
  main(sys.argv)
