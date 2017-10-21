import time
import tornado.gen

import redis
redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)

REDIS_KEY = 'my_redis_key'

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

class RedisHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        package = redis_conn.get(REDIS_KEY)
        self.write(package.decode('utf-8') if package else 'REDIS_KEY empty')
        self.finish()

    @tornado.gen.coroutine
    def post(self):
        package = self.request.body.decode('utf-8')        
        redis_conn.set(REDIS_KEY, package)
        self.finish()