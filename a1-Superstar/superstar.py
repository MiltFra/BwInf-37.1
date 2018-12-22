#!/usr/bin/python
import sys
class graph:

    def __init__(self, path):                           # reading the graph from a file
        with open(path) as f:                           # opening the file
            lines = f.readlines()                       # reading the file
            self.v = set(lines[0].rstrip('\n').split(' '))               # vertex names
            self.n = len(self.v)                        # vertex count
            self.e = set()                                # (vertex1, vertex2) --> vertex1 follows vertex2 (True/False)
            for l in [x.rstrip('\n').split(' ') for x in lines[1:]]: # vertex pairs until the end of the file
                if len(l) == 2:
                    self.e.add((l[0], l[1]))            # setting True if an entry exists
            self.price = 0                              # the graph tracks the price of the requests

    def request(self, node1, node2):                    # does node1 follow node2?
        self.price += 1    
        return (node1, node2) in self.e                 # returning the dict entry for node1 and node 2; if none is found returns False

class star_finder:                                      # Finds a "star" in a given graph; returns the price

    def __init__(self, g):                              # constructor ...
        self.g = g                                      # saving the graph
        self.links = set()                              # |g.v|x|g.v| matrix; managing the known links (0: n/a; -1: False; 1: True)
        self.candidates = g.v.copy()  # at the beginning every node is a candidate
        self.not_candidates = set()                        # at the beginning no node is not a candidate

    def request(self, node1, node2):                    # requesting node1 -> node 2 and updating sets accordingly
        r = self.g.request(node1, node2)                # r is the result of the request
        self.links.add((node1, node2))                   # updating the known links
        if r and node1 in self.candidates:         # superstars can't follow others
            self.candidates.remove(node1)               # hence the node is removed from the candidates 
            self.not_candidates.add(node1)           # into the not_candidates
        elif not r and node2 in self.candidates:      # everyone has to follow a superstar
            self.candidates.remove(node2)               # see above
            self.not_candidates.add(node2)
        print(node1, '->', node2)

    def run(self):
        while len(self.candidates) > 0:                 # if they're are no candidates left, no requests are needed
            if self.request_best():                     # if a superstar has been found, no requests are needed
                break
        print()
        print('Total cost: EUR', self.g.price)
        if len(self.candidates) > 0:
            print('Superstar found:', self.candidates.pop()) 
        else:
            print('There is no superstar in this graph!')

    def request_best(self):  
        if len(self.candidates) > 1:                    # issue the best possible request based on the current knowledge
            for i in self.candidates:                   # cycle through candidates 'til (i, j) can be requested
                for j in self.candidates:               # cycle through candidates...
                    if j != i:                          # a node can't follow itself
                        self.request(i, j)              # request the valid pair
                        return False                    # we haven't actually found something yet
        return self.check_last()                        # if there are no possible candidate -> person left, we can check the last remaining candidate

    def check_last(self):
        for c in self.candidates:
            for n in self.not_candidates:       # checking all the necessary relations
                if n != c:                               # of the last remaining candidate
                    if (n,c) not in self.links:
                        self.request(n, c)
                        return False
                    elif (c, n) not in self.links:
                        self.request(c, n)
                        return False
        return True                                     # if none is left, we've got a super star

def superstar():                                        # main function
    if len(sys.argv) < 2:                               # debug stuff; neat feature
        path = f'{"/".join(sys.argv[0].split("/")[:-1])}/beispieldaten/superstar4.txt'
    else:                                               # 99.9% of cases
        path = sys.argv[1]                              # get the path
    g = graph(path)                                     # get the graph
    sf = star_finder(g)                                 # get the star finder
    sf.run()                                            # run it; I/O is in there

if __name__ == '__main__':
    superstar()                                            
