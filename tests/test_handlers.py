import io 
import app
from unittest.mock import patch
from tornado.testing import AsyncHTTPTestCase

class HandlersTest(AsyncHTTPTestCase):
    """Test to check subscriber module."""

    def get_app(self):
        return app.make_app()

    def tearDown(self):
        pass
        
    def test_if_return_block_message_at_block_api(self):
        response = self.fetch('/block-request')
        self.assertEqual(response.code, 200)

        api_response = response.body.decode('utf-8')
        self.assertEqual(api_response, 'Hello, world - Block')

    def test_if_return_non_block_message_at_non_block_api(self):
        response = self.fetch('/non-block-request')
        self.assertEqual(response.code, 200)

        api_response = response.body.decode('utf-8')
        self.assertEqual(api_response, 'Hello, world - Yield Block')

    def test_if_return_normal_message_at_normal_api(self):
        response = self.fetch('/normal-request')
        self.assertEqual(response.code, 200)

        api_response = response.body.decode('utf-8')
        self.assertEqual(api_response, 'Hello, world - Normal')

    @patch('handlers.redis_conn.set')
    def test_if_can_integrate_with_redis(self, redis_mock):

        response = self.fetch('/redis-request', method='POST', body="body test")
        self.assertEqual(response.code, 200)        
        redis_mock.assert_called_with('my_redis_key', "body test")

    @patch('handlers.redis_conn.get')
    def test_if_can_integrate_with_redis(self, redis_mock):

        redis_mock.side_effect = lambda x: b'body test'

        api_response = self.fetch('/redis-request')
        self.assertEqual(api_response.code, 200)

        api_response = api_response.body.decode('utf-8')
        self.assertEqual(api_response, 'body test')