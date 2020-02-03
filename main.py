# -*- coding: utf-8 -*-
from math import hypot
from typing import NamedTuple
from enum import Enum
import numpy as np
import lazy

# make a word class
# has a syllabify function

# Enumeration of
class Place(Enum):
    Bilabial = 1
    Labial = 2
    Dental = 3
    Alveolar = 4
    Retroflex = 5
    Palatal = 6
    Velar = 7
    Uvular = 8
    Pharyngeal = 9
    Glottal = 10

class Manner(Enum):
    """
    0 : Occlusives  1 : Nasals      2 : Plosives   3 : Affricates  4 : Stridents
    5 : Sibilants   6 : Obstruents  7 : Fricatives 8 : Continuants 9 : Vocoids

    10 : Vowels   11 : Approximants  12 : Semivowels  13 : Rhotics 14 : Laterals
    15 : Liquids  16 : Vibrants      17 : Flaps       18 : Trills
    """
    Occlusive = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nasal = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Plosive = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Affricate = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Strident = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Sibilant = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Obstruent = np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Fricative = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Continuant = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Vocoid = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Vowel = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    Approximant = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    Semivowel = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    Rhotic = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    Lateral = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    Liquid = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    Vibrant = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    Flap = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
    Trill = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    @lazy
    def get_manner(self, consonant: str):
        return ""

class Vowel(NamedTuple):
    formant1: int
    formant2: int

class Consonant(NamedTuple):
    place: int # Phoneme.Place
    manner: int # Phoneme.Manner
    voiced: bool # Phoneme.Voiced

class Phoneme():
    def __init__(self, phoneme: str):
        self.allophone = phoneme
        self.phoneme = self.set_vowel() if self.is_vowel() else self.set_consonant()

    def is_vowel(self):
        return self.allophone in VOWELS

    def build_phoneme_feature(self):
        pass

    @lazy
    def set_consonant(self, place, voiced):
        Consonant(place, voiced)
        return self.phoneme

    @lazy
    def set_vowel(self):
        return self.phoneme

# do an enum on string for place

# A mapping of vowel to F1,  F2
VOWELS = {
    "i" : Vowel(280, 2350),
    "ɪ" : Vowel(360, 2220),
    "e" : Vowel(450, 2150),
    "æ" : Vowel(800, 1760),
    "ʌ" : Vowel(760, 1320),
    "ɑ" : Vowel(750, 1180),
    "ɛ" : Vowel(575, 1880),
    "ɒ" : Vowel(560, 920),
    "ɔ" : Vowel(480, 760),
    "ʊ" : Vowel(380, 940),
    "u" : Vowel(320, 920),
    "o" : Vowel(400, 750),
}

CONSONANTS = {
    "p" : Consonant(Place.Bilabial, Manner.get_manner, False),
    "b" : Consonant(Place.Bilabial, Manner.get_manner, True),
    "m" : Consonant(Place.Bilabial, Manner.get_manner, True),

    "ʃ" : Consonant(Place.Alveolar, Manner.get_manner, False),
    "ʒ" : Consonant(Place.Alveolar, Manner.get_manner, True),
    "t" : Consonant(Place.Alveolar, Manner.get_manner, False),
    "d" : Consonant(Place.Alveolar, Manner.get_manner, True),
    "n" : Consonant(Place.Alveolar, Manner.get_manner, True),
    "s" : Consonant(Place.Alveolar, Manner.get_manner, False),
    "z" : Consonant(Place.Alveolar, Manner.get_manner, True),
    "ɾ" : Consonant(Place.Alveolar, Manner.get_manner, False),
    "ɹ" : Consonant(Place.Alveolar, Manner.get_manner, False),
    "l" : Consonant(Place.Alveolar, Manner.get_manner, False),

    "k" : Consonant(Place.Velar, Manner.Plosive, False),
    "g" : Consonant(Place.Velar, Manner.Plosive, True),
    "ŋ" : Consonant(Place.Velar, Manner.Nasal, False),


    "f" : Consonant(Place.Labial, Manner.Fricative, False),
    "v" : Consonant(Place.Labial, Manner.Fricative, True),

    "θ" : Consonant(Place.Dental, Manner.Fricative, False),
    "ð" : Consonant(Place.Dental, Manner.Fricative, True),

    "h" : Consonant(Place.Glottal, Manner.Fricative, False),
    "ʔ" : Consonant(Place.Glottal, Manner.Plosive, False),

    "w" : Consonant(Place.Velar, Manner.Approximant, True),
    "j" : Consonant(Place.Palatal, Manner.Approximant, False),

    "tʃ" : Consonant(Place.Alveolar, Manner.Affricate, False),
    "dʒ" : Consonant(Place.Alveolar, Manner.Affricate, True),
}


def vocalic_distance(vowel1: str, vowel2: str):
    vowel1 = VOWELS[vowel1]
    vowel2 = VOWELS[vowel2]
    return hypot(vowel1.formant1 - vowel2.formant1,
                 vowel1.formant2 - vowel2.formant2)

def consonantal_distance(consonant1: str, consonant2: str):
    print(repr(CONSONANTS[consonant1].place))
    print(CONSONANTS[consonant1].manner)
    print(CONSONANTS[consonant1].manner.value)

def build_dimensional_features():
    """
    this is meant to build dimensional feature
    """
    return 1

consonantal_distance("d", "p")
# print(vocalic_distance("o","ɛ"))
