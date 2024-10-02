import json  # Import the JSON module for handling JSON data
import urllib.request  # Import urllib for making HTTP requests
import webbrowser  # Import webbrowser to open files in a web browser
import geocoder  # Import geocoder for getting geographical coordinates based on IP address
import turtle  # Import turtle for graphical representation
from PIL import Image  # Import the pillow library to handle image resizing

# URL for the Open Notify API to get information about astronauts on the ISS
url = "http://api.open-notify.org/astros.json"

# Make a request to the API and read the response
response = urllib.request.urlopen(url)

# Load the JSON data from the response
result = json.loads(response.read())

# Open a text file to write the ISS information
with open("iss.txt", "w") as file:
    # Write the number of astronauts currently on the ISS
    file.write(f"There are currently {str(result['number'])} astronauts on the ISS: \n\n")
    
    # Get the list of people on board the ISS
    people = result["people"]
    
    # Write the names of astronauts currently on the ISS
    for person in people:
        file.write(f"{person['name']} - on board \n")
    
    # Get the current geographical location (latitude and longitude) of the user's IP address
    g = geocoder.ip('me')
    # Write the user's location to the file
    file.write(f"\n Your current lat / long is: {str(g.latlng)}")

# Open the text file in the default web browser
webbrowser.open("iss.txt")

# Resize the ISS gif before loading it in turtle
img = Image.open("images/iss.gif")
img_resized = img.resize((50, 50))
img_resized.save("images/iss_resized.gif")

# Setup the world map in turtle module
screen = turtle.Screen()
# Set screen size
screen.setup(1280, 720)

# Load the world map image
screen.bgpic("images/map.gif")
# Register the ISS image and create a turtle object for the ISS
screen.register_shape("images/iss_resized.gif")
# Create a new turtle object, which will represent the ISS on the map
iss = turtle.Turtle()
# Set the shape of the turtle object to the ISS image
iss.shape("images/iss_resized.gif")
# Rotate the ISS turtle object to face 45 degrees (northeast direction)
iss.setheading(45)
# Lift the pen so the turtle moves without drawing a line on the map
iss.penup()

# Keep the window open
turtle.mainloop()
