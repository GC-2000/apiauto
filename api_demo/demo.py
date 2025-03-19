# 导入request来实现接口自动化测试

import requests

url = ''
data = {
    'username': 'admin',
    'password': '123456'
}

res = requests.post(url=url, json=data)
print(res.text)