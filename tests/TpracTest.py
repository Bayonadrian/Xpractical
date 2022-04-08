from os import pread
from Xpractical.Tprac import prac
import requests
import unittest

class pracTest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.url = 'https://toscrape.com/'
        self.prac = prac(self.url)
        self.pracReq = self.prac.req
        self.text = self.prac.uCommand('//h1/text()')

    def test_req(self):

        self.assertEqual(requests.get(self.url).content, self.pracReq)

    def test_uCommmand(self):

        self.assertEqual(self.text, ['Web Scraping Sandbox'])