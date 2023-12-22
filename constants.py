major = {"name": "Major", "notes": [0, 2, 4, 5, 7, 9, 11]}
melod = {"name": "Melodic Minor", "notes": [0, 2, 3, 5, 7, 9, 11]}
harmo = {"name": "Harmonic Minor", "notes": [0, 2, 3, 5, 7, 8, 11]}

allScales = [major, melod, harmo]

noteNames = ["C", "D", "E", "F", "G", "A", "B"]

pitch_classes = {
    0: "C",
    1: "C♯",
    2: "D",
    3: "D♯",
    4: "E",
    5: "F",
    6: "F♯",
    7: "G",
    8: "G♯",
    9: "A",
    10: "A♯",
    11: "B",
}

pitch_classes_rev = {
    "C": 0,
    "C♯": 1,
    "C𝄪": 2,
    "D♭": 1,
    "D": 2,
    "D♯": 3,
    "E♭": 3,
    "E": 4,
    "E♯": 5,
    "F": 5,
    "F♯": 6,
    "F𝄪": 7,
    "G♭": 6,
    "G": 7,
    "G♯": 8,
    "G𝄪": 9,
    "A♭": 8,
    "A": 9,
    "A♯": 10,
    "B♭": 10,
    "B": 11,
    "B♯": 0,
}

triadVoicings = {
    "name": "Triads",
    "voicings": {"close": [0, 2, 4], "spread": [0, 4, 2]},
}

seventhVoicings = {
    "name": "Sevenths",
    "voicings": {
        "4-way close": [0, 2, 4, 6],
        "drop 2": [0, 4, 6, 2],
        "drop 3": [0, 6, 2, 4],
        "drop 2 and 3": [0, 2, 6, 4],
        "drop 2 and 4": [0, 4, 2, 6],
        "double drop 2 drop 3": [0, 6, 4, 2],
    },
}

triadBNIVoicings = {
    "name": "Triad Over BN I",
    "voicings": {
        "4-way close": [0, 1, 4, 6],
        "drop 2": [0, 4, 6, 1],
        "drop 3": [0, 6, 1, 4],
        "drop 2 and 3": [0, 1, 6, 4],
        "drop 2 and 4": [0, 4, 1, 6],
        "double drop 2 drop 3": [0, 6, 4, 1],
    },
}

triadBNIIVoicings = {
    "name": "Triad Over BN II",
    "voicings": {
        "4-way close": [0, 1, 3, 6],
        "drop 2": [0, 3, 6, 1],
        "drop 3": [0, 6, 1, 3],
        "drop 2 and 3": [0, 1, 6, 3],
        "drop 2 and 4": [0, 3, 1, 6],
        "double drop 2 drop 3": [0, 6, 3, 1],
    },
}

fourPartFourths = {
    "name": "Four Part Fourths",
    "voicings": {
        "4-way close": [0, 2, 3, 6],
        "drop 2": [0, 3, 6, 2],
        "drop 3": [0, 6, 2, 3],
        "drop 2 and 3": [0, 2, 6, 3],
        "drop 2 and 4": [0, 3, 2, 6],
        "double drop 2 drop 3": [0, 6, 3, 2],
    },
}

spreadClusters = {
    "name": "Spread Clusters",
    "voicings": {
        "4-way close": [0, 1, 2, 6],
        "drop 2": [0, 2, 6, 1],
        "drop 3": [0, 6, 1, 2],
        "drop 2 and 3": [0, 1, 6, 2],
        "drop 2 and 4": [0, 2, 1, 6],
        "double drop 2 drop 3": [0, 6, 2, 1],
    },
}


threePartFourths = {
    "name": "Three Part Fourths",
    "voicings": {"close": [1, 4, 0], "spread": [0, 4, 1]},
}


allChordFamilies = [
    triadVoicings,
    threePartFourths,
    seventhVoicings,
    triadBNIVoicings,
    triadBNIIVoicings,
    fourPartFourths,
    spreadClusters,
]

chordNames = {
    (0, 3, 7): "m",
    (0, 4, 7): "M",
    (0, 4, 7, 11): "M7",
    (0, 3, 7, 10): "m7",
    (0, 4, 7, 10): "7",
    (0, 4, 8): "+",
    (0, 3, 6, 10): "ø",
    (0, 3, 6, 9): "°",
    (0, 3, 6): "dim",
    (0, 1, 6): "dim(sus(m2))",
    (0, 5, 7): "sus4",
    (0, 2, 7): "sus2",
    (0, 1, 7): "sus(m2)",
    (0, 2, 4, 7): "2",
    (0, 4, 5, 7): "4",
    (0, 4, 7, 9): "6",
    (0, 3, 7, 11): "m(maj7)",
    (0, 4, 8, 11): "aug(maj7)",
}
