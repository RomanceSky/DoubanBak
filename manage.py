#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Douban.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minicms.settings")
>>>>>>> dac9e96102dbc0bf7ac7a1753d671fa5a7b7f299

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
