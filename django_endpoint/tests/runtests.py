#!/usr/bin/env python
import os
import sys

from django.test.utils import get_runner
from django_endpoint import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_endpoint.settings")

def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['test_app'])
    sys.exit(bool(failures))

if __name__ == "__main__":
    runtests()
