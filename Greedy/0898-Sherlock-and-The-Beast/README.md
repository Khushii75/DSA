# Sherlock and The Beast

## Problem

Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus.  He also gives him a clue:  an integer. Sherlock determines the key to removing the virus is to find the largest Decent Number having that number of digits.

A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.

The number of 3's it contains is divisible by 5.

The number of 5's it contains is divisible by 3.

It is the largest such number for its length.

Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

For example, the numbers  and  are both decent numbers because there are  's and  's in the first, and  's in the second.  They are the largest values for those length numbers that have proper divisibility of digit occurrences.

Function Description

Complete the decentNumber function in the editor below.

decentNumber has the following parameter(s):

int n: the length of the decent number to create

Prints

Print the decent number for the given length, or  if a decent number of that length cannot be formed. No return value is expected.

Input Format

The first line is an integer, , the number of test cases.

The next  lines each contain an integer , the number of digits in the number to create.

Constraints

Sample Input

STDIN   Function
-----   --------
4       t = 4
1       n = 1 (first test case)
3       n = 3 (second test case)
5
11

Sample Output

-1
555
33333
55555533333

Explanation

For , there is no Decent Number having  digit, so print .

For ,  is the only possible number. (Decent Number Property 3).

For ,  is the only possible number. (Decent Number Property 2).

For ,  is the Decent Number.  All other permutations of these digits are not decent (Decent Number Property 4).

Change Theme

LanguageC++20

1

2

3

4

5

6

7

8

9

10

11

12

#include <bits/stdc++.h>
using namespace std;
int main() {
int t; cin >> t;
while (t--) {
int n; cin >> n;
int fives = n;
while (fives % 3 != 0) fives -= 5;
if (fives < 0) cout << -1 << "\n";
else cout << string(fives, '5') + string(n - fives, '3') << "\n";
}
}

Line: 12 Col: 2

Test against custom input

Loading testcase ...

Author
amititkgp

Difficulty
Easy

Max Score
30

Submitted By
96435

Need Help?
View discussions
View editorial
View top submissions

RESOURCES
Div Mod
Greedy Technique

rate this challenge

MORE DETAILS
Download problem statement
Download sample test cases
Suggest Edits

## Problem Link

[Sherlock and The Beast](https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem)
