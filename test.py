# importing libraries
import tkinter as tk
from tkinter import Message, Text
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from pathlib import Path

window = tk.Tk()
window.title("Face_Recogniser")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(
    window, text="Face-Recognition-System",
    bg="green", fg="white", width=50,
    height=3, font=('times', 30, 'bold'))

message.place(x=200, y=20)


# The function below is used for checking
# whether the text below is number or not ?
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# Take Images is a function used for creating
# the sample of the images which is used for
# training the model. It takes 60 Images of
# every new user.
def encodImg():
    # Both ID and Name is used for recognising the Image
    Id = (txt.get())
    name = (txt2.get())

    # Checking if the ID is numeric and name is Alphabetical
    if (is_number(Id) and name.isalpha()):
        # Opening the primary camera if you want to access
        # the secondary camera you can mention the number
        # as 1 inside the parenthesis
        cam = cv2.VideoCapture(0)
        # Specifying the path to haarcascade file
        harcascadePath = "data\haarcascade_frontalface_default.xml"
        # Creating the classier based on the haarcascade file.
        detector = cv2.CascadeClassifier(harcascadePath)
        # Initializing the sample number(No. of images) as 0
        sampleNum = 0
        while (True):
            # Reading the video captures by camera frame by frame
            ret, img = cam.read()
            # Converting the image into grayscale as most of
            # the the processing is done in gray scale format
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # It converts the images in different sizes
            # (decreases by 1.3 times) and 5 specifies the
            # number of times scaling happens
            faces = detector.detectMultiScale(gray, 1.3, 5)

            # For creating a rectangle around the image
            for (x, y, w, h) in faces:
                # Specifying the coordinates of the image as well
                # as color and thickness of the rectangle.
                # incrementing sample number for each image
                cv2.rectangle(img, (x, y), (
                    x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder
                # TrainingImage as the image needs to be trained
                # are saved in this folder
                cv2.imwrite(
                    "TrainingImage\ " + name + "." + Id + '.' + str(
                        sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame that has been captured
                # and drawn rectangle around it.
                cv2.imshow('frame', img)
            # wait for 100 milliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 60
            elif sampleNum > 60:
                break
        # releasing the resources
        cam.release()
        # closing all the windows
        cv2.destroyAllWindows()
        # Displaying message for the user
        res = "Images Saved for ID : " + Id + " Name : " + name

        csvFile.close()
        message.configure(text=res)
    else:
        if (is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text=res)
        if (name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text=res)



# For testing phase
def testImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Reading the trained model
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "data\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    # # getting the name from "userdetails.csv"
    # df = pd.read_csv("UserDetails\UserDetails.csv")
    # cam = cv2.VideoCapture(0)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # while True:
    #     ret, im = cam.read()
    #     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #     faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
    #         Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
    #         if (conf < 50):
    #             aa = df.loc[df['Id'] == Id]['Name'].values
    #             tt = str(Id) + "-" + aa
    #         else:
    #             Id = 'Unknown'
    #             tt = str(Id)
    #         if (conf > 75):
    #             noOfFile = len(os.listdir("ImagesUnknown")) + 1
    #             cv2.imwrite("ImagesUnknown\Image" +
    #                         str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
    #         cv2.putText(im, str(tt), (x, y + h),
    #                     font, 1, (255, 255, 255), 2)
    #     cv2.imshow('im', im)
    #     if (cv2.waitKey(1) == ord('q')):
    #         break
    cam.release()
    cv2.destroyAllWindows()

trainImg = tk.Button(window, text="encoding",
                     command=encodImg, fg="white", bg="green",
                     width=20, height=3, activebackground="Red",
                     font=('times', 15, ' bold '))
trainImg.place(x=200, y=500)
testImg = tk.Button(window, text="Testing",
                     command=testImages, fg="white", bg="green",
                     width=20, height=3, activebackground="Red",
                     font=('times', 15, ' bold '))
testImg.place(x=650, y=500)
quitWindow = tk.Button(window, text="Quit",
                       command=window.destroy, fg="white", bg="green",
                       width=20, height=3, activebackground="Red",
                       font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)

window.mainloop()