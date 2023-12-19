major = {"name": "Major", "notes": [0, 2, 4, 5, 7, 9, 11]}
melod = {"name": "Melodic Minor", "notes": [0, 2, 3, 5, 7, 9, 11]}
harmo = {"name": "Harmonic Minor", "notes": [0, 2, 3, 5, 7, 8, 11]}

pitch_classes = {
    0: "C",
    1: "C#",
    2: "D",
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B",
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
