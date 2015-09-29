__author__ = 'Joshua Zosky'

import random


class Person():

    def __init__(self):
        self.gender = 'female'
        self.face = 1
        self.emotion = 'happy'
        self.congruent = True

    def who_is_this(self):
        print "gender = %s" % self.gender
        print "face = %s" % self.face
        print "emotion = %s" % self.emotion
        print "congruent = %s" % self.congruent
