# 1 to n Without Loops

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

1 to n Without Loops
Solved

Difficulty: BasicAccuracy: 47.21%Submissions: 436K+Points: 1

Given an positive integer n, print numbers from 1 to n without using loops.
Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.
Examples

Input: n = 5
Output: 1 2 3 4 5
Explanation: We have to print numbers from 1 to 5.
Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Explanation: We have to print numbers from 1 to 10.

Constraints:
1 ≤ n ≤ 1000

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(n)

Topic Tags

Recursion

Related Articles

How Will You Print Numbers From 1 To 200 Without Using LoopOutput Of C Program Set 18 3Print 1 To N Without Using LoopsPrint Numbers 1 N Using Indirect Recursion

Discussions ( 226 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Samir Singh1 day agoSep 09, 2026 20:59 (GMT +5:30)

class Solution {
public void printTillN(int n) {
if(n != 0){
printTillN(n-1);
System.out.print(n + " ");
}

}

public static void main(String[] args){
Solution soln = new Solution();
soln.printTillN(10);

}

}

1

Reply

Sai Varun3 days agoSep 07, 2026 13:29 (GMT +5:30)

#Python Programs
-> Using Recursion(Python Code)
class Solution:
def printTillN(self, n):
if n==0:
return
self.printTillN(n-1)
print(n,end=" ")

Python Programs

0

Reply

Sylvester1 week agoSep 03, 2026 17:12 (GMT +5:30)

class Solution {

printTillN(n) {

// code here

if (n == 0) {

return;

}

this.printTillN(n - 1);

process.stdout.write(n + " ");

}

}

0

Reply

Sylvester1 week agoSep 03, 2026 17:12 (GMT +5:30)

class Solution:
def printTillN(self, n):
#code here
if n == 0:
return

self.printTillN(n -1)
print(n, end=" ")

0

Reply

Ritik kumar Pandit2 weeks agoAug 27, 2026 22:20 (GMT +5:30)

simple java ----> class Solution {
public void printTillN(int n) {
// code here
if(n!=0){
printTillN(n-1);
System.out.print(n + " ");
}
}
}

2

Reply

MADHAVI PORTE2 weeks agoAug 27, 2026 12:23 (GMT +5:30)

// code here
if(n==0){
return;
}
printTillN(n - 1);
System.out.print(n + " ");

0

Reply

PANDEY AAYUSH RAJKUMAR2 weeks agoAug 26, 2026 07:28 (GMT +5:30)

class Solution {
public void printTillN(int n) {
// code here
if(n==0)
{
return;
}
printTillN(n-1);
System.out.print(n+" ");
}
}

1

Reply

Vishesh Mani  Tripathi2 weeks agoAug 24, 2026 18:30 (GMT +5:30)

class Solution {
public:
void printTillN(int n) {
// code here
if(n == 0)
return;

printTillN(n - 1);
cout << n << " ";
}
};

0

Reply

Adarsh Pawar2 weeks agoAug 23, 2026 12:00 (GMT +5:30)

class Solution:
def printTillN(self, n):
#code here
l=[]
if(n>1):
l.append(n)
self.printTillN(n-1)
else:
l.append(1)
l.sort()
for i in l:
print(i,end=" ")

0

Reply

Mamidi Dhanalakshmi1 month agoAug 01, 2026 19:12 (GMT +5:30)

Java Solution:
class Solution {
public void printTillN(int n) {
// code here
if(n==0){
return ;
}
printTillN(n-1);
System.out.print(n+" ");

}
}

0

Reply
(Show 1 Replies)

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed200 / 200
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:164

Time Taken0.06

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

class Solution:
def printTillN(self, n):
if n==0:
return
self.printTillN(n-1)
print(n,end=" ")

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed200 / 200
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:164

Time Taken0.06

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[1 to n Without Loops](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1)
