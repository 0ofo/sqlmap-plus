import base64
import time


class default:
    def __init__(self):
        pass

    def filter(self, payload):
        # time.sleep(0.5)
        # print(payload)
        return payload
        # return self.double(payload)

    @staticmethod
    def double(payload):
        payload = payload \
            .replace('and', 'anandd') \
            .replace('or', 'oorr')
        return payload

    @staticmethod
    def base64(payload):
        payload = base64.b64encode(payload.encode('utf-8'))
        return str(payload)
