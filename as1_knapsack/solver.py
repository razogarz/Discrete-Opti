#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

from solving_funcs import recursion_solve, check_taken

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    """
    PARSE DATA
    """
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    """
    SOLUTION
    """

    solving_func = recursion_solve
    taken_i, value, weight = solving_func(items, 0, capacity)
    taken = [0]*len(items)
    for i in taken_i:
        taken[i] = 1

    """
    OUTPUT
    """
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        """
        CHANGE FUNCTION
        """
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

