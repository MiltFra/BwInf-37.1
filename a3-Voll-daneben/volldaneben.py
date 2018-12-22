#!/usr/bin/python
import sys
import queue


# The main class to solve the problem; just for some parameters to be pseudo global
class volldaneben_solver:

    # constructor ...
    def __init__(self, inputs):
        # sorting inputs for the algorithm to work
        self.inputs = sorted(inputs)
        # getting prices for intervals [a, b] with exactly one pick
        self.set_segment_prices()
        # getting prices for intervals [1, b] with two to ten picks
        self.set_combined_prices()
        # setting self.values to the actual values
        self.set_values()

    # see self.__init__
    def set_segment_prices(self):
        # just shorter code
        inp = self.inputs
        # just shorter code
        l = len(inp)
        # (start, end) --> (price, pick)
        self.segment_prices = {}
        # cycling the end of the interval in [0, l)
        for b in range(l):
            # cycling the beginning of the interval in [0, b); a <= b!
            for a in range(b+1):
                self.segment_prices[(a, b)] = (
                    self.segment_price(inp[a:b+1]), (a+b)//2)                       # getting the price and writing it into the dictionary

    # calculates the minimal cost of a given segment with one pick
    def segment_price(self, segment):
        # optimization & readability
        pick = segment[len(segment) // 2]
        # the price is the sum of deltas of each element of the segment to the pick
        return sum([abs(x - pick) for x in segment])

    # see self.__init__
    def set_combined_prices(self):
        # readability
        inp = self.inputs
        # readability
        l = len(inp)
        # (pick count, end) --> (price, previous end)
        self.combined_prices = {}
        # setting the prices of segments with one pick
        for b in range(l):
            self.combined_prices[(1, b)] = (self.segment_prices[(0, b)][0], 0)
        # [1, 9] (i) ^= [2, 10] (i') picks
        for i in range(1, 10):
            # the end can't be less than i, 'cause there are i picks already
            for b in range(i, l):
                # the beginning of the single pick interval at the end of the combined one
                for a in range(i-1, b):
                    # combinded prices without the single pick segment [a, b]
                    prev = self.combined_prices.get((i, a-1), (0, a))
                    # total price is the previous price + the single segment price
                    price = prev[0] + self.segment_prices[(a, b)][0]
                    # there might have been a previous calculation; the current best
                    best = self.combined_prices.get((i+1, b), (sys.maxsize, 0))
                    # the new price is only relevant if it's actually lower than the old one
                    if best[0] > price:
                        # if so, updated the current best for [1, b] with i' picks
                        self.combined_prices[(i+1, b)] = (price, a)
        # the acutal price is the very last one
        self.price = self.combined_prices[(10, l-1)]

    # setting the picks from the self.combined_prices
    def set_values(self):
        # a list of picks ... (indices)
        picks = []
        # track [1, b]
        b = len(self.inputs)-1
        # each consecutive combined segment has one less pick
        for i in range(10, 0, -1):
            # get the data for the current segment
            current = self.combined_prices[(i, b)]
            # append the pick of the intervall [new b + 1, b] to picks
            picks.append(self.segment_prices[(current[1], b)][1])
            # the new end of the remaining interval
            b = current[1]-1
        # indices --> values
        self.picks = [self.inputs[x] for x in picks]


# I/O: reading inputs from file
def from_file(path):
    inputs = []
    with open(path) as f:
        l = f.readline().strip('\n')
        while l != '':
            inputs.append(int(l))
            l = f.readline().strip('\n')
    return inputs


# I/O: reading inputs from input stream; < - opeartor
def from_input():
    inputs = []
    l = input()
    while l != '':
        inputs.append(int(l))
        l = input()
    return inputs


# main method; solve the problem and generate outputs
def volldaneben():
    # if no path is given, read input
    if len(sys.argv) == 1:
        inputs = from_input()
    else:                                                                           # if a path is given, read file
        inputs = from_file(sys.argv[1])
    # solve the problem
    solver = volldaneben_solver(inputs)
    print('Inputs: ', solver.inputs)
    # price output
    print('Price:', solver.price[0])
    # picks output
    print('Picks:', solver.picks)
    # validating price from inputs and picks
    actual_price = get_price(solver.inputs, solver.picks)
    if solver.price[0] != actual_price:
        print('WARNING: Invalid output!')
        print('Actual price:', actual_price)


# calculating the price according to the task from inputs and picks
def get_price(inputs, picks):
    # price: sum of minimal differences of each input to any pick
    return sum([min([abs(i-p) for p in picks]) for i in inputs])


# calling the main function ...
if __name__ == '__main__':
    volldaneben()
