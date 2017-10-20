import tornado.ioloop
import tornado.web

from handlers import BlockHandler, NonBlockHandler, DefaultHandler

import logging
LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def make_app():
    return tornado.web.Application([
        (r"/block-request", BlockHandler),
        (r"/non-block-request", NonBlockHandler),
        (r"/normal-request", DefaultHandler)
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()