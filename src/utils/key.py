class Key(object):
    def __init__(self):
        pass

    def get_key(self,api_type):
        if api_type == "faceplusplus":
            key = "QHV8eEZ1oKvr9QWdzzHpAZYc3YN64c21"
            secret = "S626Pb1ZRLI1nDTPoYsf_i6uThYBSQTR"
            return key, secret
        else:
            print("uncorrect api type")
            return