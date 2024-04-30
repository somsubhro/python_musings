# Python musings
## Trying out stuff

In this project I try out stuff and share my learning. This is a basic Python project. No installation necessary. Nothing fancy. 

## NumberOfBillsAndCoins

**The problem discussed in this directory is:**
Given a sum of money compute the minimum number of bills and coins that equal that sum.
Assume you only have the following denominations:
Bills: 20, 10, 5, 1,
Coins: .25, .1, .05, .01.
For example, given 6.35 the solution would be One 5, One 1, One .25, One .1.


> [`minimumNumberOfBillsAndCoins.py`](https://github.com/somsubhro/python_musings/blob/main/NumberOfBillsAndCoins/minimumNumberOfBillsAndCoins.py) file shows how **not to** implement this. 

This is the most brute force implementation. This implementation has several problems: 
* The bills and coins denomination is a fixed array.
* Each position of the array is tightly coupled in code logic.
* Implementation of the dictionary can be arguably better.
* Does not conform to human understanding of bills and coins because the `target_sum` variable's default data type being binary floating point.
