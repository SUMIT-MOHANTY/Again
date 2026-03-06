#!/bin/sh
set -e
flask db upgrade || true
exec gunicorn -b 0.0.0.0:5000 "backend.__main__:app"
