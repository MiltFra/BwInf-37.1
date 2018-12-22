#!/usr/bin/python3
import sys
from queue import Queue
from random import randint


def volldaneben(player_values):
    p = next_possibility(None)
    best_possibility = p
    best_pay = payment(player_values, p)
    p_pay = payment(player_values, p)
    sbest = f'{str(p):40} => {p_pay}'
    mc = max_count(len(player_values))
    c = 0
    while max(p) < len(player_values):
        p_pay = payment(player_values, p)
        if p_pay < best_pay:
            best_pay = p_pay
            best_possibility = p
            sbest = f'{str(p):40} => {p_pay}' 
        p = next_possibility(p)
        c += 1
        print(f'{sbest}; {100*c/mc}%         ', end='\r')
    print()
    return [player_values[x] for x in best_possibility], best_pay
def volldaneben2(player_values):
    pv = sorted(player_values)
    gaps = [(i, pv[i]-pv[i-1]) for i in range(1,len(pv))]
    gaps = sorted(gaps, key=lambda x: x[1], reverse=True)
    gaps = sorted(gaps[:10], key=lambda x: x[0])
    sections = []
    for i in range(1,len(gaps)):
        single_sect = []
        for j in range(gaps[i-1][0], gaps[i][0]):
            single_sect.append(pv[j])
        sections.append(single_sect)
    sections.append([pv[x] for x in range(gaps[-1][0], len(pv))])
    #ssections = "\n".join([str(x) for x in sections])
    #print(f'Sections:\n{ssections}')
    casino_values = [sect[len(sect)//2] for sect in sections]
    return casino_values, payment2(player_values, casino_values)

def payment2(player_values, casino_values):
    pay = 0
    for p in player_values:
        pay += min([abs(x-p) for x in casino_values])
    return pay
def max_count(x):
    c = x
    _c = 10
    for i in range(1,10):
        c *= x - i
        _c *= i
    return c / _c

def next_possibility(last_possibility):
    if last_possibility == None:
        return list(range(10))
    d = len(last_possibility)-1
    for i in range(len(last_possibility)-1):
        if last_possibility[i] + 1 < last_possibility[i+1]:
            d = i
            break    
    new = list(last_possibility)
    for i in range(d):
        new[i] = i
    new[d] += 1
    return new


def payment(player_values, possibility):
    casino_values = [player_values[x] for x in possibility]
    pay = 0
    for p in player_values:
        pay += min([abs(x-p) for x in casino_values])
    return pay


def reset_up_to(possibility, n):
    for i in range(n):
        possibility[i] = i
    return possibility


inputs = [randint(0,1000) for _ in range(20)]
with open('in.txt', 'w') as f:
    for i in inputs:
        f.write(str(i)+'\n')
with open('in.txt') as f:
    player_values = [int(x) for x in f.readlines()]
values, pay = volldaneben(player_values)
print(' '.join([str(x) for x in values]))
print(f'=> {pay}')
with open('out.txt', 'w') as f:
    f.write(str(pay)+'\n')
    for v in values:
        f.write(str(v)+'\n')
