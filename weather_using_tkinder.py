"""
This Program help  to Get The current Weather In world Most Of The Cities.In this Program I used Openwhether API

"""


import requests
from tkinter import *
from functools import partial
from PIL import Image
from PIL import ImageTk


# This function helps to set the key and request the weather
def weather_call(city):
    key = "ca5618a5f93ea5f1ecf59df9e52f84ec"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city,key)
    par = {'units':'imperial'}
    response = requests.get(url,params=par)
    json_format = response.json()
    jsdict = dict(json_format)
    current_whether = json_format['weather'][0]['main']
    temp = json_format['main']['temp']
    wind_speed = jsdict['wind']['speed']
    return current_whether,temp,wind_speed
#this function helps to print the values in the frame lable
def weather_lable(city):
    city = city.get()
    #print(city)
    cur_whe,temp,win_sped = weather_call(city)
    try:
         main_lable = "City: {} \nCurrent Weather:{} \nTemperature(F'):{} \nWind Speed:{}".format(city,str(cur_whe),str(temp),str(win_sped))
         lable["text"] = main_lable    
    except:
         main_lable = "Sorry.The We can't Get That Data"
         lable["text"] = main_lable

tk = Tk()

#canvas used in here
canvas = Canvas(tk,height = 1000,width = 900)
canvas.pack()
#in here we use pillow module for open the image and set the image into background image
imgu =ImageTk.PhotoImage(Image.open('D:\weather.jpg'))
canvas.background = imgu
bg = canvas.create_image(0, 0, anchor="nw", image=imgu)
#this frame is the upprr frame it holds button and the entry
frame = Frame(tk,bg = "#00004d",bd = 5)
frame.place(rely = 0.1 ,relx = 0.1 ,relheight=0.07,relwidth=0.75 )
#this variable used to hold the entry value from the user
var = StringVar()
#this is in the upper frame it's used to take the value from the user
entry = Entry(frame,bg = "#b3b3ff",textvariable = var)
entry.place(rely = 0,relx = 0,relheight =1,relwidth = 0.75)
#in here we use funtool module bacause it has paritial function it hold function parameter 
fun_tool = partial(weather_lable,var)
button = Button(frame,bg = "#6666ff",text = "Check Weather",height =50,width = 15,command= fun_tool)
button.pack(side = "right")
#this is the lower frame it's used to  print the response value from the API
lower_frame = Frame(tk,bd =5,bg = "#00004d")
lower_frame.place(rely = 0.25,relx = 0.1,relheight = 0.75,relwidth = 0.75)
#it is a part of the lower frame
lower_framee = Frame(lower_frame,bd =5,bg = "#d9d9d9")
lower_framee.place(rely = 0.1,relx = 0.1,relheight = 0.85,relwidth = 0.85)
#it the frame we print the values
lable = Label(lower_framee)
lable.place(rely = 0.25,relx =0.25,relheight = 0.55,relwidth = 0.55)


# finally end the module
tk.mainloop()