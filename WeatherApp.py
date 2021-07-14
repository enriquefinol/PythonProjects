from tkinter import *
#manage images
from PIL import ImageTk,Image
#how to connect to an IPA
import requests
import json


root = Tk()
root.title("Air Quality")
root.geometry("250x80")

#Create Lookup function
def zipLookup():
    global myLabel
    editor = Tk()
    editor.title("Air Quality")
    editor.geometry("400x50")

    #It is called by using a try/except block in order to prevent errors
    try:
        #Create a variable that holds the request
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=0FBD8FF5-E78B-42EB-8134-88E6088745A9")
        #decode the json code that was received
        api = json.loads(api_request.content)
        #Create variables that hold the different information needed
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        #Color are going to be assign as HEXADEX color
        #Color by right-clicked and 
        if category == "Good":
            weather_color = "#42f563"
        elif category == "Moderate":
            weather_color = "#f5f547"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#f2981b"
        elif category == "Unhealthy":
            weather_color = "#e30e0e"
        elif category == "Very Unhealthy":
            weather_color = "#e30ed5"
        elif category == "Hazardous":
            weather_color = "#8f063f"

        #Change the color of the whole window background
        editor.configure(background=weather_color)

        #The ipa returns the files in the form of lists with dictionaries
        #We can be specific about the information that is needed
        #Put the content to the screen
        #myLabel.grid_forget()
        myLabel = Label(editor,text=city + " Air Quality " + str(quality) + " " + category,font=("Helvetica",20),background=weather_color)
        myLabel.grid(row=0,column=0)

    except Exception as e:
        api = "Error..."

#create a label with friendly message
instruction_label = Label(root,text="Enter a valid zip code(United Sates):")
instruction_label.grid(row=0,column=0,columnspan=2)
#Create an entry box that will use the zipcode in order to search for a zone
zip = Entry(root)
zip.grid(row=1,column=1)

zipButton = Button(root, text = "Lookup Zipcode",command=zipLookup)
zipButton.grid(row=1,column=0,padx=10)

root.mainloop()