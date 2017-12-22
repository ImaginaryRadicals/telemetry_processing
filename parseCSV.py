# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 03:15:32 2017

@author: Ashley
"""

import csv

with open('telemetry1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    fieldNames = next(reader)
    print(fieldNames)
    for row in reader:
        print(', '.join(row))
        