from classes import *
from constants import *
from functions import *
import itertools

if __name__ == "__main__":
    for root, scale, voicing in itertools.product(
        range(12),
        [major, harmo, melod],
        [triadVoicings, seventhVoicings, triadBNIVoicings, triadBNIIVoicings],
    ):
        print(root, scale["name"], voicing["name"])
        write_files(root, scale, voicing)
