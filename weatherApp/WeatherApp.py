import tkinter as tk
from tkinter import font 
import requests 

HEIGHT = 500 
WIDTH = 600 

def test_function(entry):
    print("This is the entry: ", entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature(°F): %s' %(name,desc,temp)
    except:
        final_str = 'Error: Wrong Info'
    return final_str

def get_weather(city):
    weather_key = 'c2eb43959d1d0f996be6a7a5c61bee29'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params) 
    weather = response.json() 

    label['text'] = format_response(weather)

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

root = tk.Tk() # Everything in this application between this and root

# weather api key: c8b0b95d87994fc906cab30ccd430fed
# api call: api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg = '#80c1ff', bd = 5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame, font =('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text ="Get Weather", font =('Courier', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight =1)

lower_frame = tk.Frame(root,bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely =0.25, relwidth =0.75, relheight=0.6, anchor ='n')

label = tk.Label(lower_frame, font =('Courier', 20))
label.place(relwidth=1, relheight=1)

root.mainloop() # everything in this application between this and root