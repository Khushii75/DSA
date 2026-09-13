# Print n to 1 Without Loop

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Dark Mode
99+

Menu

Back to Explore Page

Ask A DoubtMy Doubts

FREQUENTLY ASKED QUESTIONS

ProblemEditorialSubmissionsComments

Print n to 1 Without Loop
Solved

Difficulty: BasicAccuracy: 77.72%Submissions: 150K+Points: 1Average Time: 10m

Print numbers from n to 1 (space separated) without the help of loops.

Examples :

Input: n = 10
Output: 10 9 8 7 6 5 4 3 2 1

Constraints :
1 ≤ n ≤ 1000

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(n)

Topic Tags

Recursion

Related Articles

Print N To 1 Without Loop

Discussions ( 195 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sylvester1 week agoSep 03, 2026 19:01 (GMT +5:30)

class Solution:
def printNos(self, n):
# Code here
if n == 0:
return

print(n, end=" ")
self.printNos(n - 1)

0

Reply

Sylvester1 week agoSep 03, 2026 19:00 (GMT +5:30)

/**
* @param {number} N
* @returns {void}
*/
class Solution {
printNos(n) {
// code here
if(n == 0){
return;
}

process.stdout.write(n + " ");
this.printNos(n-1);
}
}

0

Reply

Abhishek Chaturvedi1 month agoAug 03, 2026 14:53 (GMT +5:30)

class Solution {
public:
void printNos(int n) {
// code here
if(n==0)return;
cout<<n<<" ";
printNos(n-1);
}
};

0

Reply

Mamidi Dhanalakshmi1 month agoAug 01, 2026 19:09 (GMT +5:30)

Java Solution:
class Solution {
void printNos(int n) {
// code here
if(n==0){
return;
}
System.out.print(n+" ");
printNos(n-1);
}
}

0

Reply

Ishwar Inamdar2 months agoJun 25, 2026 10:26 (GMT +5:30)

class Solution:
def printNos(self, n):
if n == 0:
return
else:
print(n, end=' ')
self.printNos(n-1)

1

Reply

Abhay Yadav3 months agoJun 13, 2026 13:35 (GMT +5:30)

class Solution {
public:
void printNos(int n) {
// code here
if(n>=1){
cout << n << " ";
printNos(n-1);
}
}
};

0

Reply

Alman4 months agoMay 04, 2026 13:41 (GMT +5:30)

PYTHON CODE:

class Solution:
def printNos(self, n):
# Code here
if n<1:
return
print(n, end=" ")
self.printNos(n-1)

0

Reply

Alman4 months agoMay 04, 2026 13:41 (GMT +5:30)

PYTHON CODE:

0

Reply

Alman4 months agoMay 04, 2026 13:41 (GMT +5:30)

PYTHON CODE:

0

Reply

Niraj Nilesh Mate5 months agoMar 31, 2026 16:03 (GMT +5:30)

class Solution {

void printNos(int N) {
// code here
if(N==0){
return;
}
System.out.print(N+" ");
printNos( N-1);
}
}

1

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed160 / 160
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:191

Time Taken0.05

Python3
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
def printNos(self, n):
# Code here
if n == 0:
return

print(n, end=" ")
self.printNos(n - 1)

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed160 / 160
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:191

Time Taken0.05

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Print n to 1 Without Loop](https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1)
