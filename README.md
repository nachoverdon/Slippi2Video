# Slippi2Video
Script to convert Project Slippi replays into video using OBS

# Requires
* Python 3.6+ (`s2v.py` might work with a lesser version, but `obs_s2v.py` won't)
* Windows or Mac. Untested on other platforms. Might work perfectly though, who knows.
* [Project Slippi desktop app](https://github.com/project-slippi/slippi-desktop-app/releases). Comes with a custom version of Dolphin, select this one when setting up your `config.py` or OBS script. Configure Dolphin as you like. If the changes are not getting saved, check that the folder is not read only or that you have permissions.
* Install python dependencies. For Windows:
```
pip install py-slippi pyautogui
```
For Mac, `pyautogui` has a couple of extra requirements, which you can install with: `pip install -r requirements-mac.txt`. [py-slippi](https://github.com/hohav/py-slippi) is under development, so you might need the git version (this script was writen using this [commit](https://github.com/hohav/py-slippi/tree/967973d9650247de541a2e20cfd727eea3a8331a))
```pip install git+https://github.com/hohav/py-slippi --upgrade```
* [OBS](https://obsproject.com/) (64 bits) installed. It also needs the `Stop recording` hotkey to be set to `CTRL+ALT+END` (default, can be changed on config.py, here is the [list with the key names](https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function)). Also you need to configure obs the way you want to record the game, so create a scene and add Dolphin as source, etc...
* Fill config.py with the paths to the replays folder, Dolphin.exe (Slippi), Super Smash Bros. Melee NTSC 1.02 version .iso and OBS64.
* `python s2v.py`
* Pray for it to work.

# OBS Script
Only tested for Windows. "Python scripting has never been officially supported on mac since we couldn't get it to work (also issues with the buildserver I believe). Doesn't appear that anybody has figured out why it didn't work or fixed it." (per [Rodney on OBS Forums](https://obsproject.com/forum/threads/python-scripting-dont-work-on-obs-22-0-3.99061/#post-386891))

Instead of using s2v.py, it's possible to use OBS' built-in Python API (preferable atm). Set up take a little bit longer.

* Open OBS and go to `Tools` > `Scripts` > `Python Settings` and there select the directory with your `python.exe`.
__IMPORTANT NOTE:__ Must match Python/OBS bits version (32 or 64 bits) and must be Python 3.6.something, as 3.7 doesn't work (OBS fault I think, as I just doesn't even execute the sample script that comes with the program) or maybe it's just me lol. As a result, if you opt for a 'portable' version of Python, you'll probably need to follow [this guide](https://michlstechblog.info/blog/python-install-python-with-pip-on-windows-by-the-embeddable-zip-file/) in order to be able to download the necessary packages py-slippi.
* Go to the `Scripts` tab, click the `+` button, and select `obs_s2v.py`.
* Configure the options and click Start
* Pray once again

# Notes
Things to investigate/improve:

Better sync

Trimming video / cut black frames

Dolphin 200% + audio dump, then ffmpeg slowdown

Dolphin codecs

Renaming video with game info (player names, chars, stage...)

Youtube auto upload

Use queue system
