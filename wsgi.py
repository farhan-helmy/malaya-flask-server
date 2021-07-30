import sys
import site

site.addsitedir('/var/www/malaya-sentiment-analysis/lambda_venv/lib/python3.7/site-packages')

sys.path.insert(0, '/var/www/malaya-sentiment-analysis')

from app import app as application
