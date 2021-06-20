#! /usr/bin/python

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/mydir/contract')
import __init__
sys.path.insert(0, '/home/mydir/contract/contract')
from db_app import app as application
application.secret_key = 'anything you wish'
#from contract.db_app import main
#if __name__ == "__main__":
#    main()
