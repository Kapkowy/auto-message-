import pyautogui
import PySimpleGUI as Sg
import keyboard
import pickle
import os

os.system("cls")

layout = [[Sg.In('', size=(25, 0), key='lol0'),
           Sg.OptionMenu(size=(2, 0), values=['F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'F10'],
                         default_value='F2', key='ll0')],
          [Sg.In('', size=(25, 0), key='lol1'),
           Sg.OptionMenu(size=(2, 0), values=['F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'F10'],
                         default_value='F3', key='ll1')],
          [Sg.In('', size=(25, 0), key='lol2'),
           Sg.OptionMenu(size=(2, 0), values=['F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'F10'],
                         default_value='F4', key='ll2')],
          [Sg.In('', size=(25, 0), key='lol3'),
           Sg.OptionMenu(size=(2, 0), values=['F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'F10'],
                         default_value='F6', key='ll3')],
          [Sg.In('', size=(25, 0), key='lol4'),
           Sg.OptionMenu(size=(2, 0), values=['F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'F10'],
                         default_value='F7', key='ll4')],
          [Sg.In('', size=(25, 0), key='lol5'),
           Sg.OptionMenu(size=(2, 0), values=['F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'F10'],
                         default_value='F8', key='ll5')],
          [Sg.Button('Kliknij tu aby odpalic!', key='wtf')]]

window = Sg.Window('Auto Message LOL', layout, icon='icon.ico')


def lol():
    while True:
        if keyboard.is_pressed(values['ll0']):
            keyboard.write(values['lol0'])
            keyboard.press("ENTER")
            pyautogui.leftClick()
            print(values['lol0'])
        #
        if keyboard.is_pressed(values['ll1']):
            keyboard.write(values['lol1'])
            keyboard.press("ENTER")
            pyautogui.leftClick()
            print(values['lol1'])
        #
        if keyboard.is_pressed(values['ll2']):
            keyboard.write(values['lol2'])
            keyboard.press("ENTER")
            pyautogui.leftClick()
            print(values['lol2'])
        #
        if keyboard.is_pressed(values['ll3']):
            keyboard.write(values['lol3'])
            keyboard.press("ENTER")
            pyautogui.leftClick()
            print(values['lol3'])
        #
        if keyboard.is_pressed(values['ll4']):
            keyboard.write(values['lol4'])
            keyboard.press("ENTER")
            pyautogui.leftClick()
            print(values['lol4'])
        #
        if keyboard.is_pressed(values['ll5']):
            keyboard.write(values['lol5'])
            keyboard.press("ENTER")
            pyautogui.leftClick()
            print(values['lol5'])
        #
        if keyboard.is_pressed("ESC"):
            break


while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == Sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'wtf':
        Sg.popup('Pog:', "Aby zatrzymac usluge kliknij!", icon='icon.ico')
        Sg.popup('Pog:', "Jesli klikniesz OK program zacznie dzialac!", icon='icon.ico')
        lol()
window.close()
