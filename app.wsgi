import site
import sys
from pathlib import Path

site.addsitedir(Path("/var/www/Sleeping_disorder_detection/venv/lib/python3.10/site-packages"))

sys.path.insert(0, '/var/www/Sleeping_disorder_detection')

from app import app as application
