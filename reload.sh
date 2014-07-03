#!/bin/bash
killall -9 gunicorn
gunicorn -c config/gunicorn_config.py aldryn_cms.wsgi
/etc/init.d/nginx restart
