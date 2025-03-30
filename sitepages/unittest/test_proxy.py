# coding:utf-8

import unittest

from requests import Session

from sitepages.proxy import ProxyProtocol
from sitepages.proxy import ProxySession


class TestProxy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.host: str = "127.0.0.1"
        cls.port: int = 12345

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_proxy(self):
        self.assertRaises(ValueError, ProxySession,
                          ProxyProtocol.HTTP.value,
                          self.host, self.port)

    def test_http_proxy(self):
        proxies = {
            "http": f"{ProxyProtocol.HTTP.value}://{self.host}:{self.port}",
            "https": f"{ProxyProtocol.HTTP.value}://{self.host}:{self.port}"
        }
        proxy_session = ProxySession.http_proxy(self.host, self.port)
        self.assertEqual(proxy_session.proxies, proxies)
        self.assertIsInstance(proxy_session, Session)

    def test_https_proxy(self):
        proxies = {
            "http": f"{ProxyProtocol.HTTPS.value}://{self.host}:{self.port}",
            "https": f"{ProxyProtocol.HTTPS.value}://{self.host}:{self.port}"
        }
        proxy_session = ProxySession.https_proxy(self.host, self.port)
        self.assertEqual(proxy_session.proxies, proxies)
        self.assertIsInstance(proxy_session, Session)

    def test_socks4_proxy(self):
        proxies = {
            "http": f"{ProxyProtocol.SOCKS4.value}://{self.host}:{self.port}",
            "https": f"{ProxyProtocol.SOCKS4.value}://{self.host}:{self.port}"
        }
        proxy_session = ProxySession.socks4_proxy(self.host, self.port)
        self.assertEqual(proxy_session.proxies, proxies)
        self.assertIsInstance(proxy_session, Session)

    def test_socks5_proxy(self):
        proxies = {
            "http": f"{ProxyProtocol.SOCKS5.value}://{self.host}:{self.port}",
            "https": f"{ProxyProtocol.SOCKS5.value}://{self.host}:{self.port}"
        }
        proxy_session = ProxySession.socks5_proxy(self.host, self.port)
        self.assertEqual(proxy_session.proxies, proxies)
        self.assertIsInstance(proxy_session, Session)


if __name__ == "__main__":
    unittest.main()
