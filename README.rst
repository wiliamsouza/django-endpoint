
Commands used to create this project::

    $ cd ~
    $ mkdir devel
    $ cd devel
    $ git clone git@github.com:wiliamsouza/django-endpoint.git
    $ cd django-endpoint
    $ virtualenv-3.2 .
    $ touch README.rst
    $ git add README.rst
    $ git commit -m "Added README.rst"
    $ touch setup.py
    $ git add setup.py
    $ git commit -m "Added setup.py"
    $ touch tox.ini
    $ git add tox.ini
    $ git commit -m "Added tox.ini"
    $ echo 'https://www.djangoproject.com/download/1.5b2/tarball/' > requirements.tst
    $ git add requirements.txt
    $ git commit -m "Added requirements.txt"
    $ pip -r install requirements.txt
    $ echo 'tox' > test-requirements.txt
    $ git add test-requirements.txt
    $ git commit -m "Added test-requirements.txt"
    $ pip -r install test-requirements.txt
    $ touch .gitignore
    $ git add .gitignore
    $ git commit -m "Added .gitignore"
    $ django-admin.py startproject django_endpoint
    $ git add django_endpoint/
    $ git commit -m "Created initial django project"
    $ cd django_endpoint/
    $ python manage.py startapp console
    $ git add console/
    $ git commit -m "Created initial app console"
    $ python manage.py startapp authorization
    $ git add authorization/
    $ git commit -m "Created initial app authorization"
    $ mkdir -p tests/fixtures
    $ touch tests/fixtures/.gitkeep
    $ git add tests/
    $ git commit -m "Added tests and tests fixtures folder"
    $ mkdir tests/authorization
    $ mkdir tests/console
    $ git mv authorization/tests.py tests/authorization/
    $ git mv console/tests.py tests/console/
    $ git commit -m "Moved initial tests from app folders to tests folder"

Added the following to .gitignore::

    bin/
    lib/
    .tox/
    *.pyc
    include/
    __pycache__

