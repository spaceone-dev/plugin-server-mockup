import os
import unittest
import time

from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json

class TestCollector(TestCase):

    def test_init(self):
        v_info = self.inventory.Collector.init({'options': {}})
        print_json(v_info)


    def test_verify(self):
        options = {
        }
        secret_data = {
            'spaceone_api_key': 'test key'
        }
        v_info = self.inventory.Collector.verify({'options': options, 'secret_data': secret_data})
        print_json(v_info)

    def test_collect(self):
        options = {'count':10, 'provider': 'spaceone'}
        secret_data = {
            'spaceone_api_key': 'create',
            'param_int_1': 10000,
            'param_int_2': 1
        }
        filter = {}

        for i in range(1):
            resource_stream = self.inventory.Collector.collect({'options': options, 'secret_data': secret_data,
                                                            'filter': filter})
            print(i)
        # print(resource_stream)

            for res in resource_stream:
                pass
                #print_json(res)



if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
