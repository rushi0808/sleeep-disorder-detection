import site
import subprocess
import sys

cmd = '. $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate /var/www/Sleeping_disorder_detection/venv && conda env list'
subprocess.call(cmd, shell=True, executable='/bin/bash')

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/Sleeping_disorder_detection/venv/lib/python3.10/site-packages')

sys.path.insert(0, "/var/www/Sleeping_disorder_detection/")

from app import app as application
