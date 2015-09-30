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
import random as ran
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

def emotion(emotions):
    e_list = []
    for i in range(2):
        if i == 0:
            person_list = gender('male')
        else:
            person_list = gender('female')
        for person in person_list:
            person.emotion = emotions
            e_list.append(person)
    return e_list

def congruent(congruency):
    c_list = []
    for i in range(2):
        if i == 0:
            person_list = emotion('happy')
        else:
            person_list = emotion('sad')
        for person in person_list:
            person.congruent = congruency
            c_list.append(person)
    return c_list

def create_list():
    cong_list = congruent(True)
    noncong_list = congruent(False)
    total_list = cong_list + noncong_list
    # for i in total_list:
    #     i.who_is_this()
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

person_list = jumble(counter)


def check_list(in_list):
    temp_list = list(in_list)
    ran.shuffle(temp_list)
    lookback_list = []
    cc = 0
    ci = 0
    ic = 0
    ii = 0
    for i in range(len(temp_list) - 1):
        temp_list, cc, ci, ic, ii, i = combo_check(temp_list, cc, ci, ic, ii, i)
        if i == 100:
            return check_list(temp_list)
    out_list = [cc,ci,ic,ii]
    if out_list != [10, 10, 10, 10]:
        return check_list(temp_list)
    return out_list, temp_list


def combo_check(temp_list, cc, ci, ic, ii, i):
    combo = list((temp_list[i], temp_list[i + 1]))
    if combo == [True, True]:
        cc += 1
        if cc > 10:
            if i < 40:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
                cc -= 1
                combo_check(temp_list, cc, ci, ic, ii, i)
                return temp_list, cc, ci, ic, ii, i
            else:
                i = 100
    elif combo == [True, False]:
        ci += 1
        if ci > 10:
            if i < 40:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
                ci -= 1
                combo_check(temp_list, cc, ci, ic, ii, i)
                return temp_list, cc, ci, ic, ii, i
            else:
                i = 100
    elif combo == [False, True]:
        ic += 1
        if ic > 10:
            if i < 40:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
                ic -= 1
                combo_check(temp_list, cc, ci, ic, ii, i)
                return temp_list, cc, ci, ic, ii, i
            else:
                i = 100
    elif combo == [False, False]:
        ii += 1
        if ii > 10:
            if i < 40:
                move_item = temp_list.pop(i+1)
                temp_list.append(move_item)
                ii -= 1
                combo_check(temp_list, cc, ci, ic, ii, i)
                return temp_list, cc, ci, ic, ii, i
            else:
                i = 100
    else:
        print "ERRRORORORS"
        return i
    return temp_list, cc, ci, ic, ii, i

congruent_list = ([True] * 21) + ([False] * 20)
tries = 0
while True:
    try:
        tries += 1
        ch_list, con_list = check_list(congruent_list)
        print 'This took %s tries' % tries
        break
    except:
        pass
print ch_list
print con_list

i = 0
for person in person_list:
    person.congruent = con_list[i]
    i += 1
f = []
for person in person_list:
    f.append(person.congruent)
print f