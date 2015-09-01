# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:37:42 2015

@author: chris
"""

import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]