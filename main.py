from classes import *
from constants import *
from functions import *


def cycleFour():
    cMajor = Scale(0, major)
    intMap = {"5": 1, "3": 1, "1": 0}
    funMap = {"5": "3", "3": "1", "1": "5"}
    voiceLeading = VoiceLeading(cMajor, intMap, funMap)
    startingChord = Chord(
        0,
        [
            ChordTone("1", cMajor.notes[0]),
            ChordTone("3", cMajor.notes[2]),
            ChordTone("5", cMajor.notes[4]),
        ],
    )
    return voiceLeading, startingChord


if __name__ == "__main__":
    generateChordFamily(*getCycle(0, melod, 6))
    # generateChordFamily(*cycleFour())
