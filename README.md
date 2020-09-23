# Server Collector Mockup

# Introduction

This is for developer only.
Work as collector like aws-ec2 collector or gcp-compute collector.

Based on secret_data, this can do various actions.

## Secret Data format

~~~python
secret_data = {
	'spaceone_api_key': string,
	'param_int_1': integer,
	'param_int_2': integer,
	'param_str_1': string,
	'param_str_2': string
}
~~~

You can send various command to plugin.

# Command

| Command	| param_int_1  (default)	| param_int_2 		| param_str_1 	| param_str_2 	|
| ------- 	| -------     			| ------      		| -----       	| ------      	|
| create  	| number of resource(10)  	| response after (10) 	|             	|             	|
| error   	|                             	|                       |             	|             	|
| create_1	| number of resource(10)	| response after(100)	|		|		|


## create_1

return param_int_1 resources after param_int_2 seconds
