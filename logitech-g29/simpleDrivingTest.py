from psychopy.hardware import joystick
from psychopy import visual, core, event 

winWidth = 800
winHeight = 800
wheelMultiplier = 5
wheelSpeedDampener = 2
prevSpeedRegulator = 100
carHeight = 40
carWidth = 20
carX = 0
carY = 0
prevSpeed = 0
speed = 0
wheel = 0

# Init
joystick.backend='pyglet' 
win = visual.Window(size=[winWidth,winHeight], color=1, winType='pyglet')

carX = -(carWidth/2);
carY = -(carHeight/2)

nGamepads = joystick.getNumJoysticks()  
gamepad = None
if (nGamepads > 0):
    gamepad = joystick.Joystick(0)  
else:
    print("No controller found")
    quit()

while True:  
    if len(event.getKeys())>0:
        break
    event.clearEvents()
    
    # All wheel data is mapped to gamepad.axes[0]. 
    wheel = -1*wheelMultiplier*gamepad.getAxis(0);
    prevSpeed = speed;
    # All gas AND brake data is mapped to gamepad.axes[1]. This data is signed.
    gamepadSpeed = gamepad.getAxis(1);
    if (abs(gamepadSpeed) < .01):
        gamepadSpeed = 0
    else:
        gamepadSpeed = -1*gamepadSpeed
    speed = ((prevSpeedRegulator-1)*prevSpeed + 15*gamepadSpeed) / prevSpeedRegulator;
    #print(gamepadSpeed,abs(speed))
    #if (abs(speed) < .12):
    #    speed = 0
    if (speed < 0):
        speed = 0

    if (speed != 0):
        carX -= (speed*wheel)/wheelSpeedDampener
    carY += speed;

    if ((carX+carWidth) < -winWidth/2):
        carX = winWidth/2
    if (carX > winWidth/2):
        carX = -winWidth/2

    if ((carY-carHeight) > winHeight/2):
        carY = -winHeight/2;
    if (carY < -winHeight/2):
        carY = winHeight/2

    rect = visual.Rect(
        win=win,
        units="pix",
        width=carWidth,
        height=carHeight,
        pos=[carX,carY],
        fillColor=[-1, -1, 1]
    )

    rect.draw()
    win.flip() 

     