""" All tasks come from www.codewars.com """

"""
TASK: The Lift

Synopsis
A multi-floor building has a Lift in it.
People are queued on different floors waiting for the Lift.
Some people want to go up. Some people want to go down.
The floor they want to go to is represented by a number (i.e. when they enter the Lift this is the button they will press)
  
1. Rules

1.1 Lift Rules
- The Lift only goes up or down!
- Each floor has both UP and DOWN Lift-call buttons (except top and ground floors which have only DOWN and UP respectively)
- The Lift never changes direction until there are no more people wanting to get on/off in the direction it is already travelling
- When empty the Lift tries to be smart. For example,
    - If it was going up then it may continue up to collect the highest floor person wanting to go down
    - If it was going down then it may continue down to collect the lowest floor person wanting to go up
- The Lift has a maximum capacity of people
- When called, the Lift will stop at a floor even if it is full, although unless somebody gets off nobody else can get on!
- If the lift is empty, and no people are waiting, then it will return to the ground floor

1.2 People Rules
- People are in "queues" that represent their order of arrival to wait for the Lift
- All people can press the UP/DOWN Lift-call buttons
- Only people going the same direction as the Lift may enter it
- Entry is according to the "queue" order, but those unable to enter do not block those behind them that can
- If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has departed without them

Kata Task
- Get all the people to the floors they want to go to while obeying the Lift rules and the People rules
- Return a list of all floors that the Lift stopped at (in the order visited!)

NOTE: The Lift always starts on the ground floor (and people waiting on the ground floor may enter immediately)

I/O
Input
- queues a list of queues of people for all floors of the building.
    - The height of the building varies
    - 0 = the ground floor
    - Not all floors have queues
    - Queue index [0] is the "head" of the queue
    - Numbers indicate which floor the person wants go to
- capacity maximum number of people allowed in the lift

Parameter validation - All input parameters can be assumed OK. No need to check for things like:

- People wanting to go to floors that do not exist
- People wanting to take the Lift to the floor they are already on
- Buildings with < 2 floors
- Basements

Output
- A list of all floors that the Lift stopped at (in the order visited!)
"""


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(person) for person in queues]
        self.capacity = capacity

    def theLift(self):
        visited_floors = [0]
        elevator = []

        people_waiting = True

        while people_waiting:
            people_waiting = False

            # Going up
            for floor in range(0, len(self.queues)):
                stop_at_floor = False

                for person in elevator[:]:
                    if person == floor:
                        elevator.remove(person)
                        stop_at_floor = True

                for person in self.queues[floor][:]:
                    if person > floor:
                        stop_at_floor = True
                        if self.capacity > len(elevator):
                            elevator.append(person)
                            self.queues[floor].remove(person)
                        else:
                            people_waiting = True

                if stop_at_floor and not visited_floors[-1] == floor:
                    visited_floors.append(floor)

            # Going down
            for floor in range(len(self.queues) -1, -1, -1):
                stop_at_floor = False

                for person in elevator[:]:
                    if person == floor:
                        elevator.remove(person)
                        stop_at_floor = True

                for person in self.queues[floor][:]:
                    if person < floor:
                        stop_at_floor = True

                        if self.capacity > len(elevator):
                            elevator.append(person)
                            self.queues[floor].remove(person)
                        else:
                            people_waiting = True

                if stop_at_floor and not visited_floors[-1] == floor:
                    visited_floors.append(floor)

        if visited_floors[-1] != 0:
            visited_floors.append(0)

        return visited_floors
