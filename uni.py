from tkinter import *
import requests
import json
from datetime import datetime
from collections import OrderedDict
 
root =Tk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("University list")

country_value = StringVar()
 
def showUni():
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "c774716a7b3ab97e1151d8304e6b0bf9"  #sample API
 
    # Get city name from user from the input field (later in the code)
    country_name=country_value.get()
 
    # API url
    uni_url = 'http://universities.hipolabs.com/search?country=' + country_name
 
    # Get the response from fetched url
    response = requests.get(uni_url)
 
    # changing response from json to python readable 
    uni_info = str(response.json())
    print(uni_info)
    
    split= uni_info.split("name")
    split_name= dict(split)  
    split_name['name'] = sorted(uni_info['domain'], key=lambda x : x['name'], reverse=True)
    print(split_name)
    tfield.insert(INSERT, split_name)   #to insert or send value in our Text Field to display output
 
 
 
#------------------------------Frontend part of code - Interface
 
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = country_value,  width = 24, font='Arial 14 bold').pack()

 
Button(root, command = showUni, text = "Check University", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 

 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()