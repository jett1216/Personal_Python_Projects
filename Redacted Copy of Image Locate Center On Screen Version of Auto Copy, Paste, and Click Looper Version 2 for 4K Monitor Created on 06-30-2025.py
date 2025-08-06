#This code shows the general format of the original script. However, paths and names have been changed to protect the IP and client that commissioned this work.

#Ensure that database webpage is ready and notepad is already open before starting this script!!!!


#Import all necessary libraries and tools
import os
import pyautogui
import time
import pyperclip
import pynput
import keyboard
import cv2 
import PIL
import pyscreeze 
import numpy as np


#Pause
time.sleep(5.0)


#Keyboard reset and pause
pyautogui.keyUp('ctrl')
time.sleep(1.0)


#Open and Copy All Contents From Notepad Containing Update Status Statement
def copy_text_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            text = file.read()
        pyperclip.copy(text)
        print(f"Text from '{filepath}' copied to clipboard successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Update Note.txt" 
    copy_text_from_file(file_path)


#Keyboard reset and pause
pyautogui.keyUp('ctrl')
time.sleep(1.0)

#Click on Chrome
location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Chrome.png", grayscale=True, confidence=0.95)
time.sleep(1.0)
pyautogui.click(location)
time.sleep(1.0)

#Keyboard reset and pause
pyautogui.keyUp('ctrl')
time.sleep(1.0)


#Main Data Entry Loop (Each section contains a reset and pause at the end for safety measures)
try:
    while True:

        #New Chart Click
        pyautogui.keyUp('ctrl')
        time.sleep(1.0)
        pyautogui.moveTo(1313, 535)
        time.sleep(3.5)
        pyautogui.click()
        time.sleep(10.0)
        
        #Update Status Field
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Update_Status.png",  grayscale=True, confidence=0.50, region=(3220, 586, 600, 240))
        time.sleep(0.5)
        pyautogui.click(location)
        time.sleep(0.5)
    
        #Select All after clicking inside Update Status Field
        pyautogui.keyDown('ctrl')
        time.sleep(0.5)
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)


        #Paste Previously Copied Update Status into Update Status Field
        pyautogui.keyDown('ctrl')
        time.sleep(0.5)
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)


        #Diagnostic Field
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Diagnostic.png", grayscale=True, confidence=0.50, region=(3217, 1015, 230, 55))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(1.0)


        #Other Field 1 
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_1.png", grayscale=True, confidence=0.50, region=(3513, 1090, 135, 40))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(1.0)



        #Other Field 2
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_2.png", grayscale=True, confidence=0.50, region=(3725, 1989, 80, 50))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        #Other Field 3
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_3.png", grayscale=True, confidence=0.50, region=(3725, 1759, 80, 50))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        

        #Click scroll bar once to ensure auto snap to bottom-most location
        pyautogui.moveTo (3827, 2053)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.75)


        #Other Field 4
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_4.png", grayscale=True, confidence=0.50, region=(3725, 1529, 80, 50))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        #Other Field 5
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_5.png", grayscale=True, confidence=0.50, region=(3725, 1459, 80, 50))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        #Other Field 6
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_6.png", grayscale=True, confidence=0.50, region=(3725, 1392, 80, 50))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        #Other Field 7
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Other_Field_7.png", grayscale=True, confidence=0.50, region=(3725, 1325, 80, 50))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        #Other Field 8
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\ther_Field_8.png", grayscale=True, confidence=0.50, region=(3725, 1255, 80, 60))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(0.5)


        #Click scroll bar twice to ensure auto snap to bottom-most location
        
        #First click
        pyautogui.moveTo(3827, 2040)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)

        #Second click
        pyautogui.moveTo(3827, 2040)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(2.0)


        #Finalize
        location = pyautogui.locateCenterOnScreen(r"C:\Users\neoka\OneDrive\Desktop\Auto Clicker Locate On Screen Variant 06-06-2025\Finalize.png", grayscale=True, confidence=0.50, region=(3582, 2008, 185, 70))
        time.sleep(1.0)
        pyautogui.click(location)
        time.sleep(3.5)
        

        #Move back and reset to new entry record location
        pyautogui.keyUp('ctrl')
        time.sleep(1.0)
        pyautogui.moveTo(1313, 535)
        time.sleep(1.0)

        #Manual Script Interrupt by pressing the letter 'q'
        if keyboard.is_pressed('q'):
            break  
#If Image is Not Found
except pyautogui.ImageNotFoundException:
       print("Image not found.")


