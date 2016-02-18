#!/usr/bin/env python
import os
import sys
import website.settings
if __name__ == "__main__":
    #Assigning settings file
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    from django.core.management import execute_from_command_line
    DJANGO_SETTINGS_MODULE = website.settings
    execute_from_command_line(sys.argv)
