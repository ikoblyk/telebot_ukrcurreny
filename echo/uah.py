import requests


class BittrexClient(object):

    def __init__(self):
        self.base_url = "https://api.bittrex.com/api/v1.1/public/getticker?market"

    def request(self, params, method):
        url = self.base_url+method

        r = requests.get(url=url, params=params)
        result = r.json()
        return  result

    def get_ticker(self, pair):
        params = {
            "market": pair

        }
        return self.request(method="public/getticker", params=params)

    def l_price(self, pair):
        res = self.get_ticker(pair = pair)
        return res["result"]["Last"]


class Curshrn():
    def __init__(self):
        self.url = urlopen()

