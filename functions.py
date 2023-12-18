from classes import *


def generateChordFamily(voiceLeading, startingChord):
    chord = Chord(startingChord.root, startingChord.chordTones)
    while True:
        print(chord)
        chord = chord.transpose(voiceLeading)
        if chord.pitchClasses() == startingChord.pitchClasses():
            break


def getSevenToneTriad(scale, voicing="close"):
    notes = [(x[0], (scale.notes[x[1]])) for x in sevenToneTriad]
    if voicing == "spread":
        notes = [notes[0], notes[2], notes[1]]
    return [ChordTone(*note) for note in notes]


def getCycle(root, scaleType, cycleNum, voicing="close"):
    scale = Scale(root, scaleType)
    intMap = cycleMaps[cycleNum]["intMap"]
    funMap = cycleMaps[cycleNum]["funMap"]
    voiceLeading = VoiceLeading(scale, intMap, funMap)
    startingChord = Chord(root, getSevenToneTriad(scale, voicing))
    return voiceLeading, startingChord
