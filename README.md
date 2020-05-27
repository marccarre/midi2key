# midi2key

A small Python utility to convert note numbers from MIDI devices to keystrokes.
I typically use it to convert input from my [Freedrums][1] to [Clone Hero][2],
which supports drums in their Public Test Builds, accessible via their Discord.

Configuration is currently hardcoded in the script.
[MIDI Monitor][3] can be used to know which drum maps to which MIDI note.

## Setup

### Prerequisites

1. Install `python3`.
2. Install `pip3`.
3. Run `pip install --user pipenv`
4. Run `pipenv install` to install 3rd party dependencies.

### Usage

```console
./midi2key/midi2key.py
Listening to the following devices:
----
0: interf: b'CoreMIDI', name: b'FD1 v9 Bluetooth', in: 1, out: 0, open: 0
1: interf: b'CoreMIDI', name: b'FD1 v9 Bluetooth', in: 1, out: 0, open: 0
----
llddssqqkkkkkkkkjjjjjjkkkksskkkkkkkkjjqqqqqqdddd^C
Interrupted. Shutting down...
Closing device #0...
Closed device #0...
Closing device #1...
Closed device #1...
Bye!
```

[1]: https://freedrum.rocks/ "Freedrum"
[2]: https://clonehero.net/ "Clone Hero"
[3]: https://www.snoize.com/MIDIMonitor/ "MIDI Monitor"
