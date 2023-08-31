import json
import time
import requests
from utils import read_config


def update_node_name():
    heands = {"Connection": "keep-alive",
              "Content-Type": "application/json;charset=UTF-8",
              "Cookies": "JSESSIONID=CD579C23A983C7520F3A708DB714D312; JSESSIONID=4072DE381BBB6DAF8A1BBE6FAFE9FE6B"
              }
    data = {"nodeId": "",
            "name": "自动创建_%s" % time.strftime('%Y%m%d_%H_%M_%S', time.localtime()),
            "nameEn": "",
            "lang": "zh",
            "authProjectId": "10",
            "treeId": "ZGHG"}
    response = requests.get(read_config.get_nodeId_url(), headers=heands)
    if response.status_code == 200:
        data['nodeId'] = json.loads(response.text)['data']['children'][-1]['nodeId']
        response = requests.post(read_config.post_update_url(), headers=heands, data=json.dumps(data))
        if response.status_code == 200:
            return True
        else:
            return False
