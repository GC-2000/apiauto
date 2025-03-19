import json

import pytest
import requests
from read_data import yaml_read


# @pytest.mark.parametrize(['user', 'pwd'], [['admin', '123456'], ['admin', ' ']])
token = None

@pytest.mark.parametrize('data', yaml_read.read('./data/user.yaml'))
def test_logon(data):
    url = ''
    # data = {
    #     'username': user,
    #     'password': pwd
    # }
    res = requests.post(url=url, json=data['user'])
    print(res.text)
    result = json.load(res.text)
    try:
        global token
        token = result['token']
    except:
        pass

    assert data['msg'] == result['msg']



