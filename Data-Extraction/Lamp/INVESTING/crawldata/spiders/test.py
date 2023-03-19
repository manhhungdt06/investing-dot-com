import os
import re
import datetime
from pathlib import Path
current_folder = Path(__file__).parent.resolve()

name = 'Index'
# Keep this block
PATH = (os.getcwd())
PATHS = re.split('\\\\|/', PATH)
MIC = PATHS[len(PATHS)-1]
DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
LOG_TIME = datetime.now().strftime('%d')
custom_settings = {'LOG_FILE': LOG_PATH + '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log'}