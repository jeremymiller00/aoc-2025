""" 
Parse input into ranges

For each range
Check each value within range for validity

Store invalid ids in a list
Add them up
"""


def read_input(path: str) -> str:
    with open('./day3_input.txt') as file:
        data = file.readlines()
    return data


def parse_input(data: list[str]) -> list[list[int]]:
    return [parse_bank(d.strip()) for d in data]


def parse_bank(bank: str) -> list[int]:
    '''
    in
    '1234'
    out
    [1,2,3,4]
    '''
    return [int(b) for b in bank]
    

def switch_on(bank: list[int]) -> int:
    # part 1
    # first = max(bank[:-1])
    # idx = bank.index(first)
    # second = max(bank[idx+1:])
    # return int(first) * 10 + int(second)

    # part 2
    factor = 100000000000
    result = 0
    still_needed = 12
    while still_needed > 0:
        left_in_bank = len(bank)
        selelction_range = left_in_bank - still_needed + 1
        next_digit = max(bank[:selelction_range])
        idx = bank.index(next_digit)
        bank = bank[idx+1:]
        result += (next_digit * factor)
        factor /= 10
        still_needed -= 1

    return int(result)


def main(path: str) -> int:
    data = read_input(path)
    banks = parse_input(data)
    result =0
    for bank in banks:
        result += switch_on(bank)
    return result


def test():
    data = ["987654321111111",'811111111111119','234234234234278','818181911112111']
    # data = ["811111111111119"]
    banks = parse_input(data)
    result =0
    for bank in banks:
        result += switch_on(bank)
    return result

if __name__ == "__main__":
    print(main("./day3_input.txt"))
    # print(test())
