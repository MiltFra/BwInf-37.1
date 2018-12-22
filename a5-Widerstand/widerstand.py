#!/usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
import sys
from pathlib import Path


class Resistor():                                        # basic resistor; base part or template

    def __init__(self, value):                           # just setting the necessary values
        self.value = value
        self.parts = [value, ]

    def __str__(self):
        # string representation for later
        return str(self.value)

    def get_structure(self):
        return str(self.value)

    def get_value(self):
        # get_value() as method for the other kinds of resistors has to work here as well
        return self.value

    def draw(self, dctx, fnt, x1, y1, x2, y2, xr, yr):
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        dctx.line((x1, center[1], center[0]-xr//2, center[1]), fill=(0, 0, 0, 255))
        dctx.line((center[0]+xr//2, center[1], x2, center[1]), fill=(0, 0, 0, 255))
        dctx.rectangle((center[0]-xr//2, center[1]-yr//2, center[0] +
                        xr//2, center[1]+yr//2), outline=(0, 0, 0, 255), fill=(0, 100, 200, 255))
        t = str(self.get_value()) + ' Ohm'
        ts = dctx.textsize(t)
        dctx.text((center[0]-ts[0]//2, center[1]-ts[1]//2), t, fill=(0, 0, 0, 255))


class ParallelResistor():

    # save values as above, part1 and part2 are only for internal use
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
        self.parts = self.part1.parts + self.part2.parts  # parts lists are getting added

    def get_value(self):                                 # value is defined as 1/r = 1/r1 + 1/r2
        return (self.part1.get_value()
                * self.part2.get_value()) \
            / (self.part1.get_value()
               + self.part2.get_value())                # <=> r = (r1 * r2)/(r1 + r2)

    def draw(self, dctx, fnt, x1, y1, x2, y2, xr, yr):
        margin = xr // 3
        lc = (x1, (y1 + y2) // 2)       # center, left
        lm = (x1+margin, lc[1])         # center of margin, left
        llc = (lm[0], lm[1]+(y2-y1)//4)  # lower corner, left
        luc = (lm[0], lm[1]-(y2-y1)//4)  # upper corner, left
        rc = (x2, lc[1])                # center, right
        rm = (x2-margin, rc[1])         # center of margin, right
        rlc = (rm[0], rc[1]+(y2-y1)//4)  # lower corner, right
        ruc = (rm[0], rc[1]-(y2-y1)//4)  # upper corner, right
        dctx.line((lc, lm), fill=(0, 0, 0, 255))
        dctx.line((rc, rm), fill=(0, 0, 0, 255))
        dctx.line((llc, luc), fill=(0, 0, 0, 255))
        dctx.line((rlc, ruc), fill=(0, 0, 0, 255))
        self.part1.draw(dctx, fnt, x1+margin,
                        y1, x2-margin, (y1+y2)//2, xr, yr)
        self.part2.draw(dctx, fnt, x1+margin,
                        (y1+y2)//2, x2-margin, y2, xr, yr)

    def get_structure(self):
        return f'par({self.part1.get_structure()}, {self.part2.get_structure()})'

    def __str__(self):
        return f'{self.get_value():>10.4f}: {self.get_structure()}'

# basically the same as above...


class SequentialResistor():

    def __init__(self, part1, part2):
        self.set_parts(part1, part2)
        self.parts = self.part1.parts + self.part2.parts

    def set_parts(self, p, q):
        if p.get_value() > q.get_value():
            self.set_parts(q, p)
        self.part1 = p
        self.part2 = q

    def draw(self, dctx, fnt, x1, y1, x2, y2, xr, yr):
        self.part1.draw(dctx, fnt, x1, y1, (x1+x2)//2, y2, xr, yr)
        self.part2.draw(dctx, fnt, (x1+x2)//2, y1, x2, y2, xr, yr)

    def get_value(self):
        return self.part1.get_value() + self.part2.get_value()

    def get_structure(self):
        return f'seq({self.part1.get_structure()}, {self.part2.get_structure()})'

    def __str__(self):
        return f'{self.get_value():>10.4f}: {self.get_structure()}'


class ResistorFinder:

    def __init__(self, max_parts, parts, img_path=str(Path.home())):
        # constant to define how many resistors can be combined
        self.k = max_parts
        self.img_path = img_path
        # initiates the base parts
        self.set_base_parts(parts)
        # calculates all the combined parts
        self.set_combined_parts(self.k)
        self.combined_parts = [sorted(self.combined_parts[i], key=lambda x: x.get_value(
        )) for i in range(len(self.combined_parts))]

    def set_base_parts(self, parts):
        # Dictionary with integer values -> counts objects
        self.base_parts = Counter()
        # [[resistors l=0], [resitors l=1], ...] with l as length
        self.combined_parts = [[], ]
        for p in parts:                                         # Adding all the parts to the
            self.base_parts[p] = self.base_parts.get(p, 0) + 1  # base parts Counter
            # and the first 'combined' parts list
            self.combined_parts[0].append(Resistor(p))

    def get(self, value, max_k=4):
        best_by_k = []
        parts = []
        for i, p in enumerate(self.combined_parts):
            parts.extend(p)
            parts = sorted(parts, key=lambda x: x.get_value())
            a, b = 0, len(parts)-1
            while a + 1 != b:
                c = (a + b) // 2
                c_value = parts[c].get_value()
                if c_value > value:
                    b = c
                elif c_value < value:
                    a = c
                else:
                    break
            if a + 1 == b:
                if abs(value-parts[a].get_value()) < abs(value-parts[b].get_value()):
                    best_by_k.append(parts[a])
                else:
                    best_by_k.append(parts[b])
            else:
                for j in range(i, len(self.combined_parts)):
                    best_by_k.append(parts[c])
                break
        for i, r in enumerate(best_by_k):
            draw_resistor(r, f'output/r{value}-k{i+1}')
        with open(f'output/r{value}.txt', 'w') as f:
            for i, r in enumerate(best_by_k):
                f.write(f'k={i+1}: {r}\n')
        return best_by_k

    def set_combined_parts(self, k):
        print(f'Finding for k={k}')
        # setting combined parts until length k => recursive
        cb = self.combined_parts
        if k < 2:                                               # can't combine with only one part, right?
            return
        # Recursion: Calculating all the combined_parts([2; k-1])
        if len(cb) < k - 1:
            self.set_combined_parts(k - 1)
        # generating all possible candidates; might be discarded
        candidates = []
        count = 0
        max_count = sum([len(cb[i-1]) * len(cb[k-i-1]) for i in range(1, k//2+1)])
        # all possibilities of l + l' = k with l <= l' and l, l' >= 1 and in N
        for l in range(1, k // 2 + 1):
            # same procedure as above, just not that much of a candidate yet
            sub_candidates = []
            for p1 in cb[l-1]:                 # going through the first list (for l)
                # going through the second list (for l')
                for p2 in cb[k-l-1]:
                    # creating all possible parallel resistors
                    par = ParallelResistor(p1, p2)
                    # checking if any base part has been used too often
                    if self.base_parts_available(par):
                        sub_candidates.append(par)
                    # see parallel, same here
                    seq = SequentialResistor(p1, p2)
                    if self.base_parts_available(seq):
                        sub_candidates.append(seq)
                    count += 1
                    print(f'{count/max_count*100:.1f} %', end='\r')
            # removing any possible duplicates
            self.remove_duplicates(sub_candidates)
            candidates.extend(sub_candidates)
        # doing it again, better safe than sorry
        self.remove_duplicates(candidates)
        cb.append(candidates)
        print(f'Found all for k={k}')
        # for p in candidates:
        #    print(str(p))

    def remove_duplicates(self, resistors):
        resistors = sorted(resistors,
                           key=lambda x: x.get_value())  # sorting them for better performance later
        l = 0
        # stepping through all the resistors while being able to alter the list
        while l + 1 < len(resistors):
            # duplicates appear after each other, bc sorted
            a = resistors[l]
            b = resistors[l+1]
            if a.get_value() == b.get_value() and a.parts == b.parts:
                # remove duplicates, who would have thought?
                resistors.pop(l + 1)
            else:                                               # not duplicate => go on
                l += 1

    def base_parts_available(self, resistor):
        c = Counter(resistor.parts)                             # simple conversion
        for key in c.keys():                                    # checking if any part was used more than it actually exists
            if c[key] > self.base_parts.get(key, 0):
                return False                                    # if that's the case, return true
        return True                                             # if not, return false


def draw_resistor(r, path):
    width, height = 800, 600
    im = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    dctx = ImageDraw.Draw(im)
    fnt = ImageFont.truetype('font/FreeMono.ttf')
    r.draw(dctx, fnt, 0, 0, width, height,
           width//9, width//27)
    dctx.text((10, 10), 'R = ' + str(r.get_value()) + ' Ohm', fill=(0, 0, 0, 255))
    im.save(path+'.png')


def widerstand():
    path = 'bwinf37-runde1/a5-Widerstand/beispieldaten/test'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    with open(path) as f:
        parts = [float(x) for x in f.readlines()]
    print(parts)
    rf = ResistorFinder(4, parts)
    while True:
        v = float(input('R: '))
        print('----------------')
        options = rf.get(v)
        for i, r in enumerate(options):
            print(f'k={i+1}: {r}')
        print('----------------')


if __name__ == '__main__':
    widerstand()
