import os
import site
import sys

site.addsitedir(os.path("/var/www/Sleeping_disorder_detection/venv/lib/python3.10/site-packages"))

sys.path.insert(0, '/var/www/Sleeping_disorder_detection')

from app import app as application
