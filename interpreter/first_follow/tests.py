#!/usr/bin/python3

import input as inpt
import first as fir 
import follow as fol

#
# First productions
#
test_data = [
    # Test case 1
    # Curtosey of: https://www.jambe.co.nz/UNI/FirstAndFollowSets.html
    [
        # Inputs
        {
            "E" : [False, False, ["TR", "terminals"]],
            "R" : [False, False, ["+TR", "@"]],
            "T" : [False, False, ["FY"]],
            "Y" : [False, False, ["*FY", "@"]],
            "F" : [False, False, ["(E)", "id"]],
        },
        # Expected output
        {
            'E': {
                'terminals': {'(', 'i', 't'}, 
                'compounds': {'T'}}, 
            'T': {
                'terminals': {'(', 'i'}, 
                'compounds': {'F'}}, 
            'F': {
                'terminals': {'(', 'i'}, 
                'compounds': set()}, 
            'R': {
                'terminals': {'+', '@'},
                'compounds': set()}, 
            'Y': {
                'terminals': {'*', '@'}, 
                'compounds': set()}
        }
    ],

    # Test case 2
    # curtosey of: https://www.youtube.com/watch?v=62hxbNeLfrk
    [
        {
            'H': [False, False, ['KLp', 'gSK']], 
            'K': [False, False, ['bLST', '@']], 
            'L': [False, False, ['SaK', 'SK', 'qa']],
            'S': [False, False, ['ds', '@']], 
            'T': [False, False, ['gHf', 'm']]
        },
        # Expected output
        {
            'H': {
                'terminals': {'q', 'b', 'a', 'p', 'g', 'd'}, 
                'compounds': {'K', 'L'}}, 
            'K': {'terminals': {'@', 'b'},
                'compounds': set()}, 
            'L': {'terminals': {'@', 'a', 'q', 'b', 'd'}, 
                'compounds': {'S', 'K'}}, 
            'S': {'terminals': {'@', 'd'}, 
                'compounds': set()},
            'T': {'terminals': {'g', 'm'}, 
                'compounds': set()}
        }

    ]
]

#
# Test first set
#
def test_first_set():
    for i in test_data:
        first = fir.calculate_first_set(i[0])
        print(first)
        assert first == i[1]

#
# Test follow set
#
def test_follow_set():
    for i in test_data:
        follow = fol.follow(i[0])
        print(follow)

#
# Main
#
def main():
    test_first_set()
    test_follow_set()

#
# Module check
#
if __name__ == "__main__":
    main()
