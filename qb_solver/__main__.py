from ursina import *
from qb_solver.visCube import *
from qb_solver.visHints import *
from qb_solver.cubesolver import *
import random
from rubik.cube import Cube
import os

application.asset_folder=Path(os.path.join(application.package_folder.parent), 'qb_solver/')

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
window.fps_counter.enabled = False
window.exit_button.visible = False
window.color = color.dark_gray

window.fullscreen = True
window.aspect_ratio = 2

# initializing entities
cube = VisCube()  # rubiks cube
hintCube = VisHints()  # hints
center = Entity()  # center transform, used for rotation
current_piece = None


def menu():
    cube_menu_model.enabled = True
    title.enabled = True
    help_menu.enabled = True
    settings_menu.enabled = True
    start_menu.enabled = True
    exit.enabled = True
    hintButton.enabled = False
    settingsButton.enabled = False
    cube.enabled = False
    main_menu_button.enabled = False
    
    hintDisplay.enabled = False
    hintDetail.enabled = False
    hintSpecific.enabled = False
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
    notationButton.enabled = False
    settings = False
    settingsButton.color = color.gray
    hintButton.color = color.gray

def start():
    cube_menu_model.enabled = False
    title.enabled = False
    help_menu.enabled = False
    settings_menu.enabled = False
    exit.enabled = False
    start_menu.enabled = False
    hintButton.enabled = True
    settingsButton.enabled = True
    cube.enabled = True
    main_menu_button.enabled = True
    notationButton.enabled = True

def darkLight():
    if window.color == color.dark_gray:
        window.color = color.light_gray
    elif window.color == color.light_gray:
        window.color = color.dark_gray




def main():
    menu()
    # setting camera, lighting, and scene
    camera.setPos(16, 8, -25)
    camera.lookAt(cube)
    light = DirectionalLight(x=3, y=20, z=-10)
    light.lookAt(cube)  # making sure the cube is always well lit
    window.icon_filename = 'icon'  # not working yet :(
    window.title = 'QB'
    hintCube.reparent_to(cube)  # making the hints stay attached to cube
    app.run()  # opens window



def input(key):
    global anim
    global reading
    global drag
    global mousepos
    if not anim and not reading and not inputList.enabled:  # if not already animated, read keys and animate
        if key == 'm':  # this one is for hints, and requires a longer delay
            #anim = True
            #hintCube.rotateF()
            #invoke(endAnim, delay=.6)
            cube.print()
            #updateCurrentHint('Move the %s %s piece above its center\n test', 'flip-2', None)
    if inputList.enabled and not cube.anim:#inputs string from ui textbox as a list off moves
        if key == 'enter':
            readString(inputList.text)

    if key == 'left mouse down':
        invoke(checkCurrentHint, delay=cube.turnSpeed+.25)





def update():  # called every frame
    global mousepos
    global center
    global anim
    global reading
    # makes the main menu cube rotate
    if cube_menu_model.enabled:
        cube_menu_model.rotation_y += time.dt * 100






def endAnim():  # resets anim to false, needs to be a function to be used with invoke() and delay
    global anim
    anim = False


# =====================================================ui buttons=====================================================

def checkCurrentHint():
    updateCurrentHint(*hint(cube.virtualCube, current_piece))

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
        cube.rotateXi()
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
        cube.rotateYi()
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
        cube.rotateZi()
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

    cube.virtualCube = Cube("RRRRRRRRRBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYOOOOOOOOO") # Resets virtual cube


def openSettings(): #open settings menu
    global settings
    if not settings:
        settingsButton.color = color.light_gray
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
        settingsButton.color = color.gray
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
        hintButton.color = color.light_gray
        hintDisplay.enabled = True
        hints = True
    else:
        hintButton.color = color.gray
        hintDisplay.enabled = False
        hints = False
        hintSpecific.enabled = False

    if blinking:
        blinking = False
        cube.unblink()


def readString(rotations, scrambling = False):  # goes through string and does each move
    global reading
    global readSequence
    if not reading:
        cube.disableArrows()
        cube.setTurnSpeed(.1)
        stepTime = .3  # time between moves in sequence must be at least .2 higher than turn speed
        reading = True
        toggleInput()
        rotations += '0'
        readSequence = Sequence()
        readSequence.time_step = time.dt
        for i in range(len(rotations)):
            if rotations[i] == '0':
                readSequence.append(stepTime)
                readSequence.append(Func(resetReading))
                if not scrambling:
                    readSequence.append(Func(toggleInput))
                readSequence.append(Func(cube.reenableArrows))
                readSequence.append(Func(changeTurnSpeed))
                readSequence.append(Func(checkCurrentHint))
                readSequence.start()
                return
            elif rotations[i].upper() == 'U':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateUi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateU))
            elif rotations[i].upper() == 'E':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateEi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateE))
            elif rotations[i].upper() == 'D':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateDi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateD))
            elif rotations[i].upper() == 'L':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateLi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateL))
            elif rotations[i].upper() == 'M':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateMi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateM))
            elif rotations[i].upper() == 'R':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateRi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateR))
            elif rotations[i].upper() == 'F':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateFi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateF))
            elif rotations[i].upper() == 'S':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateSi))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateS))
            elif rotations[i].upper() == 'B':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateBi))
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
    moves = ["U" ,"E" ,"D" ,"L" ,"M" ,"R" ,"F" ,"S" ,"B" ,"Ui" ,"Ei" ,"Di" ,"Li" ,"Mi" ,"Ri" ,"Fi" ,"Si" ,"Bi"]
    scrambled_moves = " ".join(random.choices(moves, k=10))
    readString(scrambled_moves, True)
    #print(cube.virtualCube)

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

    if hintSpecific.enabled:
        hintMove()
        hintSpecific.enabled = False

def hintSpecificToggle():
    hintMove()
    if hintSpecific.enabled:
        hintSpecific.enabled = False
    else:
        hintSpecific.enabled = True

    if hintDetail.enabled:
        hintDetail.enabled = False

def changeTurnSpeed():
    global reading
    if not reading:
        cube.setTurnSpeed(speedSlider.value)

def updateCurrentHint(hintText, hintPicture, next_piece):
    global current_piece
    if hintText != None:
        hintSpecific.icon = hintPicture
    if hintPicture != None:
        if hintPicture == 'rotate.png' or hintPicture == 'cross-solved.png':
            hintSpecific.icon.scale = (.33, .396)
        elif hintPicture == 'top.png':
            hintSpecific.icon.scale=(.33*2, .396*2)
        elif hintPicture == 'middleV2.png':
            hintSpecific.icon.scale=(.33*2, .396*2)
            hintSpecific.icon.position = (0, -.325)
            hintSpecific.text_origin = (-.5, .4)
        else:
            hintSpecific.icon.scale = (.33 * 3, .396 * 3)
            hintSpecific.icon.position = (0, -.3)
            hintSpecific.text_origin = (-.5, .3)
        hintSpecific.text = hintText
    if next_piece != None:
        current_piece = next_piece

def displayNotation():
    cube.toggleNotation()

# =============================================================UI buttons======================================================================
# settings==============
settingsButton = Button(text='Controls', text_color = color.black, color=color.gray, scale=.095, position=(-.81, .43, 0),
                        on_click=Func(openSettings))
background = Button(text='', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(-.75, 0.06, 1), scale=(.25, .63), collider='', enabled=False)
resetButton = Button(text='Reset', color=color.red, scale=.1, position=(-.81, -.18, 0), on_click=Func(resetCube),
                     enabled=False)
rotateRButton = Button(text='', icon='rotateR', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.69, .18, 0),
                       on_click=Func(rotateD), enabled=False)
rotateLButton = Button(text='', icon='rotateL', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.81, .18, 0),
                       on_click=Func(rotateU), enabled=False)
rotateUButton = Button(text='', icon='rotateU', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.81, .3, 0),
                       on_click=Func(rotateR), enabled=False)
rotateDButton = Button(text='', icon='rotateD', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.69, .3, 0),
                       on_click=Func(rotateL), enabled=False)
rotateZRButton = Button(text='', icon='rotateZL', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.69, .06, 0),
                       on_click=Func(rotateZR), enabled=False)
rotateZLButton = Button(text='', icon='rotateZR', color=color.white, highlight_color=color.light_gray, scale=.1, position=(-.81, .06, 0),
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

main_menu_button = Button(text='Menu', text_color = color.black, color=color.gray,text_origin=(0,0),position = (-.69,.43,0), on_click=Func(menu), scale=.095)

# hints============
notationButton = Button(text='', text_color = color.black, icon='ShowNotation', color=color.gray, scale=.095, position=(-.69, -.43, 0), on_click=Func(displayNotation))
hintButton = Button(text='Hints', text_color = color.black, color=color.gray, scale=.095, position=(-.81, -.43, 0), on_click=Func(openHints))
hintDisplay = Button(text='', icon='hint1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(.6, .35, 1), scale=(.5, .25), collider='', enabled=False)
hintMoveButton = Button(text='Help', icon='', color=color.dark_gray, scale=(.3,.15), position=(-.3, -.375, -1), parent=hintDisplay, on_click=Func(hintSpecificToggle))
hintDetailButton = Button(text='Details', icon='', color=color.dark_gray, scale=(.2,.15), position=(-.0, -.375, -1), parent=hintDisplay, on_click=Func(hintDetailToggle))
hintDetail = Button(text='', icon='HintDetail1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(-0, -1.85, 1), scale=(1.1, 2.64), collider='', parent = hintDisplay, enabled=False)
hintSpecific = Button(text='We need to flip the %s %s piece\n'       
                           'Rotate the cube so the piece at the bottom right.\n'
                           'Then perform R Di F D', icon='flip-1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(.55, -.1, 1), scale=(.6, .5), collider='', enabled=False)
#hintSpecific.icon.scale = (.33,.396)
hintSpecific.icon.scale = (.33*3, .396*3)
hintSpecific.icon.position = (0,-.3)
hintSpecific.text_origin = (-.5, .3)


# menu buttons ==================
exit = Button(text='Exit',text_color = color.black, model='quad', color=color.red, scale=(.2,.07), text_origin=(0,0), position=(0,-.4))
exit.on_click = application.quit # assign a function to the button.
exittooltip = Tooltip('exit')
start_menu = Button(text='Start QB',text_color = color.black, model='quad', on_click=Func(start), color= color.rgb(0,128,0), scale=(.2,.07), text_origin=(0,0), position  = (0,-.1))
settings_menu = Button(text='Light/Dark Mode',text_color = color.black, model='quad',on_click=Func(darkLight), color= color.rgb(255,255,0), highlight_color = color.yellow.tint(.5), scale=(.2,.07), text_origin=(0,0), position  = (0,-.2))
help_menu = Button(text='Help',text_color = color.black, model='quad', color=color.rgb(255,165,0), scale=(.2,.07), text_origin=(0,0), position  = (0,-.3))
cube_menu_model = Entity(model='cubetest', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, scale=(2,2,2), position = (0,2))
title = Text(text='QB', origin=(0,0), size = 20, background=False, position = (0,2))



if __name__ == '__main__':
    main()
