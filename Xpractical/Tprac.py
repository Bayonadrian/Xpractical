from lxml import html
import requests

class prac:

    def __init__(self, url: str) -> None:
        
        self.req = requests.get(url).content
        self.xml = html.fromstring(self.req)
        self.path = self.xml.xpath

    def uCommand(self, xpath: str):

        return self.path(xpath)


