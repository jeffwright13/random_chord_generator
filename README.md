# Random Chord Generator

## Description:    
Generate a sequence of random chords and print them to console.
    
## Usage:
    rcg.py [-admM] [-f |-s] <num_chords>
    rcg.py -a | --augmented
    rcg.py -d | --diminished
    rcg.py -m | --minor
    rcg.py -M | --major
    rcg.py -f | --flats <num_chords>
    rcg.py -s | --sharps <num_chords>
    rcg.py -h | --help
    rcg.py -V | --version

## Arguments:
    num_chords      Number of chords to generate
    
## Options:
    -m --minor       Include minor chords in generated sequence
    -M --major       Include major chords in generated sequence
    -a --augmented   Include augmented chords in generated sequence
    -d --diminished  Include diminished chords in generated sequence
    -f --flats       Render chords with flats instead of sharps (default)
    -s --sharps      Render chords with sharps instead of flats
    -h --help        Show this message and exit
    -V --version     Show version info and exit


By default, the quality of the generated chords are major and minor.  Use the "--augmented" (or "-a") flag to generate augmented chords. Use the "--diminished" (or "-d") flag to generate diminished chords.

By default, accidentals are printed as flats. Use the "--sharps" (or "-s") flag to show accidentals as sharps.

### Original Author:
    davecohen

### Contributing Author:
    Jeff Wright <jeff.washcloth@gmail.com>
