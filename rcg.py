"""
Description:
    rcg.py:
    Random Chord Generator
    Generate a sequence of random chords and print them to console.

Usage:
    rcg.py [-ad] [-f | -s] <num_chords>
    rcg.py -a | --augmented
    rcg.py -d | --diminished
    rcg.py -f | --flats <num_chords>
    rcg.py -s | --sharps <num_chords>
    rcg.py -h | --help
    rcg.py -V | --version

Arguments:
    num_chords      Number of chords to generate

Options:
    -a --augmented   Include augmented chords in generated sequence
    -d --diminished  Include diminished chords in generated sequence
    -f --flats       Render chords with flats instead of sharps (default)
    -s --sharps      Render chords with sharps instead of flats
    -h --help        Show this message and exit
    -V --version     Show version info and exit

Original Author:
    davecohen

Contributing Author:
    Jeff Wright <jeff.washcloth@gmail.com>
"""
import random
from docopt import docopt


def chords(num_chords, sharps_or_flats="flats", aug=False, dim=False):
    ch_root = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
    ]

    ch_quality = ["", "m"]
    ch_quality.append("dim") if dim else None
    ch_quality.append("+") if aug else None
    ch_prog = "| "

    for x in range(num_chords):
        rand_root = random.sample(ch_root, 1)
        rand_quality = random.choice(ch_quality)
        ch_prog += str(rand_root[0] + rand_quality + " | ")
    if sharps_or_flats == "sharps":
        print("\t" + ch_prog)
    elif sharps_or_flats == "flats":
        ch_prog = ch_prog.replace("C#", "Db")
        ch_prog = ch_prog.replace("D#", "Eb")
        ch_prog = ch_prog.replace("F#", "Gb")
        ch_prog = ch_prog.replace("G#", "Ab")
        ch_prog = ch_prog.replace("A#", "Bb")
        print("\t" + ch_prog)
    else:
        raise ValueError("Illegal value for sharps_or_flats: ", sharps_or_flats)


def main():
    args = docopt(__doc__, version="1.1.1")
    sharps_or_flats = "sharps" if args["--sharps"] else "flats"
    chords(
        int(args["<num_chords>"]),
        sharps_or_flats,
        args["--augmented"],
        args["--diminished"],
    )


if __name__ == "__main__":
    main()
