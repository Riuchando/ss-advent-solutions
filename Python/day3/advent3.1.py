#!/usr/bin/python3
"""
Solves the first problem in the third pair of advent of code problems
Copyright 2015 Steven Sheffey

    This file is part of ss-advent-solutions

    ss-advent-solutions is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ss-advent-solutions is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ss-advent-solutions.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys

data = sys.stdin.read()

x=0
y=0

visitedHouses=set()
visitedHouses.add((0,0))

for instruction in data:
    if instruction == '>':
        x+=1
    elif instruction == '<':
        x-=1
    elif instruction == '^':
        y+=1
    else:
        y-=1
    visitedHouses.add((x,y))

print(len(visitedHouses))

