import json
import time
import pymongo
import sys
import urllib.parse
import base64
import traceback
import random
import urllib.request
import io
import requests
import json
import hashlib
import os

sys.path.append("pytavia_core")
sys.path.append("pytavia_settings")
sys.path.append("pytavia_stdlib")
sys.path.append("pytavia_storage")
sys.path.append("pytavia_modules")
sys.path.append("pytavia_modules")


from flask             import render_template_string
from flask             import render_template
from flask             import request

from pytavia_stdlib    import idgen
from pytavia_stdlib    import utils
from pytavia_core      import database
from pytavia_core      import config
from pytavia_core      import helper
from pytavia_core      import bulk_db_insert
from pytavia_core      import bulk_db_update
from pytavia_core      import bulk_db_multi

class delete_user_data:    
    mgdDB = database.get_db_conn(config.mainDB)         

    def __init__(self, app):
        self.webapp = app        
    # end def

    def process(self, params):        
        response = helper.response_msg(
            "CREATE_COMPANY_SUCCESS",
            "CREATE COMPANY SUCCESS", {},
            "0000"
        )  
        self.webapp.logger.debug(params)
        id_user = params['delete']
        
        # delete token user
        query_db_scripts  = {"user_id":id_user}
        delete_result = self.mgdDB.db_token_access.delete_many(query_db_scripts)
        
        x = self.mgdDB.db_users.delete_one(
            { "pkey"          : id_user }   
        )  
       
        response = {
            'kboom' : 'LIST_USER'
        }

        return response
    # end def    
# end class
