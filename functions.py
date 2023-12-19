from classes import *
import os

parent_dir = r"C:/Users/alexa/Documents/Programming/Music/goodchord/"


def generateChordFamily(cycle, root, scaleType, chord, fname):
    scale = Scale(root, scaleType)
    chordTones = [ChordTone(scale.notes[x]) for x in chord]
    startingChord = Chord(scale, chordTones[0].pitchClass, chordTones)
    chord = startingChord.copy()
    permutation = chord.getBestInversion(cycle - 1)
    while True:
        with open(fname, "a") as f:
            f.write(chord.__repr__() + "\n")
        chord.transpose(cycle - 1)
        chord.permute(permutation)
        if chord.pitchClasses() == startingChord.pitchClasses():
            break


def safeMakeFolder(path):
    try:
        os.mkdir(path)
    except OSError as error:
        return


def write_files(root, scaleType, chordVoicings):
    scaleName = scaleType["name"]
    scaleNotes = scaleType["notes"]
    rootName = pitch_classes[root]
    chordType = chordVoicings["name"]
    chordVoicings = chordVoicings["voicings"]
    path = os.path.join(parent_dir, "Chord Families")
    safeMakeFolder(path)
    path = path + f"/{rootName}/"
    safeMakeFolder(path)
    path = path + f"/{scaleName}/"
    safeMakeFolder(path)
    path = path + f"/{chordType}/"
    safeMakeFolder(path)
    for chordName, chord in chordVoicings.items():
        for cycle in range(2, 8):
            safeMakeFolder(path + f"cycle_{cycle}/")
            fname = path + f"cycle_{cycle}/{chordName}.txt"
            with open(fname, "w") as f:
                f.write(
                    f"{rootName.capitalize()} {scaleName}, Cycle {cycle}, {chordName} Voicing\n"
                )
            generateChordFamily(
                cycle, root=root, scaleType=scaleNotes, chord=chord, fname=fname
            )
