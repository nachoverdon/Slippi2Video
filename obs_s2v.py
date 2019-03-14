import os
import json
import math
import time
import subprocess
import obspython as obs
from glob import glob
from slippi import Game

replays_dir = ''
dolphin = ''
melee = ''
dolphin_process = None


def get_frames(replay):
    game = Game(replay)
    frames = game.metadata.duration

    return frames

def watch_replay(replay):
    data = {"replay": replay}  # , "isRealTimeMode": False
    with open('replay.txt', 'w') as file:
        json.dump(data, file)

def launch_dolphin():
    watch_replay("")
    return subprocess.Popen([dolphin, '-i', 'replay.txt', '-b', '-e', melee])

def start(properties, button):
    # TODO: Add option to enable recursive search, directoryception.
    replays = glob(replays_dir + '/*.slp')
    found = len(replays)
    print('Replays found:', found)
    if (found):
        dolphin_process = launch_dolphin()
        time.sleep(3)

        # for each replay, load slippi and record video
        for replay in replays:
            watch_replay(replay)
            # Time it takes for a replay to load
            time.sleep(.8)

            if (obs.obs_frontend_recording_active()):
                obs.obs_frontend_recording_stop()

            obs.obs_frontend_recording_start()
            time.sleep(math.ceil(get_frames(replay) / 60) + 1)
            obs.obs_frontend_recording_stop()

        dolphin_process.terminate()


# TODO: Useless because time.sleep is blocking main thread. fix.
def stop(properties, button):
    if (obs.obs_frontend_recording_active()):
        obs.obs_frontend_recording_stop()
    if (dolphin_process != None):
        dolphin_process.terminate()

# ----- OBS
def script_defaults(settings):
    obs.obs_data_clear(settings)

def script_description():
    return 'Launch, sync and record Project Slippi replays.\n' \
        'More info at: https://github.com/nachoverdon/Slippi2Video'

def script_update(settings):
    global replays_dir
    global dolphin
    global melee

    replays_dir = obs.obs_data_get_string(settings, 'replays')
    dolphin = obs.obs_data_get_string(settings, 'dolphin')
    melee = obs.obs_data_get_string(settings, 'melee')

def script_properties():
    props = obs.obs_properties_create()

    rep = ['replays', 'Replays folder', obs.OBS_PATH_DIRECTORY, '', None]
    dol = ['dolphin', 'Dolphin.exe (Slippi)', obs.OBS_PATH_FILE, '*.exe',
        os.getenv('APPDATA') + '\\Slippi Launcher\\dolphin\\Dolphin.exe']
    ml = ['melee', 'Melee 1.02 .ISO', obs.OBS_PATH_FILE, '*.iso', None]

    obs.obs_properties_add_path(props, *rep)
    obs.obs_properties_add_path(props, *dol)
    obs.obs_properties_add_path(props, *ml)

    obs.obs_properties_add_button(props, 'start', 'Start', start)
    obs.obs_properties_add_button(props, 'stop', 'Stop', stop)

    return props
