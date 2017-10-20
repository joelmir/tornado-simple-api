import time
import tornado.gen

class BlockHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world - Block")
        time.sleep(5)
        self.finish()

class NonBlockHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world - Yield Block")
        yield tornado.gen.sleep(5)
        self.finish()

class DefaultHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world - Normal")
        self.finish()