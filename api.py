import requests
import json
import os

class ScamSearchAPI:
    def __init__(self):
        self.api_key = os.environ.get('SS_API_KEY')
        if not self.api_key:
            with open('api.txt', 'r') as f:
                api_key = f.read().strip()
        self.base_url = "https://scamsearch.io/api/"

    def report_scammer(self, bitcoin_address, scam_type, scammer_username=None, scammer_email=None, scammer_phone=None, scam_description=None):
        url = self.base_url + "create_report"
        params = {
            "api_token": self.api_key,
            "bitcoinaddress": bitcoin_address,
            "scammertype": scam_type,
            "scammerusername": scammer_username,
            "scammeremail": scammer_email,
            "scammerphone": scammer_phone,
            "scamdescription": scam_description
        }
        response = requests.post(url, data=params)
        return response.json()

    def search_exact_match(self, search_string, search_type):
        url = self.base_url + "search"
        params = {
            "api_token": self.api_key,
            "search": search_string,
            "type": search_type
        }
        response = requests.get(url, params=params)
        return response.json()

    def search_wild_card(self, search_string, search_type):
        url = self.base_url + "search-with-wild"
        params = {
            "api_token": self.api_key,
            "search": search_string,
            "type": search_type
        }
        response = requests.get(url, params=params)
        return response.json()

if __name__ == "__main__":
    pass
   
