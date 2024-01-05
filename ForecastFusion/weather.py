from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from geopy.exc import GeocoderInsufficientPrivileges

root = Tk()
root.title("Forecast Fusion")
root.geometry("900x500+300+200") 
root.resizable(False, False)

def getWeather():
    city=textfield.get()

    

   
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

        else:
            messagebox.showwarning("Error", "Invalid city name. Please try again.")

    except GeocoderInsufficientPrivileges:
        messagebox.showerror("Error", "Geocoding service error: Insufficient privileges. Please check your API key.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)
w = Label(font=("arial", 15, 'bold'))
w.place(x=400, y=250)
h = Label(font=("arial", 15, 'bold'))
h.place(x=400, y=250)
d = Label(font=("arial", 15, 'bold'))
d.place(x=400, y=250)
p = Label(font=("arial", 15, 'bold'))
p.place(x=400, y=250)


def getWeather():
    city = textfield.get()

    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            # Call function to fetch weather data from OpenWeatherMap
            fetch_weather_data(city)

        else:
            messagebox.showwarning("Error", "Invalid city name. Please try again.")

    except GeocoderInsufficientPrivileges:
        messagebox.showerror("Error", "Geocoding service error: Insufficient privileges. Please check your API key.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def fetch_weather_data(city):
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=70ab0ada9130772e96d226fa001373ae"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.5)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # Update the labels with weather information
    t.config(text=f"{temp}°")
    c.config(text=f"{condition} | FEELS LIKE {temp}°")
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)



#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)


#Bottom box
Frame_image=PhotoImage(file="box.png")
Frame_myimage=Label(image=Frame_image)
Frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ff")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ff")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ff")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ff")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ff")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ff")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ff")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ff")
p.place(x=670,y=430)






root.mainloop()