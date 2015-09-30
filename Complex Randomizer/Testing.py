__author__ = 'Joshua Zosky'

'''
import RandNoRep as rnr

import random

a = range(100)
print a
b = rnr.random_no_replacement(a)
print a
print b

people = range(5)
women = list(people)
men = list(people)
emotion = ['happy', 'sad']

list_a = rnr.random_no_replacement(women)
list_a += rnr.random_no_replacement(men)
'''
'''
import popfaces as pf


def face_list():
    person_list = []
    for face_number in range(5):
        person = pf.Person()
        person.face = face_number + 1
        person_list.append(person)
        print person_list[face_number].face
    return person_list

def gender_list(person_list, gender):
    temp_list = list(person_list)
    for person in temp_list:
        person.gender = gender
        print person.gender
    return temp_list

pl = face_list()
pl_female = gender_list(pl, 'female')
pl_male = gender_list(pl, 'male')
print pl_female
print pl_male
'''
"""
import popfaces as pf
import RandNoRep as rnr

counter = 0

def face(number):
    person = pf.Person()
    person.face = number + 1
    return person


def gender(gender_mf):
    g_list = []
    for j in range(5):
        person = face(j)
        person.gender = gender_mf
        g_list.append(person)
    return g_list

def emotion(emotion):
    e_list = []
    for i in range(2):
        if i == 0:
            person_list = gender('male')
        else:
            person_list = gender('female')
        for person in person_list:
            person.emotion = emotion
            e_list.append(person)
    return e_list

def congruent(contiguity):
    c_list = []
    for i in range(2):
        if i == 0:
            person_list = emotion('happy')
        else:
            person_list = emotion('sad')
        for person in person_list:
            person.contiguous = contiguity
            c_list.append(person)
    return c_list

def create_list():
    cont_list = congruent(True)
    noncont_list = congruent(False)
    total_list = cont_list + noncont_list
    for i in total_list:
        i.who_is_this()
    print len(total_list)
    return total_list

def jumble(count):
    count += 1
    lister = create_list()
    print lister
    a = rnr.random_no_replacement(lister)
    temp = None
    for i in range(len(a)):
        if i > 0:
            if a[i].face == temp.face:
                if a[i].gender == temp.gender:
                    if a[i].emotion == temp.emotion:
                        print "broken"
                        a = jumble(count)
                        return a
        # a[i].who_is_this()
        temp = a[i]
    print 'yay, this took %s tries' % count
    return a

print jumble(counter)
"""
import random as ran

def check_list(in_list):
    temp_list = list(in_list)
    ran.shuffle(temp_list)
    lookback_list = []
    cc = 0
    ci = 0
    ic = 0
    ii = 0
    for i in range(len(temp_list) - 1):
        combo = list((temp_list[i], temp_list[i + 1]))
        print combo
        if combo == ['C', 'C']:
            cc += 1
            if cc > 10 and i < 39:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
        elif combo == ['C', 'I']:
            ci += 1
            if ci > 10 and i < 39:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
        elif combo == ['I', 'C']:
            ic += 1
            if ic > 10 and i < 39:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
        elif combo == ['I', 'I']:
            ii += 1
            if ii > 10 and i < 39:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
        else:
            print "ERRRORORORS"
            return i
        #lookback_list.append(temp_list.pop(0))
        #print lookback_list
    #out_list = list(lookback_list)
    out_list = [cc,ci,ic,ii]
    return out_list

congruent_list = (['C'] * 21) + (['I'] * 20)
print congruent_list
# ran.shuffle(congruent_list)
print congruent_list
print check_list(congruent_list)