from pynput import keyboard
import pyclip

import translator
from configHandler import config


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
        # cropping the sides of pasted data since pyclip is dumb
        text = str(pyclip.paste())[2:-1]
        text = text.replace("\\r\\n", "\n")
        
        # translate it
        translatedText = translator.translate(
            text, *config["layouts"]["active"].split(" -> "))
        
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