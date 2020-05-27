#!/usr/bin/env python
from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '0'  # Hide welcome message: "Hello from the pygame community. https://www.pygame.org/contribute.html"
import sys
import pygame.midi as midi
import keyboard

RED, YELLOW, BLUE, GREEN, ORANGE, WHITE = 0, 1, 2, 3, 4, 5

CLONE_HERO = {
    RED:    's',  # Snare
    YELLOW: 'd',  # Hi-Hat / Cymbals
    BLUE:   'j',  # High Tom / Medium Tom
    GREEN:  'k',  # Medium Tom / Low Tomtom / Cymbals
    ORANGE: 'q',  # Ride / Crash / Other Cymbals
    WHITE:  'l',  # Kick
}

FREEDRUM = {
    38: CLONE_HERO[RED],     # Snare
    42: CLONE_HERO[YELLOW],  # Hi-Hat
    # 46: '',  # Hit Hat Open
    50: CLONE_HERO[BLUE],    # Hi Tom
    47: CLONE_HERO[GREEN],   # Mid Tom
    57: CLONE_HERO[ORANGE],  # Crash
    36: CLONE_HERO[WHITE],   # Kick
    # 41: '',  # Low Tom
    # 44: '',  # Pedal Hi-Hat
}

def main():
    midi.init()
    device_ids = input_device_ids()
    if not device_ids:
        print('No MIDI input devices.', file=sys.stderr)
        sys.exit(1)
    print_devices_info(device_ids)
    listen_to(device_ids)

INTERF, NAME, IN, OUT, OPEN = 0, 1, 2, 3, 4

def input_device_ids():
    device_ids = []
    for device_id in range(midi.get_count()):
        info = midi.get_device_info(device_id)
        if info[IN] == 1:
            device_ids.append(device_id)
    return device_ids

def print_devices_info(device_ids):
    print('Listening to the following devices:')
    print('----')
    for device_id in device_ids:
        print_device_info(device_id)
    print('----')

def print_device_info(device_id):
    print('%d: interf: %s, name: %s, in: %d, out: %d, open: %d' % (device_id, *midi.get_device_info(device_id)))

NUM_EVENTS = 1024
SLEEP_TIME_IN_SECS = 0.02  # 20 ms

def listen_to(device_ids):
    try:
        devices = [midi.Input(device_id) for device_id in device_ids]
        while True:
            for device in devices:
                if device.poll():
                    events = device.read(NUM_EVENTS)
                    for event in events:  # e.g.: [[[137, 41, 0, 0], 1373474], [[153, 41, 8, 0], 1373475], ...]
                        data, timestamp = event
                        _, note_number, _, _ = data
                        if note_number in FREEDRUM:
                            keyboard.press_and_release(FREEDRUM[note_number])
            sleep(SLEEP_TIME_IN_SECS)  # Prevent busy polling at 100% CPU.
    except KeyboardInterrupt:
        print('\nInterrupted. Shutting down...')
    finally:
        for device in devices:
            try_close(device)
        midi.quit()
        print('Bye!')

def try_close(device):
    device_id = device.device_id
    print('Closing device #%d...' % device_id)
    try:
        device.close()
    except Exception as e:
        print(e, file=sys.stderr)
    print('Closed device #%d...' % device_id)

if __name__ == '__main__':
    main()
