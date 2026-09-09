# GCD of Two

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Light Mode
99+

Menu

Back to Explore Page

Ask A DoubtMy Doubts

FREQUENTLY ASKED QUESTIONS

ProblemEditorialSubmissionsComments

GCD of Two
Solved

Difficulty: BasicAccuracy: 51.03%Submissions: 241K+Points: 1

Given two positive integers a and b, find GCD of a and b.

Note: Don't use the inbuilt gcd function

Examples:

Input: a = 20, b = 28
Output: 4
Explanation: GCD of 20 and 28 is 4

Input: a = 60, b = 36
Output: 12
Explanation: GCD of 60 and 36 is 12

Constraints:
1 ≤ a, b ≤ 109

Expected Complexities

Time Complexity: O(log(min(a, b)))
Auxiliary Space: O(1)

Company Tags

AccentureTCS

Topic Tags

Mathematics

Related Articles

Gcd In CppProgram To Find Gcd Or Hcf Of Two Numbers

Discussions ( 263 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sylvester3 days agoSep 06, 2026 04:57 (GMT +5:30)

class Solution:
def gcd(self, a, b):
# code here
if b == 0:
return a
return self.gcd(b, a % b)

0

Reply

Sylvester3 days agoSep 06, 2026 04:54 (GMT +5:30)

/**
* @param number a
* @param number b
* @returns number
*/

class Solution {
gcd(a, b) {
// code here
if(b == 0){
return a;
}

return this.gcd(b, a % b);
}
}

0

Reply

MADHAVI PORTE1 week agoAug 27, 2026 12:41 (GMT +5:30)

while (b != 0) {
int rem = a % b;
a = b;
b = rem;
}
return a;

0

Reply

Sindhureddy2 weeks agoAug 26, 2026 20:16 (GMT +5:30)

class Solution {
public static int gcd(int a, int b) {
// code here
while(a>0 && b>0){
if(a>b){
a = a%b;
}
else{
b= b%a;
}
}
if(a==0) return b;
return a;
}
}

2

Reply

Sankeerthana2 weeks agoAug 26, 2026 15:09 (GMT +5:30)

class Solution {
public static int gcd(int a, int b) {
// code here
while(b!=0){
int temp=b;
b=a%b;
a=temp;
}
return a;

}
}

1

Reply

Thejas Bj3 weeks agoAug 17, 2026 15:29 (GMT +5:30)

class Solution:
def gcd(self, n1, n2):

if n1 == 0:
return n2

if n1 < n2:
n1, n2 = n2, n1

return self.gcd(n1 % n2, n2)

0

Reply

Anonymous_Geek1 month agoAug 07, 2026 15:34 (GMT +5:30)

c++

0

Reply

Ayush Mishra1 month agoJul 31, 2026 23:27 (GMT +5:30)

class Solution {
public static int gcd(int a, int b) {
// code here
if(b==0){
return a;
}
return gcd(b, a%b);
}
}

0

Reply

Balaji Vinothkumar3 months agoJun 09, 2026 21:07 (GMT +5:30)

class Solution {
public static int gcd(int a, int b) {
while(b !=0)
{
int temp = b;

b = a % b;

a = temp;
}
return a;

}
}

0

Reply

Ranu3 months agoMay 16, 2026 08:11 (GMT +5:30)

class Solution {
public static int gcd(int a, int b) {
// code here
while(a > 0 && b > 0){
if(a > b)   a = a - b;
else b = b - a;
}
return a;
}
}

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:151

Time Taken0.04

Python3
C (gcc 5.4)
C++ (17)
Java (21)
Python3
C#
Javascript (Node v22)

Editor Settings
Font Size
Theme

Choose Your Preferred font For The Code Editor
12px13px14px15px16px18px20px22px

1
2
3
4
5
6
7
8

class Solution:
def gcd(self, a, b):
# code here
while b!=0:
temp=a%b
a=b
b=temp
return a

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:151

Time Taken0.04

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[GCD of Two](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)
