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


def getCSVTable(filename=0):
    if filename==0:
        # Open file dialog if no filename is given.
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename()

    dataTable = []
    fieldNames = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # Clean up field names
        fieldNames = next(reader)
        for i, field in enumerate(fieldNames):
            fieldNames[i] = fieldNames[i].strip()
        print(fieldNames)

        for row in reader:
            thisRecord = {}
            for i, item in enumerate(row):
                try:
                    thisRecord[fieldNames[i]] = float(item)
                except:
                    thisRecord[fieldNames[i]] = item

            dataTable.append(thisRecord)
    return dataTable

#%% Analysis Tools
    
def diff(value,time,maxRate=-1):
    diffValue = np.diff(value)
    diffTime = np.diff(time)
    diffRate = diffValue/diffTime
    # Cap rate outputs at maxRate to avoid outliers (low efficiency loop)
    for i, iRate in enumerate(diffRate):
        if maxRate != -1 and abs(iRate) > maxRate:
            diffRate[i] = 0
    return diffRate
    

#%% Visualization Routines

def plotJewelArm(dataTable):
    # Extract data as lists using list comprehensions.
    time = [record['time'] for record in dataTable]
    jewelArm = [record['JEWEL_ARM'] for record in dataTable]
    plt.figure(1)
    plt.clf()
    plt.title("Jewel Arm over time")
    plt.plot(time,jewelArm, 'r--', label='jewelArm')
    plt.xlabel('Time (s)')
    plt.ylabel('Jewel Arm Servo [0,1]')
    plt.legend()
    plt.show()

def plotXYPosition(dataTable):
    # Extract data as lists using list comprehensions.
    time = [record['time'] for record in dataTable]
    x = [record['x_in'] for record in dataTable]
    y = [record['y_in'] for record in dataTable]
    theta = [record['theta_rad'] for record in dataTable]
    plt.figure(2)
    plt.clf()
    plt.title("Mecanum Navigation Position")
    plt.plot(x,y, 'r--.', label='position')
    plt.xlabel('X inches')
    plt.ylabel('Y inches')
    plt.legend()
    plt.show()
    
def plotMotorTickRateVsPower(dataTable):
    # Extract data as lists using list comprehensions.
    time = [record['time'] for record in dataTable]
    motorTicks = [record['DRIVE_FRONT_LEFT_ticks'] for record in dataTable]
    motorTickRate = diff(motorTicks,time)
    motorPower = [record['DRIVE_FRONT_LEFT_power'] for record in dataTable]
    plt.figure(3)
    plt.clf()
    plt.title("Motor Ticks vs Power")
    plt.plot(motorPower[0:-1], motorTickRate, 'b.', label='position')
    plt.xlabel('Power')
    plt.ylabel('Tick Rate')
    plt.legend()
    plt.show()

#%% Main routine, run if module is executed directly, rather than imported.    

def main():
    #dataTable = getCSVTable('telemetry1.csv')
    dataTable = getCSVTable()
    plotJewelArm(dataTable)
    plotXYPosition(dataTable)
    plotMotorTickRateVsPower(dataTable)


if __name__ == '__main__':
    main()


