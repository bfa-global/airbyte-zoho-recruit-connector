#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_zoho_recruit import SourceZohoRecruit


def run():
    source = SourceZohoRecruit()
    launch(source, sys.argv[1:])
