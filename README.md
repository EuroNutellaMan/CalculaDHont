# CalculaD'Hont
A simple calculator to assign seats from an election based on the D'Hont method.

## How it works ##
First it will prompt you to insert a maximum number of parties, their name and what their electoral result is.
After that it will ask how many seats need to be assigned, then it will do the following loop untill all seats are assigned:
1) Find the biggest value among the electoral results
2) Memorize its position
3) Add 1 seat to the party in that position
4) Divide that party's electoral result by 2
5) Repeat

## Requirements ##
1) Python 3.11.3 onwards
2) Colorama module for python

## How to use ##
1) Download the file and save it wherever you like
2) Run from a terminal using ```python /path/to/calculadhont.py``` (note: use ```python3 ...``` on Windows)

Browser version coming soon<sup>tm</sup>
