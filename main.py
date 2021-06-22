from ursina import *
from visCube import *
from visHints import *
import random

anim = False  # used to lockout inputs during animation
blinking = False
# drag = False  # used to rotate cube with mouse
reading = False # used to lockout inputs during reading strings
settings = False #checks if settings menu is open
hints = False #checks if hints menu is open
readSequence = Sequence() #used for sequence of moves
mousepos = []  # stores mouse position for rotating camera
app = Ursina()
# window settings
window.borderless = False
# window.fps_counter.enabled = False
window.exit_button.visible = False
window.color = color.dark_gray


# initializing entities
cube = VisCube()  # rubiks cube
hintCube = VisHints()  # hints
center = Entity()  # center transform, used for rotation


def main():
    # setting camera, lighting, and scene
    camera.setPos(8, 8, -25)
    camera.lookAt(cube)
    light = DirectionalLight(x=3, y=20, z=-10)
    light.lookAt(cube)  # making sure the cube is always well lit
    window.icon_filename = 'icon'  # not working yet :(
    window.title = 'QB'
    hintCube.reparent_to(cube)  # making the hints stay attached to cube
    app.run()  # opens window



def input(key):
    # uedlmrfsb
    global anim
    global reading
    global drag
    global mousepos
    if not anim and not reading and not inputList.enabled:  # if not already animated, read keys and animate
        if key == 'm':  # this one is for hints, and requires a longer delay
            anim = True
            hintCube.rotateF()
            invoke(endAnim, delay=.6)

        if key == 'q':
            anim = True
            cube.rotateU()
            invoke(endAnim, delay=.55)

        if key == 'w':
            anim = True
            cube.rotateUU()
            invoke(endAnim, delay=.55)

        if key == 'a':
            anim = True
            cube.rotateE()
            invoke(endAnim, delay=.55)

        if key == 's':
            anim = True
            cube.rotateEE()
            invoke(endAnim, delay=.55)

        if key == 'z':
            anim = True
            cube.rotateD()
            invoke(endAnim, delay=.55)

        if key == 'x':
            anim = True
            cube.rotateDD()
            invoke(endAnim, delay=.55)

        if key == 'e':
            anim = True
            cube.rotateL()
            invoke(endAnim, delay=.55)

        if key == 'r':
            anim = True
            cube.rotateLL()
            invoke(endAnim, delay=.55)

        if key == 'd':
            anim = True
            cube.rotateM()
            invoke(endAnim, delay=.55)

        if key == 'f':
            anim = True
            cube.rotateMM()
            invoke(endAnim, delay=.55)

        if key == 'c':
            anim = True
            cube.rotateR()
            invoke(endAnim, delay=.55)

        if key == 'v':
            anim = True
            cube.rotateRR()
            invoke(endAnim, delay=.55)

        if key == 't':
            anim = True
            cube.rotateF()
            invoke(endAnim, delay=.55)

        if key == 'y':
            anim = True
            cube.rotateFF()
            invoke(endAnim, delay=.55)

        if key == 'g':
            anim = True
            cube.rotateS()
            invoke(endAnim, delay=.55)

        if key == 'h':
            anim = True
            cube.rotateSS()
            invoke(endAnim, delay=.55)

        if key == 'b':
            anim = True
            cube.rotateB()
            invoke(endAnim, delay=.55)

        if key == 'n':
            anim = True
            cube.rotateBB()
            invoke(endAnim, delay=.55)
    #these are used for camera movement, to be deleted in final version
    # if key == 'left mouse down':
    #    drag = True
    #    mousepos = mouse.position

   # if key == 'left mouse up':
     #   drag = False

    if inputList.enabled and not cube.anim:#inputs string from ui textbox as a list off moves
        if key == 'enter':
            readString(inputList.text)





def update():  # called every frame
    global mousepos
    global center
    global anim
    global reading
    # camera movements, to be deleted in final build
    # if drag:
    #    cube.reparent_to(center)
    #    center.rotation_y += 100 * (mousepos[0] - mouse.position[0])
    #    center.rotation_x += 100 * (mouse.position[1] - mousepos[1])
    #    cube.reparent_to(scene)
    #    center.rotation = (0, 0, 0)
    # mousepos = mouse.position


def endAnim():  # resets anim to false, needs to be a function to be used with invoke() and delay
    global anim
    anim = False


# =====================================================ui buttons=====================================================
def rotateR(): #rotates right
    global anim
    global reading
    if not anim and not reading:
        cube.emptyArrowFunc()
        cube.rotateX()
        anim = True
        invoke(endAnim, delay=speedSlider.value + .15)


def rotateL(): #rotates left
    global anim
    global reading
    if not anim and not reading:
        cube.emptyArrowFunc()
        anim = True
        cube.rotateXX()
        invoke(endAnim, delay=speedSlider.value + .15)


def rotateU(): #rotates upward
    global anim
    global reading
    if not anim and not reading:
        cube.emptyArrowFunc()
        anim = True
        cube.rotateY()
        invoke(endAnim, delay=speedSlider.value + .15)


def rotateD(): #rotates downward
    global anim
    global reading
    if not anim and not reading:
        cube.emptyArrowFunc()
        anim = True
        cube.rotateYY()
        invoke(endAnim, delay=speedSlider.value + .15)

def rotateZL(): #rotates left on z axis
    global anim
    global reading
    if not anim and not reading:
        cube.emptyArrowFunc()
        cube.rotateZ()
        anim = True
        invoke(endAnim, delay=speedSlider.value + .15)

def rotateZR(): #rotates right on z axis
    global anim
    global reading
    if not anim and not reading:
        cube.emptyArrowFunc()
        cube.rotateZZ()
        anim = True
        invoke(endAnim, delay=speedSlider.value + .15)


def resetCube():  # resets cube
    global cube
    global anim
    global readSequence
    global reading
    reading = False
    readSequence.paused = True
    readSequence.kill()
    cube.delete()
    cube.rotation = (0, 0, 0)
    cube = VisCube()
    anim = True
    invoke(endAnim, delay=.65)
    changeTurnSpeed()


def openSettings(): #open settings menu
    global settings
    if not settings:
        resetButton.enabled = True
        rotateRButton.enabled = True
        rotateLButton.enabled = True
        rotateUButton.enabled = True
        rotateDButton.enabled = True
        background.enabled = True
        inputButton.enabled = True
        scrambleButton.enabled = True
        rotateZRButton.enabled = True
        rotateZLButton.enabled = True
        speedSlider.enabled = True
        settings = True
    else:
        resetButton.enabled = False
        rotateRButton.enabled = False
        rotateLButton.enabled = False
        rotateUButton.enabled = False
        rotateDButton.enabled = False
        background.enabled = False
        inputButton.enabled = False
        scrambleButton.enabled = False
        rotateZRButton.enabled = False
        rotateZLButton.enabled = False
        speedSlider.enabled = False
        settings = False

def openHints(): #open hints menu
    global hints
    global blinking
    if not hints:
        hintDisplay.enabled = True
        hints = True
    else:
        hintDisplay.enabled = False
        hints = False

    if blinking:
        blinking = False
        cube.unblink()



def readString(rotations, scrambling = False):  # goes through string and does each move
    global reading
    global readSequence
    if not reading:
        cube.disableArrows()
        cube.setTurnSpeed(.1)
        stepTime = .3  # time between moves in sequence 65
        reading = True
        toggleInput()
        rotations = rotations.upper()
        rotations += '0'
        readSequence = Sequence()
        for i in range(len(rotations)):
            if rotations[i] == '0':
                readSequence.append(stepTime)
                readSequence.append(Func(resetReading))
                if not scrambling:
                    readSequence.append(Func(toggleInput))
                readSequence.append(Func(cube.reenableArrows))
                readSequence.append(Func(changeTurnSpeed))
                readSequence.start()
                return
            elif rotations[i] == 'U':
                if rotations[ i +1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateUU))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateU))
            elif rotations[i] == 'E':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateEE))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateE))
            elif rotations[i] == 'D':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateDD))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateD))
            elif rotations[i] == 'L':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateLL))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateL))
            elif rotations[i] == 'M':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateMM))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateM))
            elif rotations[i] == 'R':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateRR))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateR))
            elif rotations[i] == 'F':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateFF))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateF))
            elif rotations[i] == 'S':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateSS))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateS))
            elif rotations[i] == 'B':
                if rotations[i + 1] == "'":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateBB))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateB))


def resetReading():  # helps make sure no moves are made while reading a list of moves
    global reading
    reading = False

def toggleInput():  # toggles the text input on or off
    if inputList.enabled:
        inputList.enabled = False
    elif not reading:
        inputList.enabled = True

def scramble():  # creates a random string of moves
    moves = ["u" ,"e" ,"d" ,"l" ,"m" ,"r" ,"f" ,"s" ,"b" ,"u'" ,"e'" ,"d'" ,"l'" ,"m'" ,"r'" ,"f'" ,"s'" ,"b'" ,"uu"
             ,"ee" ,"dd" ,"ll" ,"mm" ,"rr" ,"ff" ,"ss" ,"bb"]
    scrambled_moves = "".join(random.choices(moves, k=25))
    readString(scrambled_moves, True)

def hintMove():
    global blinking
    if blinking:
        blinking = False
        cube.unblink()
    else:
        blinking = True
        cube.blink()

def hintDetailToggle():
    if hintDetail.enabled:
        hintDetail.enabled = False
    else:
        hintDetail.enabled = True

def changeTurnSpeed():
    global reading
    if not reading:
        cube.setTurnSpeed(speedSlider.value)
# =============================================================UI buttons======================================================================
# settings==============
settingsButton = Button(text='', icon='gear', color=color.gray, scale=.075, position=(-.81, .43, 0),
                        on_click=Func(openSettings))
background = Button(text='', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(-.75, 0.06, 1), scale=(.25, .63), collider='', enabled=False)
resetButton = Button(text='Reset', color=color.red, scale=.1, position=(-.81, -.18, 0), on_click=Func(resetCube),
                     enabled=False)
rotateRButton = Button(text='', icon='rotateR', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.69, .18, 0),
                       on_click=Func(rotateR), enabled=False)
rotateLButton = Button(text='', icon='rotateL', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.81, .18, 0),
                       on_click=Func(rotateL), enabled=False)
rotateUButton = Button(text='', icon='rotateU', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.81, .3, 0),
                       on_click=Func(rotateU), enabled=False)
rotateDButton = Button(text='', icon='rotateD', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.69, .3, 0),
                       on_click=Func(rotateD), enabled=False)
rotateZRButton = Button(text='', icon='rotateZR', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.69, .06, 0),
                       on_click=Func(rotateZR), enabled=False)
rotateZLButton = Button(text='', icon='rotateZL', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.81, .06, 0),
                       on_click=Func(rotateZL), enabled=False)
inputButton = Button(text='Input', color=color.red, scale=.1, position=(-.69, -.06, 0), on_click=Func(toggleInput),
                     enabled=False)
inputList = TextField(max_lines=1, position=(-.75 ,-.3 ,0), enabled=False)
scrambleButton = Button(text='Scramble', color=color.red, scale=.1, position=(-.81, -.06, 0), on_click=Func(scramble),
                     enabled=False)
speedSlider = Slider(min=1, max=.1, default=.5, text='Turn Speed', height=.1, on_value_changed=Func(changeTurnSpeed), position=(-.742, -.20, 0), scale=.2, enabled=False)
speedSlider.label.origin = (0,0)
speedSlider.label.position = (.25,.25)
speedSlider.label.scale = 4.5
speedSlider.knob.text_color = color.clear
# hints============
hintButton = Button(text='', icon='hintButton', color=color.gray, scale=.075, position=(-.81, -.43, 0), on_click=Func(openHints))
hintDisplay = Button(text='', icon='hint1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(.6, .35, 1), scale=(.5, .25), collider='', enabled=False)
hintMoveButton = Button(text='Show Move', icon='', color=color.dark_gray, scale=(.3,.15), position=(-.3, -.375, -1), parent=hintDisplay, on_click=Func(hintMove))
hintDetailButton = Button(text='Details', icon='', color=color.dark_gray, scale=(.2,.15), position=(-.0, -.375, -1), parent=hintDisplay, on_click=Func(hintDetailToggle))
hintDetail = Button(text='', icon='HintDetail1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(-0, -1.85, 1), scale=(1.1, 2.64), collider='', parent = hintDisplay, enabled=False)




if __name__ == '__main__':
    main()
