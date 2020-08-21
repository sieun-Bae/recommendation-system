import pandas as pd

from bs4 import BeautifulSoup
import json

import requests
import time
import sys


## key ##
key = '56627a7a52716f743637486e52564f'
key_place_ = '72496f7145716f7439315742664153'

## params ##
'''
FORM = 'json'
START_IDX = 1 
END_IDX = 30
FAC_CODE = ''
'''

## url ##
'''
url = f'http://openAPI.seoul.go.kr:8088/{key_}/{FORM}/SearchCulturalFacilitiesTrafficService/{START_IDX}/{END_IDX}/{FAC_CODE}'
'''

## store data ##
INFO = {}

def load_(url, start_idx, end_idx):
	# iterate while end_num reach END_IDX #
	#while end_num <= END_IDX:

	lm_json = requests.get(url).json()
	elements = lm_json['SearchCulturalFacilitiesTrafficService']['row']
	attr_ = ['FAC_CODE', 'FAC_NAME', 'TRAFTYPE', 'TRAFINFO']
	
	INFO = pd.DataFrame(data = elements, dtype = str, columns = attr_)
	print(INFO)
	return INFO

def load_traffic_():
	key_ = '72496f7145716f7439315742664153'	
	
	# set params #
	FORM = 'json'
	START_IDX = 1
	END_IDX = 5
	FAC_CODE = ''
	
	url = f'http://openAPI.seoul.go.kr:8088/{key_}/{FORM}/SearchCulturalFacilitiesTrafficService/{START_IDX}/{END_IDX}/{FAC_CODE}'
	
	load_(url, START_IDX, END_IDX)

def main():
	if sys.argv[1] == 'traffic':
		load_traffic_()
	else:
		print('command: python loadData_ \'traffic\' or something.')

if __name__ == '__main__':
	main()
