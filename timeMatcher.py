# Implementation of an interview question TechWithTim was given by Clement Mihailescu
# Given a list of list/tuple objects of length 2 representing time objects, write an algorithm
# that takes two lists and finds free blocks of time
# Not sure if Clement would have accepted this, but i found this implementation to be better for me
person1 = [('10:00', '10:30'), ('12:00', '12:30'), ('16:00','16:30')]
person2 =[('10:00', '10:30'),('12:30','13:00'),('14:30','15:00'), ('16:00', '16:30'), ('16:30', '17:00'), ('17:00', '17:30'), ('17:30', '18:00')]


all_slots = {('10:00','10:30'), ('10:30','11:00'), ('11:00','11:30'), ('11:30','12:00'), ('12:00','12:30'), ('12:30','13:00'), ('13:00', '13:30'),
             ('13:30','14:00'), ('14:00','14:30'), ('14:30','15:00'), ('15:00','15:30'), ('15:30','16:00'), ('16:00','16:30'),
             ('16:30','17:00'), ('17:00','17:30'), ('17:30','18:00')}


def timeMatch(times_1, times_2, all_available_slots):
    times_1_set = set(times_1)
    times_2_set = set(times_2)
    mutual_free = []
    person1_free_slots = all_available_slots.difference(times_1_set)
    person2_free_slots = all_available_slots.difference(times_2_set)
    
    mutual_free_slots = person1_free_slots.intersection(person2_free_slots)
    for i in mutual_free_slots:
        mutual_free.append(i)
    
    return mutual_free

for slot in timeMatch(person1, person2, all_slots):
    print(slot)










