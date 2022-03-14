import os

from tornado.ioloop import IOLoop
from tornado.web import Application
from handlers.hello_world_handlers import HelloWorldHandler, TestDBHandler, TestArgsHandler
from handlers.surveycake_handlers import ApiParamsHandler
        

def make_app():
    
    print('-' * 10, 'APP START', '-' * 10)

    routers = [
        # Base
        (r'/hello-world', HelloWorldHandler),
        (r'/test-db', TestDBHandler),
        (r'/test-args/([a-z0-9]{16})/([a-z0-9]{16})', TestArgsHandler),
        # SurveyCake
        (r'/surveycake/recipient/([a-z0-9]{16})/([a-z0-9]{16})', ApiParamsHandler),
    ]

    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
    )

    return Application(routers, **settings)


    
if __name__ == '__main__':

    app = make_app()
    app.listen(11235)
    IOLoop.current().start()
