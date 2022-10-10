import yaml
import requests


class Util:
    @classmethod
    def get_conf(cls):
        with open('../conf/conf.yaml','r',encoding='utf8') as f:
            data = yaml.load(f,Loader=yaml.FullLoader)
            return data

