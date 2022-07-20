""" https://adventofcode.com/2021/day/8 """

from typing import List


def solve_malfunction(patterns: List[str], output=List[str]) -> List[int]:
    mapping_letters = {}
    mapping_numbers = {}

    # Easy numbers first
    mapping_numbers['8'] = 'abcdefg'  # for completeness
    mapping_numbers['1'] = [
        pattern for pattern in patterns if len(pattern) == 2][0]
    mapping_numbers['4'] = [
        pattern for pattern in patterns if len(pattern) == 4][0]
    mapping_numbers['7'] = [
        pattern for pattern in patterns if len(pattern) == 3][0]
    mapping_letters['a'] = (set(mapping_numbers['7']) -
                            set(mapping_numbers['1'])).pop()

    mapping_numbers['2'] = find_2(patterns, mapping_numbers['1'])
    mapping_numbers['6'] = find_6(
        [pattern for pattern in patterns if len(pattern) == 6], mapping_numbers['1'])
    mapping_numbers['3'] = find_3([pattern for pattern in patterns if len(
        pattern) == 5], mapping_numbers['1'] + mapping_letters['a'])
    mapping_numbers['5'] = find_5([pattern for pattern in patterns if len(
        pattern) == 5], mapping_numbers['2'], mapping_numbers['3'])
    mapping_numbers['9'] = find_9([pattern for pattern in patterns if len(
        pattern) == 6], mapping_numbers['6'], mapping_numbers['1'], mapping_numbers['4'])
    mapping_numbers['0'] = find_0([pattern for pattern in patterns if len(
        pattern) == 6], mapping_numbers['6'], mapping_numbers['9'])

    numbers = []
    for pattern in output:
        numbers.append(list(mapping_numbers.keys())[
                       list(mapping_numbers.values()).index(pattern)])

    return numbers


def find_2(patterns: List[str], one: str) -> str:
    """ 2 is the only display without the F, which is either letter of 1 (CF in original display)"""
    options = [pattern for pattern in patterns if one[0] not in pattern]
    if len(options) == 2:  # There are 2 displays without a C, so this is the wrong selection
        return [pattern for pattern in patterns if one[1] not in pattern][0]
    else:
        return options[0]


def find_6(options: List[str], one: str) -> str:
    """ 6 is the only 6-segment display that does not contain CF (both in the display for 1). """
    for option in options:
        if not all([char in option for char in one]):
            return option


def find_3(options: List[str], required_letters: str) -> str:
    """ 3 is the only display with length 5 that (in the original display) contains ACF. """
    for option in options:
        if all([x in option for x in required_letters]):
            return option


def find_9(options: List[str], six: str, one: str, four: str) -> str:
    """ There are 3 displays of length 6: 0, 6 and 9.
        We can find the difference between the 0-segments and 9-segments,
        by finding which one of them has both B and D (to be found by 4 - 1). """

    options.remove(six)
    for letter in one:
        four.replace(letter, '')  # BCDF -> BD

    for option in options:
        # 0: ABCEFG, 9: ABCDFG (contains BD).
        if all([char in option for char in four]):
            return option


def find_0(options: List[str], six: str, nine: str) -> str:
    """ There are 3 displays of length 6: 0, 6 and 9.
        We know the patterns for 6 and 9, so 0 remains. """
    options.remove(six)
    options.remove(nine)
    return options[0]


def find_5(options: List[str], two: str, three: str) -> str:
    """ There are 3 displays of length 5: 2, 3 and 5.
        We know the patterns for 2 and 3, so 5 remains. """

    options.remove(two)
    options.remove(three)
    return options[0]


def recognize_patterns(signals: List[tuple]) -> List[int]:
    """ For each 10-pattern set, calculate the correct wire/segment combinations.
        Returns the 4 (corrected) displayed digits of each record. """
    results = []
    for patterns, displays in signals:
        results.append(solve_malfunction(patterns, displays))

    return results


def first_star(signals: List) -> int:
    solved_displays = recognize_patterns(signals)
    count = 0
    for display in solved_displays:
        count += len([x for x in display if x in ['1', '4', '7', '8']])

    return count


def second_star(signals: List) -> int:
    count = 0
    solved_displays = recognize_patterns(signals)
    for display in solved_displays:
        count += int(''.join(display))
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        records = f.readlines()
        combinations = []
        for record in records:
            line = []
            for element in record.strip().split('|'):
                line.append([''.join(sorted(x)) for x in element.split(' ') if x])
            # Remove the 8-pattern for easier analysis of other displays
            line[0].remove('abcdefg')
            combinations.append(tuple(line))

        print('Star 1: ' + str(first_star(combinations)))
        print('Star 2 ' + str(second_star(combinations)))
