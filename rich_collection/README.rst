=========
Collections
=========

Adds collections to django CMS 3 pages.

Quick start
-----------

0. Install djangocms-rich-page from https://github.com/andreesg/djangocms-rich-page

1. Add "rich_collection" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'rich_collection',
    )

3. Execute migration or syncdb to create the rich_collection models::

    $ python manage.py syncdb

    $ python manage.py migrate

=====
Usage
=====

You will find the following new items::

    Add Collection / Edit Collection
    Remove Collection

Add Collection - Allows to add a collection of rich pages to the current page.

Don't forget to choose "Rich Page" as the template for the current page ;) 
