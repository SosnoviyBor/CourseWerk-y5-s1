# Layman, the layout switcher

<img src="./static/icon.png">

Fully customisable, yet simple layout switcher. As it should be.

Sometimes you just forget to switch keyboard layout and end up writing _іщьуерштп дшлу ерші_ instead of _something like this_. But what if instead of writing everything from scratch you just pressed one keybind?

<img src="./static/demo.gif">

You can add your own custom layouts to the app in `./layouts` folder based on the template. Just don't forget to add it later to the config file.

## Requirements
- OS: Windows (others haven't been tested yet)
- Python 3
    - pystray
    - pynput
    - pyclip
    - pillow

## How to use
0. [Download](https://www.python.org/downloads/) and install python. Then install project requirements.

```cmd
pip install -r requirements.txt
```

1. Open `config.json` and fill the `layouts` list with filenames from `/layouts` folder.

> [!TIP]
> Make sure to list in `displayed` layouts only those you will actually use. Otherwise you'll just pollute your menu with useless junk.

> [!IMPORTANT]
> Configs update only on app launch!

2. Run Layman. Its icon should appear in the icon bar.

```cmd
py main.py
```

3. Pick your layout option in the app.

> [!IMPORTANT]
> `Auto` layout works only with different alphabets! And supports only 2 layouts per time.

4. Select the text and hit your `translate` keybind (<kbd>Alt</kbd> + <kbd>B</kbd> by default).
5. ? ? ?
6. Profit!

## Todo
- [ ] Moar layouts
- [ ] Layout adding guide
- [ ] Project compiling with GitHub Actions
- [ ] Implement autostart
- [ ] Linux support