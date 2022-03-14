from tornado.web import RequestHandler
from connect_mongo import Connect

class HelloWorldHandler(RequestHandler):
    
    def get(self):
        print()
        print('Hello from', self.request.remote_ip)
        return self.write('Hello World')


class TestDBHandler(RequestHandler):

    def get(self):
        print()
        print('Test connect database')
        db = Connect.get_connection()['testDB']
        obj = db.test.find_one({}, {'_id': 0})
        return self.write(dict(obj))


class TestArgsHandler(RequestHandler):

    def get(self, hash_key, iv_key):
        return self.write({
            'hash key': hash_key,
            'iv key': iv_key,
        })