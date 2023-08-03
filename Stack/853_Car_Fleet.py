# LC AUTO CHOOSES PYTHON INSTEAD OF PYTHON3
# I.E. INT DIVISION WON'T RETURN FLOAT

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    atom = [(pos, speed) for pos, speed in zip(position, speed)]
    stack = []
    # don't auto initally to stack, add as you move through the data
    for pos, speed in sorted(atom, reverse=True):
        stack.append((target - pos) / speed)  # time taken to reach target
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()  # works because we are working reverse order
    return len(stack)

# use if instead of while, because we move backwards in one direction (and doesn't change) !!!!!!

assert (carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3)
assert (carFleet(target=10, position=[3], speed=[3]) == 1)
assert (carFleet(target=10, position=[6, 8], speed=[3, 2]) == 2)
