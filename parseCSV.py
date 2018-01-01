# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 03:15:32 2017

@author: Ashley
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
# File Dialog
import tkinter as tk
from tkinter import filedialog


def getDictionary(filename=0):
    if filename==0:
        # Open file dialog if no filename is given.
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename()
        print(filename)
        print()

    dataTable = {}
    fieldNames = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # Clean up field names
        fieldNames = next(reader)
        for i, field in enumerate(fieldNames):
            fieldNames[i] = fieldNames[i].strip()
            # Populate dictionary names with empty lists.
            dataTable[fieldNames[i]] = []
        print(fieldNames)

        for row in reader:
            for i, item in enumerate(row):
                try:
                    newDataItem = float(item)
                except:
                    newDataItem = item
                dataTable[fieldNames[i]].append(newDataItem)
    return dataTable

#%% Main routine, run if module is executed directly, rather than imported.

def main():
    print("getDictionary(filename) is loaded.")


if __name__ == '__main__':
    main()

