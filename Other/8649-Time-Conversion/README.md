# Time Conversion

## Problem

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.

- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

Return '12:01:00'.

Return '00:01:00'.

Function Description

Complete the  function with the following parameter(s):

: a time in  hour format

Returns

: the time in  hour format

Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid

Sample Input 0

07:05:45PM

Sample Output 0

19:05:45

Change Theme

LanguageC++20

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

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

1

2

string timeConversion(string s) {
string period = s.substr(s.length() - 2);  // "AM" or "PM"
int hh = stoi(s.substr(0, 2));
string rest = s.substr(2, s.length() - 4);  // ":MM:SS"

if(period == "AM"){
if(hh == 12) hh = 0;
} else {
if(hh != 12) hh += 12;
}

string hourStr = (hh < 10) ? "0" + to_string(hh) : to_string(hh);

return hourStr + rest;
}

int main(){
string s;
cin >> s;

string result = timeConversion(s);
cout << result << endl;

return 0;
}
#include <bits/stdc++.h>
using namespace std;

Line: 28 Col: 2

Test against custom input

You have earned 15.00 points!
You are now 55 points away from the 2nd star for your problem solving badge.

21%45/100

CongratulationsYou solved this challenge. Would you like to challenge your friends?

Next Challenge

Compiler Message
Success

Input (stdin)
07:05:45PM

Expected Output
19:05:45

Author
vatsalchanana

Difficulty
Easy

Max Score
15

Submitted By
1236142

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

[Time Conversion](https://www.hackerrank.com/challenges/time-conversion/problem)
