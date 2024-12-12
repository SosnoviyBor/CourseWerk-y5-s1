# Layman, the layout switcher

<img src="./static/icon.png">

Курсова робота ля-ля-ля...

## Requirements
- OS: Windows (others haven't been tested yet)
- pystray
- pynput
- pyclip
- pillow

## How to use
0. Open `config.json` and fill the `layouts` part of it with layouts from `/layouts` folder.

Make sure to list in `displayed` layouts only those, which you will actually use. Otherwise you'll just pollute your menu with useless junk.

__Configs update only on Layman's launch!__

1. Run Layman with `py main.py` command.
2. Pick your layout option in Layman.
3. Select text you want to translate and hit `Alt + B` keys.

__`Auto` layout works only with different alphabets!__ And supports only 2 layouts per time.

4. ? ? ?
5. Profit!

## Todo
- Config verifier and default config generator
- CI/CD
- Implement autostart
- Linux support