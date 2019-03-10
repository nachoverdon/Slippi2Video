import os
import time
import math
import json
import subprocess
import pyautogui as pag
from glob import glob
from slippi import Game
from config import CONFIG


# Path with the replays
replays_folder = CONFIG['replays_folder']
# path to Dolphin (Slippi)
dolphin = CONFIG['dolphin']
melee = CONFIG['melee']
obs_path = CONFIG['obs_path']
obs_exe = 'obs64.exe'
hotkey = CONFIG['hotkey'] # hotkey to stop recording OBS

# Fetch replay data, load Slippi and records video
def convert(replay):
    frames = get_frames(replay)
    seconds = math.ceil(frames / 60)
    if seconds <= 30:
        print('Replay ' + replay + ' is 30 seconds long or less.')
        return
    dolphin_process = launch_dolphin()
    record_video(replay, seconds, dolphin_process)


def get_frames(replay):
    game = Game(replay)
    frames = game.metadata.duration

    return frames


def record_video(replay, seconds, dolphin_process):
    # starts OBS recording
    obs_process = launch_obs()
    print('Recording...')
    watch_replay(replay)

    # waits for the duration of the replay
    time.sleep(seconds)
    # time.sleep(6)

    # performs hotkey to stop recording
    pag.hotkey(*hotkey)
    time.sleep(1)

    # closes Dolphin and OBS
    dolphin_process.terminate()
    obs_process.terminate()


def watch_replay(replay):
    data = {"replay": replay}  # , "isRealTimeMode": False
    with open('replay.txt', 'w') as file:
        json.dump(data, file)


def launch_dolphin():
    watch_replay("")
    dolphin_process = subprocess.Popen(
        [dolphin, '-i', 'replay.txt', '-b', '-e', melee])
    time.sleep(2)  # Time it takes to load game aprox.

    return dolphin_process


def launch_obs():
    # Current working directory. Due to a bug in OBS, it cannot launch from cmd
    # unless it's launched from its directory
    cwd = os.getcwd()
    os.chdir(obs_path)
    obs_process = subprocess.Popen([obs_exe, '--startrecording'])
    os.chdir(cwd)
    time.sleep(2)

    return obs_process


# Get replays names
replays = glob(replays_folder + '/*.slp')

# for each replay, load slippi and record video
for replay in replays:
    convert(replay)

