'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''

#import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   1 : {'name' : 'Laptop', 'state' : "GPIO.LOW"},
   2 : {'name' : 'Music System', 'state' : "GPIO.LOW"},
   3 : {'name' : 'Printer', 'state' : "GPIO.LOW"},
   4 : {'name' : 'HF Rig', 'state' : "GPIO.LOW"},
   5 : {'name' : 'VHF Rig', 'state' : "GPIO.LOW"},
   6 : {'name' : 'Table Lamp', 'state' : "GPIO.LOW"},
   }

# Set each pin as an output and make it low:
#for pin in pins:
#   GPIO.setup(pin, GPIO.OUT)
#   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
#   for pin in pins:
#      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
       'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
