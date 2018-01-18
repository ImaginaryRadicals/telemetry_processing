# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 21:00:52 2017

@author: Ashley
"""

# getCSVTable
import parseCSV
import math
#import csv
import matplotlib.pyplot as plt
import numpy as np
# File Dialog
import tkinter as tk
from tkinter import filedialog


#%%

def openFileDialog():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    return filename


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

def plotServos(dataTable):
    time = dataTable['time']
    jewelArm = dataTable['JEWEL_ARM']
    plt.clf()
    plt.title("Servo Positions")
    plt.plot(time,jewelArm, '-', label='jewelArm')
    plt.plot(time,dataTable['CLAW_LEFT'],'-.', label='clawLeft')
    plt.plot(time,dataTable['CLAW_RIGHT'], ':', label='clawRight')
    plt.xlabel('Time (s)')
    plt.ylabel('Servo Positions [0,1]')
    plt.legend()
    plt.show()

def plotXYPosition(dataTable):
    x = dataTable['x_in']
    y = dataTable['y_in']
    plt.clf()
    plt.title("Mecanum Navigation Position")
    plt.plot(x,y, 'r--.', label='position')
    plt.xlabel('X inches')
    plt.ylabel('Y inches')
    plt.legend()
    plt.show()
    
def plotPositionVsTime(dataTable):
    time = dataTable['time']
    x = dataTable['x_in']
    y = dataTable['y_in']
    theta_deg = [item*180/math.pi for item in dataTable['theta_rad']]
    fig, ax1 = plt.subplots()
    plt.title("Mecanum Navigation Position vs Time")
    ax1.plot(time, x, 'b:', label='X inches')
    ax1.plot(time, y, 'r:', label='Y inches')
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Distance (inches)', color='b')
    ax1.tick_params('y', colors='b')
    plt.legend()
    
    ax2 = ax1.twinx()
    ax2.plot(time, theta_deg, 'k:', label='Rotation degrees CCW')
    ax2.set_ylabel('Rotation degrees CCW', color='k')
    ax2.tick_params('y', colors='k')
    fig.tight_layout()
    #plt.legend()
    plt.show()

def plotMotorTickRateVsPower(dataTable):
    time = dataTable['time']
    motorTicks = dataTable['DRIVE_FRONT_LEFT_ticks']
    motorTickRate = diff(motorTicks,time)
    motorPower = dataTable['DRIVE_FRONT_LEFT_power']
    plt.clf()
    plt.title("Motor Ticks vs Power")
    plt.plot(motorPower[0:-1], motorTickRate, 'b.', label='position')
    plt.xlabel('Power')
    plt.ylabel('Tick Rate')
    plt.legend()
    plt.show()
    
def plotMotorData(dataTable, motorName):
    time = dataTable['time']
    motorPower = dataTable[motorName + '_power']
    motorTicks = dataTable[motorName + '_ticks']
    
    fig, ax1 = plt.subplots()    
    plt.title(motorName + " MOTOR")
    ax1.plot(time, motorPower, 'r.', label='power')
    ax1.set_xlabel('time (s)')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel('Motor Power', color='r')
    ax1.tick_params('y', colors='r')
    
    # Create twin axis
    ax2 = ax1.twinx()
    ax2.plot(time, motorTicks, 'b.', label='ticks')

    ax2.set_ylabel('Encoder Ticks', color='b')
    ax2.tick_params('y', colors='b')
    
    fig.tight_layout()
#    plt.legend()
    plt.show()
    
def plotSensorData(dataTable):
    time = dataTable['time']
    plt.clf()
    plt.title("Sensor Outputs")
    plt.plot(time,dataTable['light_level'], 'k-', label='light level')
    plt.plot(time,dataTable['red_channel'],'r-.', label='red level')
    plt.plot(time,dataTable['blue_channel'], 'b:', label='blue level')
    plt.xlabel('Time (s)')
    plt.ylabel('Sensor Data [0,1]')
    plt.legend()
    plt.show()

def plotControlerSticks(dataTable):
    time = dataTable['time']
    plt.clf()
    plt.title("Controller Stick Inputs")
    plt.plot(time,dataTable['left_stick_x'], 'k-', label='Left Stick X')
    plt.plot(time,dataTable['left_stick_y'],'r-.', label='Left Stick Y')
    plt.plot(time,dataTable['right_stick_x'], 'b:', label='Right Stick X')
    plt.plot(time,dataTable['right_stick_y'], 'g-.', label='Right Stick Y')
    plt.xlabel('Time (s)')
    plt.ylabel('Input Data [-1,1]')
    plt.legend()
    plt.show()
    
def plotControlerAnalogTriggers(dataTable):
    time = dataTable['time']
    plt.clf()
    plt.title("Controller Analog Trigger Inputs")
    plt.plot(time,dataTable['left_trigger'], 'r:', label='Left Trigger')
    plt.plot(time,dataTable['right_trigger'],'b-.', label='Right Trigger')
    plt.xlabel('Time (s)')
    plt.ylabel('Input Data [0,1]')
    plt.legend()
    plt.show()    
    
def plotControlerButtons(dataTable):
    time = dataTable['time']
    plt.clf()
    plt.title("Controller Button Inputs")
    plt.plot(time,dataTable['a_button'], 'g:', label='A button')
    plt.plot(time,dataTable['b_button'],'r:', label='B button')
    plt.plot(time,dataTable['x_button'],'b:', label='X button')    
    plt.plot(time,dataTable['y_button'],'y:', label='Y button')
    plt.plot(time,dataTable['left_bumper'],'c-.', label='Left Bumper')    
    plt.plot(time,dataTable['right_bumper'],'m--', label='Right Bumper')
    plt.plot(time,dataTable['left_stick_button'],'k:', label='Left Stick Button')    
    plt.plot(time,dataTable['right_stick_button'],'m:', label='Right Stick Button')
    plt.xlabel('Time (s)')
    plt.ylabel('Input Data [0,1]')
    plt.legend()
    plt.show()      

#%% Main routine, run if module is executed directly, rather than imported.

def main():
    dataTable = parseCSV.getDictionary('telemetry.csv')
    controllerDataTable = parseCSV.getDictionary('controls.csv')
    plt.close("all")
    
    plt.figure()
    plotServos(dataTable)
    plt.figure()
    plotXYPosition(dataTable)
    
    plotPositionVsTime(dataTable)
    plt.figure()
    plotSensorData(dataTable)
    
    # Display data for all motors
    driveMotors = ['DRIVE_FRONT_LEFT','DRIVE_FRONT_RIGHT',
                   'DRIVE_BACK_LEFT','DRIVE_BACK_RIGHT', 
                   'ARM_MOTOR']
    for i,motor in enumerate(driveMotors):
        plotMotorData(dataTable,motor)

    # Controller data plots
    plt.figure()
    plotControlerSticks(controllerDataTable)
    plt.figure()
    plotControlerAnalogTriggers(controllerDataTable)
    plt.figure()
    plotControlerButtons(controllerDataTable)    

if __name__ == '__main__':
    main()


