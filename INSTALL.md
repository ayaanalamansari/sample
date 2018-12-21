Region-Management
=================

# Important Notes

This guide is long because it covers many cases and includes all commands you need.

This installation guide was created for and tested on **Ubuntu 16.04** operating systems.

This is the official installation guide to set up a production server. To set up a **development installation** and to contribute read `Contributing.md`.

The following steps have been known to work. Please **use caution when you deviate** from this guide. Make sure you don't violate any assumptions Region_Management makes about its environment.

# Overview

The  Region_Management installation consists of setting up the following components:

1. Packages / Dependencies
1. System Users
1. Database
1. Region_Management
1. Supervisor
1. Nginx
1. Update Existing Setup to Newer Version

## Packages / Dependencies

Run following commands

    sudo apt-get update
    sudo apt-get -y upgrade

**Note:** During this installation some files will need to be edited manually. If you are familiar with vim set it as default editor with the commands below. If you are not familiar with vim please skip this and keep using the default editor.

    # Install vim and set as default editor
    sudo apt-get install -y vim-gnome
    sudo update-alternatives --set editor /usr/bin/vim.gnome

Install the required packages (needed to compile Ruby and native extensions to Ruby gems):

    sudo apt-get install -y build-essential git-core libssl-dev libffi-dev curl redis-server checkinstall libcurl4-openssl-dev python-docutils pkg-config python3-dev python-dev python-virtualenv

**Note:** In order to receive mail notifications, make sure to install a mail server. The recommended mail server is postfix and you can install it with:

    sudo apt-get install -y postfix

Then select 'Internet Site' and press enter to confirm the hostname.

# System Users

Create a `region_management` user for Region_Management:

    sudo adduser --disabled-login --gecos 'Region_Management' region_management

# Database

We recommend using a PostgreSQL database.

    # Install the database packages
    sudo apt-get install -y postgresql postgresql-client libpq-dev

    # Login to PostgreSQL
    sudo -u postgres psql -d postgres

    # Create a user for Region_Management
    # Do not type the 'postgres=#', this is part of the prompt
    postgres=# CREATE USER region_management WITH PASSWORD '123456' CREATEDB;

    # Create the Region_Management production database & grant all privileges on database
    postgres=# CREATE DATABASE region_management_production OWNER region_management;

    # Quit the database session
    postgres=# \q

    # Try connecting to the new database with the new user
    sudo -u region_management -H psql -d region_management_production

    # Quit the database session
    region_management_production> \q

# Region-Management

    # We'll install Region_Management into home directory of the user "region_management"
    cd /home/region_management

## Clone the Source

    # Clone Region_Management repository
    sudo -u region_management -H region_management clone https://github.com/region_management/region_management.git region_management

## Configure It

    # Switch User region_management
    sudo su region_management

    # Go to Region_Management installation folder
    cd /home/region_management/region_management

    # Virtual Envirnoment and requirements
    virtualenv -p /usr/bin/python3.6 env
    source env/bin/activate
    pip install -r requirements.txt

## Project and Database Configuartion Settings

    # Edit desired configurations in config/local.py i.e. STATICFILES_DIRS
    cp config/local.py.example config/local.py
    chmod o-rwx config/local.py
    editor config/local.py

Example:

        DEBUG = False

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'region_management_production',
                'USER': 'region_management',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '',
            }
        }

## Validate configurations

    ./manage.py validate

## Migrate Database & Seed Default Data

    ./manage.py migrate
    ./manage.py loaddata fixtures/default.json

## Load Assets

    ./manage.py collectstatic

## Gunicorn Or uWSGI

    # Copy either of the configuration file for respective server
    cp scripts/gunicorn.bash scripts/runserver.bash

    OR

    cp scripts/uwsgi.bash scripts/runserver.bash

    # Make it executable
    chmod u+x scripts/runserver.bash

## Celery & Celerybeat

    cp scripts/celery.bash.example scripts/celery.bash
    cp scripts/celerybeat.bash.example scripts/celerybeat.bash

## Exit User region_management

    exit

# Supervisor

## Installation

    sudo apt-get install -y supervisor

    # Go to Region_Management installation folder
    cd /home/region_management/region_management

## Configuration

    sudo cp config/supervisor/region_management.conf /etc/supervisor/conf.d/region_management.conf
    sudo cp config/supervisor/region_management_celery.conf /etc/supervisor/conf.d/region_management_celery.conf
    sudo cp config/supervisor/region_management_celerybeat.conf /etc/supervisor/conf.d/region_management_celerybeat.conf

## Supervisor Configuration Update

    sudo service supervisor restart
    sudo supervisorctl reread
    sudo supervisorctl update

# Nginx

## Installation

    sudo apt-get install -y nginx

## Site Configuration

    # Copy the example site config:
    sudo cp config/nginx/region_management /etc/nginx/sites-available/region_management
    sudo ln -s /etc/nginx/sites-available/region_management /etc/nginx/sites-enabled/region_management

Make sure to edit the config file to match your setup:

    # Change YOUR_SERVER_FQDN to the fully-qualified
    # domain name of your host serving Region_Management.
    sudo editor /etc/nginx/sites-available/region_management

**Note:** If you want to use HTTPS, replace the `region_management` Nginx config with `region_management-ssl`. See [Using HTTPS](#using-https) for HTTPS configuration details.

## Test Configuration

Validate your `region_management` or `region_management-ssl` Nginx config file with the following command:

    sudo nginx -t

You should receive `syntax is okay` and `test is successful` messages. If you receive errors check your `region_management` or `region_management-ssl` Nginx config file for typos, etc. as indicated in the error message given.

## Provide access to static files and error templates

    sudo adduser nginx region_management
    sudo chmod -R 750 /home/region_management/region_management/static/
    sudo chmod -R 750 /home/region_management/region_management/templates/

## Restart

    sudo service nginx restart

# Update Existing Setup to Newer Version


# Using HTTPS

To use Region_Management with HTTPS:


Using a self-signed certificate is discouraged but if you must use it follow the normal directions then:

1. Generate a self-signed SSL certificate:

    ```
    mkdir -p /etc/nginx/ssl/
    cd /etc/nginx/ssl/
    sudo openssl req -newkey rsa:2048 -x509 -nodes -days 3560 -out region_management.crt -keyout region_management.key
    sudo chmod o-r region_management.key
    ```
