from classes import *


def generateChordFamily(cycle, root, scaleType, chord, fname):
    scale = Scale(root, scaleType)
    chordTones = [ChordTone(scale.notes[x]) for x in chord]
    startingChord = Chord(scale, 0, chordTones)
    chord = startingChord.copy()
    permutation = chord.getBestInversion(cycle - 1)
    while True:
        with open(fname, "a") as f:
            f.write(chord.__repr__() + "\n")
        chord.transpose(cycle - 1)
        chord.permute(permutation)
        if chord.pitchClasses() == startingChord.pitchClasses():
            break


def write_files(root, scaleType, chordVoicings):
    scaleName = scaleType["name"]
    scaleNotes = scaleType["notes"]
    rootName = pitch_classes[root]
    for chordName, chord in chordVoicings.items():
        for cycle in range(2, 8):
            fname = f"{rootName}_{scaleName}_cycle_{cycle}_{chordName}.txt"
            with open(fname, "w") as f:
                f.write(
                    f"{rootName.capitalize()} Major, Cycle {cycle}, {chordName} Voicing\n"
                )
            generateChordFamily(
                cycle, root=root, scaleType=scaleNotes, chord=chord, fname=fname
            )
