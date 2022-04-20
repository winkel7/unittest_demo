import requests


class RequestHandler:
    sess = requests.session()

    def handle_request(self, url, method, params=None, data=None, json=None, **kwargs):
        res = self.sess.request(url, method, params=params, data=data, json=json, **kwargs)
        return res

    def __del__(self):
        self.sess.close()
