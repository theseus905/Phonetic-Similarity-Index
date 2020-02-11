# -*- coding: utf-8 -*-
from enum import Enum
from math import hypot
from typing import NamedTuple
from dataclasses import dataclass
import numpy as np
# from lazy import *


# make a word class
# has a syllabify function

# Enumeration of
class Place(Enum):
    Bilabial = 0
    Labial = 1
    Dental = 2
    Alveolar = 3
    PostAlveolar = 4
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
    Occlusive = 0
    Nasal = 1
    Plosive = 2
    Affricate = 3
    Strident = 4
    Sibilant = 5
    Obstruent = 6
    Fricative = 7
    Continuant = 8
    Vocoid = 9
    Vowel = 10
    Approximant = 11
    Semivowel = 12
    Rhotic = 13
    Lateral = 14
    Liquid = 15
    Vibrant = 16
    Flap = 17
    Trill = 18

@dataclass
class Vowel():
    formant1: int
    formant2: int

@dataclass
class Consonant():
    phoneme: str # Phoneme.phoneme
    place: int # Phoneme.Place
    manner: int # Phoneme.Manner
    voiced: bool # Phoneme.Voiced

class Phoneme():
    def __init__(self, phoneme):
        self.allophone = phoneme

    def is_vowel(self) -> bool:
        """ Checks if phoneme is a vowel """
        return self.allophone in VOWELS

    @staticmethod
    def build_phoneme_feature(manners: list) -> list:
        """ """
        embedded_manners = [0] * len(Manner)
        for manner in manners:
            embedded_manners[manner.value] = 1
        return embedded_manners

    # @lazy
    def set_consonant(self, place: int, manners: list, voiced: bool):
        embedded_manners = Phoneme.build_phoneme_feature(manners)
        return Consonant(self.allophone, place, embedded_manners, voiced)

    # @lazy
    def set_vowel(self):
        return VOWELS[self.allophone]

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
    "p" : (Place.Bilabial, [Manner.Obstruent, Manner.Plosive, Manner.Occlusive], False),
    "b" : (Place.Bilabial, [Manner.Obstruent, Manner.Plosive, Manner.Occlusive], True),
    "m" : (Place.Bilabial, [Manner.Nasal, Manner.Occlusive], True),

    "ʃ" : (Place.PostAlveolar, [Manner.Sibilant, Manner.Strident, Manner.Obstruent,
                                Manner.Fricative, Manner.Continuant], False),
    "ʒ" : (Place.PostAlveolar, [Manner.Sibilant, Manner.Strident, Manner.Obstruent,
                                Manner.Fricative, Manner.Continuant], True),

    "t" : (Place.Alveolar, [Manner.Plosive, Manner.Obstruent, Manner.Occlusive], False),
    "d" : (Place.Alveolar, [Manner.Plosive, Manner.Obstruent, Manner.Occlusive], True),
    "n" : (Place.Alveolar, [Manner.Nasal, Manner.Occlusive], True),

    "s" : (Place.Alveolar, [Manner.Sibilant, Manner.Strident, Manner.Obstruent,
                            Manner.Fricative, Manner.Continuant], False),
    "z" : (Place.Alveolar, [Manner.Sibilant, Manner.Strident, Manner.Obstruent,
                            Manner.Fricative, Manner.Continuant], True),

    "ɾ" : (Place.Alveolar, [Manner.Flap, Manner.Vibrant, Manner.Rhotic,
                            Manner.Liquid], False),

    "ɹ" : (Place.Alveolar, [Manner.Vocoid, Manner.Rhotic, Manner.Liquid,
                            Manner.Approximant, Manner.Continuant], False),
    "l" : (Place.Alveolar, [Manner.Lateral, Manner.Continuant, Manner.Approximant,
                            Manner.Liquid, Manner.Vocoid], False),

    "k" : (Place.Velar, [Manner.Obstruent, Manner.Plosive, Manner.Occlusive], False),
    "g" : (Place.Velar, [Manner.Obstruent, Manner.Plosive, Manner.Occlusive], True),
    "ŋ" : (Place.Velar, [Manner.Nasal, Manner.Occlusive], False),

    "f" : (Place.Labial, [Manner.Strident, Manner.Obstruent, Manner.Fricative,
                          Manner.Continuant], False),
    "v" : (Place.Labial, [Manner.Strident, Manner.Obstruent, Manner.Fricative,
                          Manner.Continuant], True),

    "θ" : (Place.Dental, [Manner.Obstruent, Manner.Fricative, Manner.Continuant], False),
    "ð" : (Place.Dental, [Manner.Obstruent, Manner.Fricative, Manner.Continuant], True),
    #
    "h" : (Place.Glottal, [Manner.Fricative, Manner.Continuant, Manner.Obstruent], False),
    "ʔ" : (Place.Glottal, [Manner.Plosive, Manner.Occlusive, Manner.Obstruent], False),
    #
    "w" : (Place.Velar, [Manner.Approximant, Manner.Semivowel, Manner.Continuant,
                         Manner.Vocoid], True),
    "j" : (Place.Palatal, [Manner.Approximant, Manner.Semivowel, Manner.Continuant,
                           Manner.Vocoid], True),
    #
    "tʃ" : (Place.Alveolar, [Manner.Affricate, Manner.Sibilant, Manner.Strident,
                             Manner.Occlusive, Manner.Obstruent], False),
    "dʒ" : (Place.Alveolar, [Manner.Affricate, Manner.Sibilant, Manner.Strident,
                             Manner.Occlusive, Manner.Obstruent], True),
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

# consonantal_distance("d", "p")
# print(vocalic_distance("o","ɛ"))

x = Phoneme("p")
y = x.set_consonant(*CONSONANTS["p"])
print(repr(y.place))
