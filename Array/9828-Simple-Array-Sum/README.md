# Simple Array Sum

## Problem

Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

Function Description

Complete the  function with the following parameter(s):

: an array of integers

Returns

: the sum of the array elements

Input Format

The first line contains an integer, , denoting the size of the array.

The second line contains  space-separated integers representing the array's elements.

Constraints

Sample Input

STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]

Sample Output

31

Explanation

Print the sum of the array's elements: .

Change Theme

LanguagePython 3

1

2

3

4

5

6

def simpleArraySum(ar):
return sum(ar)

n = int(input())
ar = list(map(int, input().split()))
print(simpleArraySum(ar))

Line: 6 Col: 26

Test against custom input

CongratulationsYou solved this challenge. Would you like to challenge your friends?

Next Challenge

Loading testcase ...

Author
shashank21j

Difficulty
Easy

Max Score
10

Submitted By
3021035

Need Help?
View discussions
View editorial
View top submissions

rate this challenge

MORE DETAILS
Download problem statement
Download sample test cases
Suggest Edits

## Problem Link

[Simple Array Sum](https://www.hackerrank.com/challenges/simple-array-sum/problem)
