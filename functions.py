from classes import *
import os

parent_dir = r"C:/Users/alexa/Documents/Programming/Music/goodchord/"


def generateChordFamily(cycle, root, scaleType, chordNotes, fname):
    scale = Scale(root, scaleType)
    chordTones = [ChordTone(scale.notes[x]) for x in chordNotes]
    startingChord = Chord(scale, chordTones[0].pitchClass, chordTones)
    chord = startingChord.copy()
    permutation = chord.getBestInversion(cycle - 1)
    with open(fname, "a", encoding="UTF-8") as f:
        f.write("(" + " ".join([str(x + 1) for x in chordNotes]) + ") ")
    newChordNotes = chordNotes.copy()
    for i in range(len(permutation)):
        newChordNotes[i] = chordNotes[permutation[i]]
    with open(fname, "a", encoding="UTF-8") as f:
        f.write("--> (" + " ".join([str(x + 1) for x in newChordNotes]) + ")\n")
    indx = 0
    while indx < len(chordTones) * len(scaleType):
        if indx > 0:
            with open(fname, "a", encoding="UTF-8") as f:
                f.write("Alternate Voicing:\n")
        while True:
            with open(fname, "a", encoding="UTF-8") as f:
                f.write(chord.__repr__() + "\n")
            indx += 1
            chord.transpose(cycle - 1)
            chord.permute(permutation)
            if chord.pitchClasses() == startingChord.pitchClasses():
                break
        startingChord = Chord(
            scale, chordTones[1].pitchClass, chordTones[1:] + [chordTones[0]]
        )
        chord = startingChord.copy()


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
    path = path + f"/{rootName} {scaleName}/"
    safeMakeFolder(path)
    path = path + f"/{chordType}/"
    safeMakeFolder(path)
    for cycle in range(2, 8):
        fname = path + f"Cycle {cycle}.txt"
        with open(fname, "w", encoding="UTF-8") as f:
            f.write(
                f"{rootName.capitalize()} {scaleName}, Cycle {cycle}\n"
                + "-" * 25
                + "\n"
            )
        for chordName, chord in chordVoicings.items():
            with open(fname, "a", encoding="UTF-8") as f:
                f.write(f"{chordName.capitalize()}: ")
            generateChordFamily(
                cycle, root=root, scaleType=scaleNotes, chordNotes=chord, fname=fname
            )
            with open(fname, "a", encoding="UTF-8") as f:
                f.write("-" * 25 + "\n")
