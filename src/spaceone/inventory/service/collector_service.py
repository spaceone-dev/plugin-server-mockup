# -*- coding: utf-8 -*-

import logging
import random
import copy
import time

from spaceone.core.error import *
from spaceone.core.service import *
from spaceone.core.pygrpc.message_type import *

from spaceone.inventory.error import *
from spaceone.inventory.service.aws_ec2 import aws_ec2

_LOGGER = logging.getLogger(__name__)

FILTER_FORMAT = [
    {
        'key': 'project_id',
        'name': 'Project ID',
        'type': 'str',
        'resource_type': 'SERVER',
        'search_key': 'identity.Project.project_id',
        'change_rules': [{
            'resource_key': 'data.compute.instance_id',
            'change_key': 'instance_id'
        }, {
            'resource_key': 'data.compute.region',
            'change_key': 'region_name'
        }]
    }, {
        'key': 'collection_info.service_accounts',
        'name': 'Service Account ID',
        'type': 'str',
        'resource_type': 'SERVER',
        'search_key': 'identity.ServiceAccount.service_account_id',
        'change_rules': [{
            'resource_key': 'data.compute.instance_id',
            'change_key': 'instance_id'
        }, {
            'resource_key': 'data.compute.region',
            'change_key': 'region_name'
        }]
    }, {
        'key': 'server_id',
        'name': 'Server ID',
        'type': 'list',
        'resource_type': 'SERVER',
        'search_key': 'inventory.Server.server_id',
        'change_rules': [{
            'resource_key': 'data.compute.instance_id',
            'change_key': 'instance_id'
        }, {
            'resource_key': 'data.compute.region',
            'change_key': 'region_name'
        }]
    }, {
        'key': 'instance_id',
        'name': 'Instance ID',
        'type': 'list',
        'resource_type': 'CUSTOM'
    },
    {
        'key': 'region_name',
        'name': 'Region',
        'type': 'list',
        'resource_type': 'CUSTOM'
    }
]


SUPPORTED_RESOURCE_TYPE = ['inventory.Server']

@authentication_handler
class CollectorService(BaseService):
    def __init__(self, metadata):
        super().__init__(metadata)

    @check_required(['options'])
    def init(self, params):
        """ init plugin by options
        """
        capability = {
            'filter_format': FILTER_FORMAT,
            'supported_resource_type': SUPPORTED_RESOURCE_TYPE
        }
        return {'metadata': capability}

    @transaction
    @check_required(['options','secret_data'])
    def verify(self, params):
        """ verify options capability
        Args:
            params
              - options
              - secret_data: may be empty dictionary

        Returns:

        Raises:
             ERROR_VERIFY_FAILED:
        """
        options = params['options']
        secret_data = params['secret_data']
        return {}

    @transaction
    @check_required(['options','secret_data', 'filter'])
    def list_resources(self, params):
        """ Get quick list of resources

        Args:
            params:
                - options
                - secret_data
                - filter

        Returns: list of resources
        """
        options = params['options']
        secret_data = params['secret_data']
        filters = params['filter']
        return self._execute(options, secret_data, filters)


    def _execute(self, options, secret_data, filters):
        """ Secret sends various parameters

        secret_data(dict) : {
            'spaceone_api_key': str,
            'param_int_1': int,
            'param_int_2': int,
            'param_str_1': str,
            'param_str_2': str
        }
        """
        results = []
        cmd = secret_data.get('spaceone_api_key', 'create')
        param_int_1 = secret_data.get('param_int_1', 10)
        param_int_2 = secret_data.get('param_int_2', 0)
        param_str_1 = secret_data.get('param_str_1', '')
        param_str_2 = secret_data.get('param_str_2', '')

        # Parse command
        if cmd == "create":
            results = self._create(param_int_1, param_int_2, param_str_1)
        elif cmd == "create_with_no_match":
            results = self._create_with_no_match(param_int_1, param_int_2, param_str_1)
        return results

    def _create(self, num_of_resources, response_after, provider):
        results = []
        res = aws_ec2
        if provider == 'aws':
            res = aws_ec2
        else:
            res = aws_ec2

        for i in range(int(num_of_resources)):
            id = random.randrange(100000, 200000)
            instance_id = f'i-{id}'
            print(instance_id)
            res_data = copy.deepcopy(res)
            resource = res_data['resource']
            resource.update({'reference':
                                {'resource_id': f'arn:aws:ec2:test-region:11111111111:instance/{instance_id}'},
                             'provider': provider
                             })
            res_data['resource'] = resource
            results.append(res_data)
        time.sleep(response_after)
        return results

    def _create_with_no_match(self, num_of_resources, response_after, provider):
        results = []
        res = aws_ec2
        if provider == 'aws':
            res = aws_ec2
        else:
            res = aws_ec2

        for i in range(int(num_of_resources)):
            id = random.randrange(100000, 200000)
            instance_id = f'i-{id}'
            print(instance_id)
            res_data = copy.deepcopy(res)
            resource = res_data['resource']
            resource.update({'reference':
                                {'resource_id': f'arn:aws:ec2:test-region:11111111111:instance/{instance_id}'},
                             'provider': provider
                             })
            res_data['resource'] = resource
            results.append(res_data)
        time.sleep(response_after)
        return results


