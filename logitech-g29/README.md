# logitech g29
Code documenting how to leverage the [Logitech G29 racing wheel](https://www.logitechg.com/en-us/products/driving/driving-force-racing-wheel.html) in JS and Python. 

## js 
Use the [Gamepad API](https://www.w3.org/TR/gamepad/) to access data and events. [This project](https://github.com/luser/gamepadtest) includes a web page that will show all available events and data from connected gamepads.

### simpleDrivingTest.html
Demonstrates how to control a simple rectangle using the wheel, gas, and brake data from the Logitech G29.

## Python and PsychoPy
Use the the [PsychoPy](https://www.psychopy.org/documentation.html) [Joystick](https://psychopy.org/api/hardware/joystick.html) library to access data and events.

### simpleDrivingTest.py
The same app as above implemented using Psychopy Joystick library.
