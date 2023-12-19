from constants import *
import math
import itertools


def tonalDistance(a, b, intervals=True):
    if a == b:
        return 0
    low, hi = (min(a, b), max(a, b))
    result = min(hi - low, low + 12 - hi)
    if intervals:
        return math.ceil(result / 2)
    return result


class ChordTone:
    def __init__(self, pitchClass):
        self.pitchClass = pitchClass

    def __repr__(self):
        return pitch_classes[self.pitchClass]


class Chord:
    def __init__(self, scale, root, chordTones):
        self.root = root
        self.chordTones = chordTones
        self.scale = scale

    def getBestInversion(self, num):
        minDistance = math.inf
        bestPerm = None
        for perm in itertools.permutations(self.pitchClasses()):
            newPitches = list(perm)
            indices = [self.pitchClasses().index(pitch) for pitch in newPitches]
            if indices == list(range(len(newPitches))):
                continue
            for i in range(len(newPitches)):
                toneIndx = self.scale.notes.index(newPitches[i])
                newPitches[i] = self.scale.notes[(toneIndx + num) % self.scale.length]
            distance = 0
            for j in range(len(newPitches)):
                distance += tonalDistance(newPitches[j], self.pitchClasses()[j])
            if distance < minDistance:
                minDistance = distance
                bestPerm = indices
        return bestPerm

    def transpose(self, num):
        newChordTones = []
        for tone in self.chordTones:
            toneIndx = self.scale.notes.index(tone.pitchClass)
            newPitchClass = self.scale.notes[(toneIndx + num) % self.scale.length]
            newChordTones.append(ChordTone(newPitchClass))
        rootIndx = self.scale.notes.index(self.root)
        self.root = self.scale.notes[(rootIndx + num) % self.scale.length]
        self.chordTones = newChordTones

    def permute(self, indices):
        newTones = []
        for index in indices:
            newTones.append(self.chordTones[index])
        self.chordTones = newTones

    def pitchClasses(self):
        return [tone.pitchClass for tone in self.chordTones]

    def copy(self):
        return Chord(self.scale, self.root, self.chordTones)

    def __repr__(self):
        str = ""
        notes = []
        for tone in self.chordTones:
            indx = self.scale.notes.index(tone.pitchClass)
            notes.append(self.scale.noteNames[indx].ljust(2, " "))
        return " ".join(notes)


class Scale:
    def __init__(self, root, notes):
        self.root = root
        self.notes = [(note + root) % 12 for note in notes]
        self.length = len(notes)
        self.noteNames = self.addNoteNames()

    def __repr__(self):
        return str([pitch_classes[x % 12] for x in self.notes])

    def findNote(self, pitchClass):
        for i in range(len(self.notes)):
            if self.notes[i] % 12 == pitchClass:
                return i
        raise (Exception("Note not found"))

    def addNoteNames(self):
        rootName = pitch_classes[self.root][0]
        baseNoteIndx = noteNames.index(rootName)
        baseNotes = noteNames[baseNoteIndx:] + noteNames[:baseNoteIndx]
        for i in range(len(baseNotes)):
            natural = pitch_classes_rev[baseNotes[i]]
            actual = self.notes[i]
            if actual == 0 and natural == 11:
                baseNotes[i] = "B♯"
            elif actual > natural:
                if tonalDistance(actual, natural, False) == 1:
                    baseNotes[i] += "♯"
                else:
                    baseNotes[i] += "𝄪"
            elif actual < natural:
                if natural in [5, 0]:
                    baseNotes[i] = pitch_classes[(natural - 1) % 12]
                else:
                    baseNotes[i] += "♭"
            if pitch_classes_rev[baseNotes[i]] != self.notes[i]:
                print(i, actual, natural, baseNotes, self.notes)
                raise Exception("Parsing Error")
        return baseNotes
