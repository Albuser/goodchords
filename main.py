from classes import *
from constants import *
from functions import *
import itertools

if __name__ == "__main__":
    for root, myScale in itertools.product(range(12), [major, harmo, melod]):
        scale = Scale(root, myScale["notes"])
        print(
            (pitch_classes[root] + " " + myScale["name"] + ": ").ljust(20, " "),
            ", ".join(scale.noteNames),
        )
    for root, scale, voicing in itertools.product(
        range(12),
        [major, harmo, melod],
        [triadVoicings, seventhVoicings, triadBNIVoicings, triadBNIIVoicings],
    ):
        print(root, scale["name"], voicing["name"])
        write_files(root, scale, voicing)
