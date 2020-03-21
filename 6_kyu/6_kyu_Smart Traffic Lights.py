""" All tasks come from www.codewars.com """

"""
TASK: Smart Traffic Lights

Your friend Bob is working as a taxi driver. After working for a month he is frustrated in the city's traffic lights. 
He asks you to write a program for a new type of traffic light. 
It is made so it turns green for the road with the most congestion.

Example: There are 42 cars waiting on 27th ave. There are 72 cars waiting on 3rd st. 
Since there are more cars on 3rd st, the light turn green for that street.

You don't need to worry about the process of detecting cars yet.

How your program will be tested:

Python:
t = SmartTrafficLight([42, '27th ave'], [72, '3rd st'])
t.turngreen()
#-> '3rd st'
t.turngreen() #Assuming all the cars on 3rd st are gone
#-> '27th ave'
t.turngreen() #Assuming all the cars on both streets are gone
#-> None (if both streets have an equal amount of cars)
"""

class SmartTrafficLight():
    def __init__(self, st1, st2):
        self.streets = sorted([st1, st2])

    def turngreen(self):
        if self.streets:
            return self.streets.pop()[1]


# class SmartTrafficLight():
#     def __init__(self, st1, st2):
    #     self.st1 = st1
    #     self.st2 = st2

    # def turngreen(self):
        # if self.st1[0] > self.st2[0]:
        #     self.st1[0] = 0
        #     return self.st1[1]
        # elif self.st1[0] < self.st2[0]:
        #     self.st2[0] = 0
        #     return self.st2[1]


# PyCharm terminal tests
t = SmartTrafficLight([42, '27th ave'], [72, '3rd st'])
print(t.turngreen()) # 3rd st
print(t.turngreen()) # 27th ave
print(t.turngreen()) # None


b = SmartTrafficLight([92, '27th ave'], [72, '3rd st'])
print(b.turngreen()) # 27th ave
print(b.turngreen()) # 3rd st
print(b.turngreen()) # None
