# Slippi2Video
Script to convert Project Slippi replays into video using OBS

# Requires
* Windows. Untested on other platforms. Might work perfectly though, who knows.
* [Project Slippi desktop app](https://github.com/project-slippi/slippi-desktop-app/releases). Comes with a custom version of Dolphin. Configure Dolphin as you like, but check the `Render to main window` option on `Graphics/General`. If the changes are not getting saved, check that the folder is not read only or that you have permissions.
* Install python dependencies.
```
pip install py-slippi
```
[py-slippi](https://github.com/hohav/py-slippi) is under development, so you might need the git version (this script was writen using this [commit](https://github.com/hohav/py-slippi/tree/967973d9650247de541a2e20cfd727eea3a8331a))
```pip install git+https://github.com/hohav/py-slippi --upgrade```
* [OBS](https://obsproject.com/) (64 bits) installed. It also needs the `Stop recording` hotkey to be set to `CTRL+ALT+END` (default, can be changed on config.py, here is the [list with the key names](https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function)). Also you need to configure obs the way you want to record the game, so create a scene and add Dolphin as source, etc...
* Fill config.py with the paths to the replays folder, Dolphin.exe (Slippi), Super Smash Bros. Melee NTSC 1.02 version .iso and OBS64.
* `python s2v.py`
* Pray for it to work.

# OBS Script
Instead of using s2v.py, it's possible to use OBS' built-in Python API (preferable atm). Set up take a little bit longer.

* Open OBS and go to `Tools` > `Scripts` > `Python Settings` and there select the directory with your `python.exe`. *IMPORTANT NOTE:* Must match Python/OBS bits version (32 or 64 bits) and must be Python 3.6.something, as 3.7 doesn't work (OBS fault I think, as I just doesn't even execute the sample script that comes with the program) or maybe it's just me lol. As a result, if you opt for a 'portable' version of Python, you'll probably need to follow [this guide](https://michlstechblog.info/blog/python-install-python-with-pip-on-windows-by-the-embeddable-zip-file/) in order to be able to download the necessary packages py-slippi.

# Notes
Things to investigate/improve:

Better sync

Trimming video

Dolphin 200% + audio dump, then ffmpeg slowdown

Dolphin codecs

Renaming video with game info (player names, chars, stage...)

Youtube auto upload
