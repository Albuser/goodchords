from constants import *


class ChordTone:
    def __init__(self, function, pitchClass):
        self.function = function
        self.pitchClass = pitchClass

    def __repr__(self):
        return pitch_classes[self.pitchClass]


class VoiceLeading:
    def __init__(self, scale, intMapping, funMapping):
        # Interval Mapping should look like '{"5": -1', ... } (descending second)
        # Function Mapping should look like '{"5": "3", ... } (cycle 2, Triad)
        self.scale = scale
        self.intervalMapping = intMapping
        self.functionMapping = funMapping

    def transpose(self, chordTone: ChordTone):
        newFun = self.functionMapping[chordTone.function]
        curNoteIndx = self.scale.findNote(chordTone.pitchClass)
        newNoteIndx = (curNoteIndx + self.intervalMapping[chordTone.function]) % len(
            self.scale.notes
        )
        newPitchClass = self.scale.notes[newNoteIndx]
        return ChordTone(newFun, newPitchClass)


class Chord:
    def __init__(self, root, chordTones):
        self.root = root
        self.chordTones = chordTones

    def transpose(self, voiceLeading):
        newChordTones = [voiceLeading.transpose(tone) for tone in self.chordTones]
        isRoot = [tone.function == "1" for tone in newChordTones]
        rootIndx = isRoot.index(True)
        newRoot = pitch_classes[newChordTones[rootIndx].pitchClass]
        return Chord(newRoot, newChordTones)

    def pitchClasses(self):
        return [tone.pitchClass for tone in self.chordTones]

    def __repr__(self):
        str = ""
        for tone in self.chordTones:
            str += (tone.__repr__()).ljust(3, " ")
        return str


class Scale:
    def __init__(self, root, notes):
        self.root = root
        self.notes = [note + root for note in notes]

    def __repr__(self):
        return str([pitch_classes[x % 12] for x in self.notes])

    def findNote(self, pitchClass):
        for i in range(len(self.notes)):
            if self.notes[i] % 12 == pitchClass:
                return i
        raise (Exception("Note not found"))
