import time
import hashlib
import uuid
import json
import requests
import ct_config

class CT_API:
    def __init__(self, ct_config):
        self.userid = ct_config.userid
        self.private_key = ct_config.private_key
        self.sessionid = ct_config.sessionid
        self.pin = ct_config.pin
        self.pintoken = ct_config.pintoken
        # mixin api base url
        self.api_base_url = 'http://leaper.one'

    """
    BASE METHON
    """
    def __genUrl(self, path):
        return self.api_base_url + path

    """
    generate GET http request
    """
    def __genGetRequest(self, path):
        url = self.__genUrl(path)
        r = requests.get(url)
        return r.json()

    """
    generate POST http request
    """
    def __genPostRequest(self, path, body):
        # generate url
        url = self.__genUrl(path)
        r = requests.post(url, json=body)
        return r.json()

    """
    METHON
    """
    def creat_id(self):
        return self.__genGetRequest('/api/v1/creat_id/')

    def pub(self, data, pin='000000'):

        body = {
                'userid': self.userid,
                'data': data,
                'pintoken': self.pintoken,
                'private_key': self.private_key,
                'pin': pin,
                'sessionid': self.sessionid
        }

        return self.__genPostRequest('/api/v1/pub/', body)
