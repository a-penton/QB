from ursina import *
from visCube import *
from visHints import *
from cubesolver import *
import random
from rubik.cube import Cube
import os

#application.asset_folder=application.package_folder.parent

anim = False  # used to lockout inputs during animation
blinking = False
drag = False  # used to rotate cube with mouse
reading = False # used to lockout inputs during reading strings
settings = False #checks if settings menu is open
hints = False #checks if hints menu is open
colorScheme = False #Checks if the color scheme has changed
bgmToggle = False
readSequence = Sequence() #used for sequence of moves
mousepos = []  # stores mouse position for rotating camera
app = Ursina()
# window settings
window.borderless = False
window.fps_counter.enabled = True
window.exit_button.visible = False
window.color = color.dark_gray

window.fullscreen = True
window.aspect_ratio = 2

# initializing entities
cube = VisCube()  # rubiks cube
hintCube = VisHints()  # hints
center = Entity()  # center transform, used for rotation
current_piece = None
current_stage = -1

error_timer = 0


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
    global error_timer
    if not anim and not reading and not inputList.enabled:  # if not already animated, read keys and animate
        if key == 'm':  # this one is for hints, and requires a longer delay
            #anim = True
            #hintCube.rotateF()
            #invoke(endAnim, delay=.6)
            cube.print()
            #updateCurrentHint('Move the %s %s piece above its center\n test', 'flip-2', None)
    if inputList.enabled and not cube.anim:#inputs string from ui textbox as a list off moves
        if key == 'enter':
            error_text.enabled = False
            if validString(inputList.text):
                readString(inputList.text)
            else:
                error_text.enabled = True
                error_timer = 0

    if key == 'left mouse down':
        error_text.enabled = False
        invoke(checkCurrentHint, delay=cube.turnSpeed+.25)
        if mouse_in_zone(mouse.position):
            cube.disableArrows()
            drag = True
            mousepos = mouse.position

    if key == 'left mouse up':
        cube.reenableArrows()
        drag = False
        cube.rotation = (0, 0, 0)



def update():  # called every frame
    global mousepos
    global center
    global anim
    global reading
    global error_timer
    global drag 
    # makes the main menu cube rotate
    if cube_menu_model.enabled:
        cube_menu_model.rotation_y += time.dt * 100

    if error_text.enabled:
        if error_timer >= 180:
            error_text.enabled = False
        else:
            error_timer += 1
    if drag:
        cube.reparent_to(center)
        center.rotation_y += 300 * (mousepos[0] - mouse.position[0])
        center.rotation_x += 300 * (mouse.position[1] - mousepos[1])
        cube.reparent_to(scene)
        center.rotation = (0, 0, 0)
    mousepos = mouse.position



def endAnim():  # resets anim to false, needs to be a function to be used with invoke() and delay
    global anim
    anim = False


# =====================================================ui buttons=====================================================

def mouse_in_zone(mousepos):
    if mousepos[0] < -0.43 or mousepos[1] < -0.35:
        return False
    return True

def checkCurrentHint():
    updateCurrentHint(*hint(cube.virtualCube, current_piece, current_stage))

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
    # this fixes the issue where cube reset reverts color scheme
    if colorScheme == True:
        toggle_color_scheme()
        toggle_color_scheme()
    anim = True
    invoke(endAnim, delay=.65)
    changeTurnSpeed()
    # inputList.text = ''
    # inputList.cursor.origin = (-1,-.5)
    inputList.enabled= False
    cube.virtualCube = Cube("RRRRRRRRRBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYOOOOOOOOO") # Resets virtual cube


def openSettings(): #open settings menu
    global settings
    if not settings:
        #settingsButton.color = color.light_gray
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
        #settingsButton.color = color.gray
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
        hintSpecific.enabled = False

    if blinking:
        blinking = False
        cube.unblink()

def validString(input):
    
    valid_chars = ["F", "L", "R", "D", "B", "M", "U", "S", "E", "X", "Y", "Z"]
    other_chars = ["i", "2"]

    for i in range(len(input)):
        if input[i].upper() not in valid_chars:
            if not (i > 0 and input[i].lower() in other_chars and input[i - 1].upper() in valid_chars):
                if input[i] != " ":
                    return False
    return True

def readString(rotations, scrambling = False):  # goes through string and does each move
    global reading
    global readSequence
    if not reading:
        cube.disableArrows()
        cube.setTurnSpeed(.1)
        stepTime = .4  # time between moves in sequence must be at least .2 higher than turn speed
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
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateU))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateU))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateU))
            elif rotations[i].upper() == 'E':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateEi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateE))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateE))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateE))
            elif rotations[i].upper() == 'D':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateDi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateD))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateD))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateD))
            elif rotations[i].upper() == 'L':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateLi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateL))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateL))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateL))
            elif rotations[i].upper() == 'M':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateMi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateM))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateM))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateM))
            elif rotations[i].upper() == 'R':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateRi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateR))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateR))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateR))
            elif rotations[i].upper() == 'F':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateFi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateF))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateF))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateF))
            elif rotations[i].upper() == 'S':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateSi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateS))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateS))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateS))
            elif rotations[i].upper() == 'B':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateBi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateB))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateB))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateB))
            elif rotations[i].upper() == 'X':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateXi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateX))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateX))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateX))
            elif rotations[i].upper() == 'Y':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateYi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateY))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateY))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateY))
            elif rotations[i].upper() == 'Z':
                if rotations[i + 1].lower() == "i":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateZi))
                elif rotations[i + 1] == "2":
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateZ))
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateZ))
                else:
                    readSequence.append(stepTime)
                    readSequence.append(Func(cube.rotateZ))
            elif rotations[i].lower() != 'i' and rotations[i] != ' ' and rotations[i] != '2':
                print("Invalid Input")


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
    global current_piece
    if blinking:
        blinking = False
        cube.unblink()
    else:
        blinking = True
        cube.blink(current_piece)


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


def updateCurrentHint(hintText, hintPicture, next_piece, next_stage):
    global current_piece
    global current_stage
    global blinking
    if hintText != None:
        hintSpecific.text = hintText
    if hintPicture != None:
        if hintPicture in ['rotate-white-bottom.png', 'cross-solved.png']:
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
        hintSpecific.icon = hintPicture
    
    current_piece = next_piece
    current_stage = next_stage
    if blinking:
        cube.unblink()
        cube.blink(current_piece)


def displayNotation():
    cube.toggleNotation()


def menu():
    cube_menu_model.enabled = True
    title.enabled = True
    help_menu.enabled = True
    tutorial_menu.enabled = True
    setting_menu.enabled = True
    start_menu.enabled = True
    exit.enabled = True
    hintButton.enabled = False
    #settingsButton.enabled = False
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
    #settingsButton.color = color.gray
    #hintButton.color = color.gray
    aboutus_menu.enabled = False
    tutorial_box.enabled = False
    inputList.enabled= False
    error_text.enabled = False


def darkLight():
    if window.color == color.dark_gray:
        window.color = color.light_gray
        light_dark.icon = 'Picture2'
        wallpaper.icon = 'testing_light'
        title.icon = 'title_text_copy'
        setting_menu.icon = 'gear'

    elif window.color == color.light_gray:
        window.color = color.dark_gray
        light_dark.icon = 'Picture1'
        wallpaper.icon = 'testing_dark'
        title.icon = 'title_text'
        setting_menu.icon = 'gear_light'


def bgm_toggle():
    global bgmToggle
    if not bgmToggle:
        bgm_buttom.icon = 'off_bgm'
        bgAudio.pause()
        bgmToggle = True
    else:
        bgm_buttom.icon = 'on_bgm'
        bgAudio.resume()
        bgmToggle = False


def toggleAboutus():
    tutorial_box.enabled = False
    if aboutus_menu.enabled == True:
        aboutus_menu.enabled = False
    elif aboutus_menu.enabled == False:
        aboutus_menu.enabled = True


def toggleTutorial():
    aboutus_menu.enabled = False
    if tutorial_box.enabled == True:
        tutorial_box.enabled = False
    elif tutorial_box.enabled == False:
        tutorial_box.enabled = True


def toggle_color_scheme():
    global colorScheme
    if not colorScheme:
        cube_menu_model.texture = "colorscheme2"
        color_scheme.icon = "colorscheme2"
        cube.W.texture = "colorscheme2"
        cube.WG.texture = "colorscheme2"
        cube.WB.texture = "colorscheme2"
        cube.WR.texture = "colorscheme2"
        cube.WO.texture = "colorscheme2"
        cube.WRG.texture = "colorscheme2"
        cube.WGO.texture = "colorscheme2"
        cube.WBR.texture = "colorscheme2"
        cube.WOB.texture = "colorscheme2"
        cube.R.texture = "colorscheme2"
        cube.GR.texture = "colorscheme2"
        cube.BR.texture = "colorscheme2"
        cube.YR.texture = "colorscheme2"
        cube.YGR.texture = "colorscheme2"
        cube.YRB.texture = "colorscheme2"
        cube.G.texture = "colorscheme2"
        cube.GO.texture = "colorscheme2"
        cube.YG.texture = "colorscheme2"
        cube.YOG.texture = "colorscheme2"
        cube.B.texture = "colorscheme2"
        cube.BO.texture = "colorscheme2"
        cube.YB.texture = "colorscheme2"
        cube.YBO.texture = "colorscheme2"
        cube.O.texture = "colorscheme2"
        cube.YO.texture = "colorscheme2"
        cube.Y.texture = "colorscheme2"
        colorScheme = True
    else:
        cube_menu_model.texture = "RubiksTex"
        cube.W.texture = "RubiksTex"
        cube.WG.texture = "RubiksTex"
        cube.WB.texture = "RubiksTex"
        cube.WR.texture = "RubiksTex"
        cube.WO.texture = "RubiksTex"
        cube.WRG.texture = "RubiksTex"
        cube.WGO.texture = "RubiksTex"
        cube.WBR.texture = "RubiksTex"
        cube.WOB.texture = "RubiksTex"
        cube.R.texture = "RubiksTex"
        cube.GR.texture = "RubiksTex"
        cube.BR.texture = "RubiksTex"
        cube.YR.texture = "RubiksTex"
        cube.YGR.texture = "RubiksTex"
        cube.YRB.texture = "RubiksTex"
        cube.G.texture = "RubiksTex"
        cube.GO.texture = "RubiksTex"
        cube.YG.texture = "RubiksTex"
        cube.YOG.texture = "RubiksTex"
        cube.B.texture = "RubiksTex"
        cube.BO.texture = "RubiksTex"
        cube.YB.texture = "RubiksTex"
        cube.YBO.texture = "RubiksTex"
        cube.O.texture = "RubiksTex"
        cube.YO.texture = "RubiksTex"
        cube.Y.texture = "RubiksTex"
        color_scheme.icon = "RubiksTex"
        colorScheme = False



def toggleSettings():
    if setting_menu.color == color.clear:
        setting_menu.color = color.gray
    elif setting_menu.color == color.gray:
        setting_menu.color = color.clear
    if light_dark.enabled == True:
        light_dark.enabled = False
    elif light_dark.enabled == False:
        light_dark.enabled = True
    if settings_box.enabled == True:
        settings_box.enabled = False
    elif settings_box.enabled == False:
        settings_box.enabled = True
    if color_scheme.enabled == True:
        color_scheme.enabled = False
    elif color_scheme.enabled == False:
        color_scheme.enabled = True
    if volumeSlider.enabled == True:
        volumeSlider.enabled = False
    elif volumeSlider.enabled == False:
        volumeSlider.enabled = True
    if bgm_buttom.enabled == True:
        bgm_buttom.enabled = False
    elif bgm_buttom.enabled == False:
        bgm_buttom.enabled = True
    if bgm_title.enabled == True:
        bgm_title.enabled = False
    elif bgm_title.enabled == False:
        bgm_title.enabled = True



def start():
    cube_menu_model.enabled = False
    title.enabled = False
    help_menu.enabled = False
    tutorial_menu.enabled = False
    setting_menu.enabled = False
    exit.enabled = False
    start_menu.enabled = False
    hintButton.enabled = True
    #settingsButton.enabled = True
    cube.enabled = True
    main_menu_button.enabled = True
    notationButton.enabled = True
    aboutus_menu.enabled = False
    tutorial_box.enabled = False
    setting_menu.color = color.clear
    settings_box.enabled == False
    light_dark.enabled = False
    color_scheme.enabled = False
    settings_box.enabled = False
    volumeSlider.enabled = False
    bgm_buttom.enabled = False
    bgm_title.enabled = False

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


# =============================================================UI buttons======================================================================
# settings======================
# settingsButton = Button(text='Controls', text_color = color.black, color=color.gray, scale=.095, position=(-.81, .43, 0),
                        # on_click=Func(openSettings))
background = Button(text='', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(-.74, -.059, 1), scale=(.42, .862), collider='', enabled=False)
resetButton = Button(text='', icon='reset_button',color=color.clear,highlight_color=color.light_gray,scale=.152, position=(-.85, -.39, 0), on_click=Func(resetCube),
                     enabled=False)

rotateRButton = Button(text='', icon='rotateR', color=color.white, highlight_color=color.light_gray, scale=.152, position=(-.63, .113, 0),
                       on_click=Func(rotateD), enabled=False)
rotateLButton = Button(text='', icon='rotateL', color=color.white, highlight_color=color.light_gray, scale=.152, position=(-.85, .113, 0),
                       on_click=Func(rotateU), enabled=False)
rotateUButton = Button(text='', icon='rotateU', color=color.white, highlight_color=color.light_gray, scale=.152, position=(-.85, .278, 0),
                       on_click=Func(rotateR), enabled=False)
rotateDButton = Button(text='', icon='rotateD', color=color.white, highlight_color=color.light_gray, scale=.152, position=(-.63, .278, 0),
                       on_click=Func(rotateL), enabled=False)
rotateZRButton = Button(text='', icon='rotateZL', color=color.white, highlight_color=color.light_gray, scale=.152, position=(-.63, -.056, 0),
                       on_click=Func(rotateZR), enabled=False)
rotateZLButton = Button(text='', icon='rotateZR', color=color.white, highlight_color=color.light_gray, scale=.152, position=(-.85, -.056, 0),
                       on_click=Func(rotateZL), enabled=False)
inputButton = Button(text='', icon='input_button',color=color.clear,highlight_color=color.light_gray, scale=.152, position=(-.63, -.225, 0), on_click=Func(toggleInput),
                     enabled=False)
# inputList = TextField(max_lines=1, position=(-.37 ,-.32 ,0), enabled=False)

scrambleButton = Button(text='', icon='scramble_button',color=color.clear,highlight_color=color.light_gray, scale=.152, position=(-.85, -.225, 0), on_click=Func(scramble),
                     enabled=False)
speedSlider = Slider(min=1, max=.1, default=.5, text='Turn Speed', height=.1, on_value_changed=Func(changeTurnSpeed), position=(-.7, -.42, 0), scale=.24, enabled=False)
speedSlider.label.origin = (0,0)
speedSlider.label.position = (.24,.25)
speedSlider.label.scale = 4.5
speedSlider.knob.text_color = color.clear

main_menu_button = Button(text='',icon='menu_button', color=color.clear, position = (-.745,.435), on_click=Func(menu), scale=(.3,.11))


# hints==================================
#Bottom buttons
notationButton = Button(text='', icon='notation_button', color=color.clear, scale=(.31,.12),position=(.13, -.43), on_click=Func(displayNotation))
hintButton = Button(text='', icon='hints_button', color=color.clear,highlight_color=color.clear, scale=(.31,.12), position=(-.22, -.43), on_click=Func(openHints))

#top hint box
hintDisplay = Button(text='', icon='hint1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(.65, .35, 1), scale=(.58, .252), collider='', enabled=False)
#Small buttons
hintMoveButton = Button(text='Help', icon='', color=color.dark_gray, scale=(.25,.15), position=(-.24, -.375, -1), parent=hintDisplay, on_click=Func(hintSpecificToggle))
hintDetailButton = Button(text='Details', icon='', color=color.dark_gray, scale=(.25,.15), position=(.06, -.375, -1), parent=hintDisplay, on_click=Func(hintDetailToggle))
#big detailed hint
hintDetail = Button(text='', icon='HintDetail1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(0, -1.85, 1), scale=(1.03, 2.64), collider='', parent = hintDisplay, enabled=False)
#Specific hint box
hintSpecific = Button(text='We need to flip the %s %s piece\n'       
                           'Rotate the cube so the piece at the bottom right.\n'
                           'Then perform R Di F D', icon='flip-1', color=color.gray, highlight_color=color.gray, pressed_color=color.gray,
                    position=(.65, -.1, 1), scale=(.597, .61), collider='', enabled=False)
#hintSpecific.icon.scale = (.33,.396)
hintSpecific.icon.scale = (.329*3, .396*3)
hintSpecific.icon.position = (.06,-.3)
hintSpecific.text_origin = (-.5, .3)

# menu buttons =================================
exit = Button(text='',icon='quit_button', text_color = color.black, color=color.clear,scale=(.36,.12), position=(-.7,-.35)) # button
exit.on_click = application.quit
exittooltip = Tooltip('exit')
start_menu = Button(text='', icon='start_button', text_color = color.black, on_click=Func(start), color= color.clear, scale=(.36,.12), position  = (-.7,.1))# button
tutorial_menu = Button(text='',icon='tutorial_button',on_click=Func(toggleTutorial),text_color = color.black, color= color.clear,scale=(.36,.12),position  = (-.7,-.05)) #button
help_menu = Button(text='',icon='aboutus_button',on_click=Func(toggleAboutus), text_color = color.black, color=color.clear, scale=(.36,.12), position=(-.7,-.2)) #button
cube_menu_model = Entity(model='cubetest', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, scale=(3.5,3.5,3.5), position = (1.5,0))
title = Button(text='',icon='title_text', color=color.clear, scale = (.5,.21),position = (-.7,.3))

setting_menu = Button(text='',icon='gear_light', color=color.clear, highlight_color = color.gray, scale=(.1,.1),on_click=Func(toggleSettings), position=(.85,.4))
light_dark = Button(text='',icon='Picture1', color=color.clear,scale=(.2,.08),on_click=Func(darkLight), position=(.85,.3), enabled=False)
color_scheme = Button(text='',icon='RubiksTex', color=color.clear,scale=(.2,.08),on_click=Func(toggle_color_scheme), position=(.85,.21), enabled=False)
bgm_buttom = Button(text='',icon='on_bgm', color=color.clear,scale=(.2,.08),on_click=Func(bgm_toggle), position=(.85,.015), enabled=False)
bgm_title = Button(text='Music', color=color.clear, position=(.85, 0.065), enabled=False, scale=.01)
settings_box = Button(text='', color=color.gray, highlight_color=color.gray, icon = '', pressed_color=color.gray, position = (.85,.155,50),scale=(.23,.375), enabled=False)


aboutus_menu = Button(text='\t      About Us\n\n\tMembers:\n\tAndrew Penton\n\tNoah Gorgevski-Sharpe\n\tHeinrich Perez\n\tSteven Perez\n\tDaniel Shinkarow',
                        color=color.gray, position=(0,0), scale=(.69,.73),highlight_color=color.gray, pressed_color=color.gray,text_origin=(-.35,.45))
tutorial_box = Button(text='Tutorial\nPlace holder text',color=color.gray, position=(0,0), scale=(.69,.73),highlight_color=color.gray, pressed_color=color.gray,text_origin=(-.35,.45))

wallpaper = Button(text='',icon='testing_dark',color=color.clear,highlight_color=color.clear, pressed_color=color.clear,enabled=True, parent=camera, position=(0,0,50),scale=(1920/52,1080/52))

bgVolume = .5
bgAudio = Audio('impossiblegame', pitch=1, loop=True, autoplay=True, volume=.5)
bgAudio.play()

def changeAudio():
    bgAudio.volume = volumeSlider.value

volumeSlider = Slider(0, 1, default = .5,text = 'Volume',height=.05, dynamic=True, on_value_changed=changeAudio, color=color.gray, scale=.4 ,x = .743,y = .1, enabled=False)
volumeSlider.knob.text_color = color.clear
volumeSlider.label.origin = (0,0)
volumeSlider.label.position = (.25,.1)
volumeSlider.label.scale = 2.3

inputList = TextField(max_lines=1, position=(-.22 ,-.33 ,0), enabled=False)
error_text = Text(text='Error: Invalid Input', origin=(1.5 ,13.65 ,1), enabled=False, color=color.red)
