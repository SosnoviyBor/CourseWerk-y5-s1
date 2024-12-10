## main workflow plan:
- copy text with CTRL + C (true/false)
- react on ALT + C (configurable)
- use clipboard as input
- fix the text
- paste the text back with CTRL + V (true/false)

## design:
- no windows (framework doesnt matter)
- icon in tray
    - list of translation options
    ---
    - settings -> opens config file
    - about
    - exit
- settings (toml)
    - list[filenames]: language list
    - bool: do copy
    - key: copy
    - bool: do paste
    - key: paste
    - key: run translation
    - [ ? ] bool: autostart (requires compiling???)
- [ ? ] compiled to an executable

## libs:
- tomllib - toml reader
- pynput - keyboard manipulation
- pyclip - clipboard interactions
- tkinter / pyqt - desktop app framework
- [ ? ] pyinstaller - exe compiler