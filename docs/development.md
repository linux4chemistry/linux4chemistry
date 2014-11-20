This document illustrates how to setup a local development environemnt and run a personal instance of the Linux4Chemistry website.


Requirements
------------

I will obviously assume you will be using Linux (although most of the instructions will work for other Operating Systems too), and I will also assume that the Anaconda python distribution will be used (this is also not strictly required, but very convenient).


Setup
-----

Fork the Linux4Chemistry project on GitHub, and then create a local clone of your own git repository:

  $ git clone git@github.com:rvianello/linux4chemistry.git

Install the project dependencies in a dedicated conda environment:

  $ cd linux4chemistry
  $ conda create -c l4c -n l4c -f conda-spec.txt
  $ source activate l4c
  (l4c) $ pip install -r pip-requirements.txt 

Configure the project settings for development:

  (l4c) $ pushd ./l4c_db/linux4chemistry/settings
  (l4c) $ ln -s development.py __init__.py
  (l4c) $ popd

Create the directory where the sqlite database will be placed:

  (l4c) $ mkdir ../dev-data

Create the project's database. 'syncdb' will prompt the user for the creation of a superuser account. Answer 'yes' and enter some simple user credentials (this account will be used to access the django admin interface and manipulate the database).

  (l4c) $ pushd ./l4c_db
  (l4c) $ python manage.py syncdb
  (l4c) $ python manage.py migrate l4c

Load the database with the json fixture that is stored in l4c_db/l4c/fixtures/

  (l4c) $ python manage.py l4c_load

And finally complete the setup with copying the project static files to the proper location from where they will be served:

  (l4c) $ python manage.py collectstatic
  (l4c) $ popd


Running the local server
------------------------

A simple bash script is provided, allowing to start uwsgi in the development environment and use it as an alternative to the django development server:

  (l4c) $ ./runserver.sh 

While the uwsgi server is running, a local instance of the Linux4Chemistry website will be available at http://127.0.0.1:8000. The uwsgi server will be running in the foreground inside the original shell, logging every incoming request. It can be stopped with a simple ctrl-C.



