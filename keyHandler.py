from pynput import keyboard
import pyclip

import translator
from fileHandlers.configHandler import config
import fileHandlers.layoutHandler as layoutHandler


class Handler:
    controller = keyboard.Controller()
    
    def __init__(self):
        # create hotkey
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse(
                config["options"]["translate"]["keybind"]),
            on_activate=self.onActivate)

        # register listener for it
        self.listener = keyboard.Listener(
            on_press=self.canonical(hotkey.press),
            on_release=self.canonical(hotkey.release))
        self.listener.start()


    # input normalisation
    def canonical(self, func):
        return lambda key: func(self.listener.canonical(key))


    def onActivate(self):
        # get text
        if config["options"]["copy"]["do"]:
            self.pressKeybind(config["options"]["copy"]["keybind"])
        text = pyclip.paste().decode()
        
        # if nothing was selected
        if text.strip() == "":
            return
        
        inLayout = None
        outLayout = None
        # auto mode
        if config["layouts"]["active"] == "Auto":
            layoutNames = [
                config["layouts"]["auto"][0],
                config["layouts"]["auto"][1]]
            layouts = [
                layoutHandler.getLayout(config["layouts"]["auto"][0]),
                layoutHandler.getLayout(config["layouts"]["auto"][1])]
            
            for char in text:
                if char.isalpha():
                    for layout in layouts:
                        # may fuck up with "implicit" case
                        if char.lower() in layout["lower"]:
                            print(f"triggered with {char}")
                            inLayout = layoutNames.pop(layouts.index(layout))
                            outLayout = layoutNames.pop()
                            break
                if inLayout:
                    break
        # manual mode
        else:
            inLayout, outLayout = config["layouts"]["active"].split(" -> ")
        
        # translate it
        translatedText = translator.translate(
            text, inLayout, outLayout)
        
        # paste it
        pyclip.copy(translatedText)
        if config["options"]["paste"]["do"]:
            self.pressKeybind(config["options"]["paste"]["keybind"])


    def pressKeybind(self, keybind):
        # release already translation keybind buttons
        # so they don't interfiere
        for keyName in keyboard.HotKey.parse(config["options"]["translate"]["keybind"]):
            try:    key = keyboard.Key(keyName)
            except: key = keyName
            self.controller.release(key)
        
        # parse keybind keys into a digestable form
        # since pynput doesnt want you to press key combos
        keys = []
        for keyName in keyboard.HotKey.parse(keybind):
            try:    key = keyboard.Key(keyName)
            except: key = keyName
            keys.append(key)
        
        # press them fuckers
        for key in keys:
            self.controller.press(key)
        
        for key in reversed(keys):
            self.controller.release(key)