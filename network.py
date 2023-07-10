import os
import re
import requests
import json


def getIPv6Address():
    output = os.popen("ipconfig /all").read()
    # print(output)
    result = re.findall(
        r"临时 IPv6 地址. . . . . . . . . . : (([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})", output, re.I)
    return result[0][0]


def dns_records():
    headers = {
        'X-Auth-Email': 'xxxxx@163.com',
        'X-Auth-Key': 'xxxxxx',
        'Content-Type': 'application/json',
    }

    data = '{"type":"AAAA","name":"temp.sakurakoi.top","content":"' + \
        getIPv6Address()+'","ttl":1,"proxied":false}'

    response = requests.put(
        'https://api.cloudflare.com/client/v4/zones/xxxxx/dns_records/xxxxx', headers=headers, data=data)
    success = json.loads(response.text).get('success')
    if success:
        print("已经成功替换啦！")
    else:
        print("替换失败....看看哪里填错了？或者在GitHub问问？")


if __name__ == "__main__":
    dns_records()
