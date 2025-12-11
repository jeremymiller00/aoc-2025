# https://adventofcode.com/2025/day/1


class Safe():
    def __init__(self, passing=False):
        self.current_dial_location = 50
        self.passing_zeros = 0
        self.passing = passing
    
    def turn_dial(self, turn: str):
        direction = turn[0]
        steps = int(turn[1:])
        if direction == "R":
            if not self.passing:
                new_location = self.current_dial_location + steps % 100
            elif self.passing:
                new_location = self.current_dial_location
                for i in range(steps):
                    new_location += 1
                    if new_location > 99:
                        new_location -= 100
                    if new_location == 0:
                        self.passing_zeros += 1

        elif direction == "L":
            if not self.passing:
                new_location = self.current_dial_location - steps % 100
                if new_location < 0:
                    new_location += 100
            elif self.passing:
                new_location = self.current_dial_location
                for i in range(steps):
                    new_location -= 1
                    if new_location < 0:
                        new_location += 100
                    if new_location == 0:
                        self.passing_zeros += 1
        
        self.current_dial_location = new_location % 100
        return

    def is_zero(self):
        return self.current_dial_location == 0


def count_zeros(passing=False):
    with open("./day1_input.txt") as file:
        raw_turn_sequence = file.readlines()
    turn_sequence = [x.strip() for x in raw_turn_sequence]

    zeros = 0
    safe = Safe()
    for t in turn_sequence:
        safe.turn_dial(t)
        if safe.is_zero():
            zeros += 1
    
    if passing:
        return safe.passing_zeros  # + zeros
    else:
        return zeros


def test():
    turn_sequence = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    safe = Safe()
    for t in turn_sequence:
        safe.turn_dial(t)
        # print(safe.current_dial_location)
    
    print(safe.passing_zeros)


if __name__ == "__main__":
    print(count_zeros(passing=True))
    # test()
