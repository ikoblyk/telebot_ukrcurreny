import requests
from logging import getLogger


logger = getLogger(__name__)


class hr(object):

    def __init__(self):
        self.base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange "

    def request(self, params, method):
        url = self.base_url+method

        r = requests.get(url=url, params=params)
        result = r.json()
        return  result


        self.request(method="public/getticker")

    def l_price(self, pair):
        res = self.get_ticker(pair = pair)
        return res["27"]["txt"]