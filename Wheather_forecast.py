import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from datetime import datetime
from tkinter import Label
from PIL import Image, ImageTk

def getweather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=fcf96aca82a012422e03af684a9aca5b"
    api_link=requests.get(complete_api_link)
    # converting the data into json file
    api_data=api_link.json()
    #print(api_data)

    if api_data['cod']=='404':
       print("Invalid City: {}, please check you city name".format(city))
    else:
      temp_city=((api_data['main']['temp'])-273.15)
      weather_desp=api_data['weather'][0]['description']
      hmdt=api_data['main']['humidity']
      wind_spd=api_data['wind']['speed']
      date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
      print("-----------------------------------------------------")
    
    
      
      

root=tk.Tk()
root.title("Wheather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
# Open the image file
image_path1 = "C:/Users/hp/Downloads/Copy of search.png"
search_image = Image.open(image_path1)

# Convert the image to a Tkinter-compatible format
tk_image1 = ImageTk.PhotoImage(search_image)


# Create a label with the image
my_image1 = Label(root, image=tk_image1, bg="#404040", borderwidth=0)
my_image1.image = tk_image1  # This line is necessary to prevent garbage 
my_image1.place(x=20, y=20)


textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",fg="white")
textfield.place(x=50,y=40)
textfield.focus()

image_path2 = "C:/Users/hp/Downloads/Copy of search_icon.png"
search_icon = Image.open(image_path2)
tk_image2 = ImageTk.PhotoImage(search_icon)
my_image2 = tk.Button(root, image=tk_image2, bg="#404040", borderwidth=0,cursor="hand2", command=getweather)
my_image2.image = tk_image2  # This line is necessary to prevent garbage collection
my_image2.place(x=400,y=34)

#logo
image_path3 = "C:/Users/hp/Downloads/Copy of logo.png"
logo_icon = Image.open(image_path3)
tk_image3 = ImageTk.PhotoImage(logo_icon)
my_image3 = Label(root, image=tk_image3)
my_image3.image = tk_image3  # This line is necessary to prevent garbage collection
my_image3.place(x=150,y=100)

#bottom box
image_path4 = "C:/Users/hp/Downloads/Copy of box.png"
Frame_image=Image.open(image_path4)
tk_image4 = ImageTk.PhotoImage(Frame_image)
my_image4 = Label(root, image=tk_image4)
my_image4.image = tk_image4  # This line is necessary to prevent garbage collection
my_image4.pack(padx=5,pady=5,side="bottom")

#time
name=Label(root,font=("arial",15,"bold")) 
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label1.place(x=120,y=400)
label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label2.place(x=300,y=400)
label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label3.place(x=480,y=400)
label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label4.place(x=670,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=300,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=480,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()
'''location = input("Enter the city name:- ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=fcf96aca82a012422e03af684a9aca5b"
api_link=requests.get(complete_api_link)
# converting the data into json file
api_data=api_link.json()
#print(api_data)

if api_data['cod']=='404':
    print("Invalid City: {}, please check you city name".format(location))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desp=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-----------------------------------------------------")
    print("Wheather Stats for- {}".format(location.upper(),date_time))
    print("------------------------------------------------------")
    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current wheather discription  :",weather_desp)
    print("Current Humidity  :",hmdt,'%')
    print("Current wind speed  :",wind_spd,'kmph')'''

