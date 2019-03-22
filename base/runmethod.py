#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 下午5:58
# @Author  : jaingtao.zhu
# @File    : runmethod.py

import requests
import json
from data.get_data import GetData
from util.operation_json import OperetionJson


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    runMethod = RunMethod()
    jsonAction = OperetionJson()
    result = runMethod.run_main('Post', 'http://m.imooc.com/passport/user/login', jsonAction.get_data('user'))
    print(result)
    pass
