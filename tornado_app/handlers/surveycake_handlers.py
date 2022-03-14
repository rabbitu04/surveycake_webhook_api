import json
import requests

from base64 import b64decode
from connect_mongo import Connect
from Crypto.Cipher import AES
from datetime import datetime
from tornado.web import RequestHandler

db = Connect.get_connection()['testDB']

url = 'https://shareparty.surveycake.biz/webhook/v0/'
# url = 'https://www.surveycake.com/webhook/v0/'


class ApiParamsHandler(RequestHandler):
    
    def check_xsrf_cookie(self):
        pass
    
    def post(self, hash_key, iv_key):
        cipher = AES.new(hash_key.encode('utf-8'), AES.MODE_CBC, iv_key.encode('utf-8'))
        svid = self.get_argument('svid', '')
        logging.info
        
        hash_code = self.get_argument('hash', '')
        if svid and hash_code:
            params = {
                'svid': svid,
                'hash': hash_code,
            }
            ct = requests.get(url + svid + '/' + hash_code).content
            pt = cipher.decrypt(b64decode(ct))
            pt = b'{"svid":' + pt.split(b'svid":')[1].split(b']}]}')[0] + b']}]}'
            pt = pt.decode('unicode_escape')

            survey = json.loads(pt)

            db.surveycake.insert_one({
                'params': params,
                'survey': survey,
            })
        return
