#!/bin/bash
killall -9 gunicorn
gunicorn -c config/gunicorn_config.py aldryn_cms.wsgi --daemon --log-level=debug --log-file=config/logs/aldryn.log
