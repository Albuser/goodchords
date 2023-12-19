from constants import *
import math
import itertools


def tonalDistance(a, b):
    if a == b:
        return 0
    low, hi = (min(a, b), max(a, b))
    return math.ceil(min(hi - low, low + 12 - hi) / 2)


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
        for tone in self.chordTones:
            str += (tone.__repr__()).ljust(3, " ")
        return str


class Scale:
    def __init__(self, root, notes):
        self.root = root
        self.notes = [(note + root) % 12 for note in notes]
        self.length = len(notes)

    def __repr__(self):
        return str([pitch_classes[x % 12] for x in self.notes])

    def findNote(self, pitchClass):
        for i in range(len(self.notes)):
            if self.notes[i] % 12 == pitchClass:
                return i
        raise (Exception("Note not found"))
