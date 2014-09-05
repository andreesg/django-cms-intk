=========
Collections
=========

Collection plugin for django CMS 3.

Quick start
-----------

0. Install djangocms-simpletext from https://github.com/intk/djangocms-simpletext

1. Add "rich_collection" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'djangocms_simpletext',
    )

3. Execute migration or syncdb to create the rich_collection models::

    $ python manage.py syncdb

    $ python manage.py migrate

=====
Usage
=====


