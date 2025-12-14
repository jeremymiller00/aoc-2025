""" 
Parse input into ranges

For each range
Check each value within range for validity

Store invalid ids in a list
Add them up
"""


def read_input(path: str) -> str:
    with open('./day2_input.txt') as file:
        data = file.read()
    return data


def parse_input(data: str) -> list[int]:
    # return a list of all ids to check
    invalid_ids = []
    raw_ranges = data.split(",")
    ranges = [r.split("-") for r in raw_ranges]
    range_objects = [range(int(r[0]), int(r[1])+1) for r in ranges]
    for ro in range_objects:
        for i in ro:
            # dont add if not symmetrical as a string
            if is_invalid(i):
                invalid_ids.append(i)
    return invalid_ids


def is_invalid(product_id: int) -> bool:
    # part one: id is a sequence repeated twice
    # s = str(product_id)
    # if not len(s) % 2 == 0:
    #     return False
    # middle = int(len(s)/2)
    # a, b = s[:middle], s[middle:]
    # if a == b:
    #     return True
    # return False

    # part two: id is a sequence repeated N times
    s = str(product_id)
    l = len(s)
    if l % 2 == 0:
        middle = int(l/2)
        a, b = s[:middle], s[middle:]
        if a == b:
            return True

    factor = 3
    while factor <= l:
        if l % factor == 0:
            candidates = []
            # take that many characters until none left
            temp_s = s
            candidate_size = int(l / factor)
            while len(temp_s) > 0:
                candidates.append(temp_s[:candidate_size])
                temp_s = temp_s[candidate_size:]
            # check if they are all the same
            if candidates.count(candidates[0]) == len(candidates):
                return True
            else:
                factor += 2
        else:
            factor += 2


def main(path: str) -> int:
    data = read_input(path)
    ids = parse_input(data)
    return sum(ids)


def test():
    data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # data = "2121212118-2121212124"
    ids = parse_input(data)
    return sum(ids)


if __name__ == "__main__":
    print(main("./day2_input.txt"))
    # print(test())
