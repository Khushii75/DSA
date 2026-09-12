# Tower Of Hanoi

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

Discussions ( 441 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sankeerthana1 week agoSep 04, 2026 19:35 (GMT +5:30)

class Solution {
public int towerOfHanoi(int n, int from, int to, int aux) {
// code here
return (int)(Math.pow(2,n)-1);
}
}

0

Reply

Laxmi Sneha1 week agoSep 03, 2026 11:23 (GMT +5:30)

class Solution {

0

Reply

GORANTLA SIREESHA2 weeks agoAug 25, 2026 16:32 (GMT +5:30)

class Solution {
public int towerOfHanoi(int n, int from, int to, int aux) {
// code here
return (int)(Math.pow(2,n)-1);
}
}

0

Reply

Dushyant chauhan1 month agoAug 11, 2026 09:50 (GMT +5:30)

Time = O(1)

Space Complexity

O(1)  Very Easy         return pow(2,n)-1;

0

Reply

Raman Singh1 month agoAug 07, 2026 15:30 (GMT +5:30)

class Solution:
def  towerOfHanoi(self, n, fromm, to, aux):
# code here

# if n == 1:
#     print(f'Disk {n} -> from {fromm} to {to}')
#     return

# self.towerOfHanoi(n-1, fromm, aux, to)
# print(f'Disk {n} -> from {fromm} to {to}')
# self.towerOfHanoi(n-1, aux, fromm, to)

return 2**n - 1

0

Reply

RAVIKRINDI1 month agoJul 27, 2026 13:49 (GMT +5:30)

class Solution:
def  towerOfHanoi(self, n, fromm, to, aux):
# code here
if n==0:
return 0
else:
return pow(2,n)-1

0

Reply

Anonymous_Geek3 months agoMay 31, 2026 16:26 (GMT +5:30)

class Solution {
public:
int towerOfHanoi(int n, int from, int to, int aux) {
return (1<<n)-1;
}
};

This is all you needs to get all the test cases passed

2

Reply

Jayanta Nath3 months agoMay 22, 2026 18:14 (GMT +5:30)

class Solution:
def  towerOfHanoi(self, n, fromm, to, aux):
# code here

# 1 solve(3, A, C, B)

#    1.1 solve(2, A, B, C)

#        1.1.1 solve(1, A, C, B)

#        1.1.2 move 2 : A → B

#        1.1.3 solve(1, C, B, A)

#    1.2 move 3 : A → C

#    1.3 solve(2, B, C, A)

#        1.3.1 solve(1, B, A, C)

#        1.3.2 move 2 : B → C

#        1.3.3 solve(1, A, C, B)

if n == 1:
return 1

moves = 0

moves += self.towerOfHanoi(n-1, fromm, aux, to)
moves += 1
moves += self.towerOfHanoi(n-1, aux, to, fromm)

return moves

0

Reply

Jayanta Nath3 months agoMay 22, 2026 17:50 (GMT +5:30)

For n = 3
and tower A(3), B, C

Move(3, A → C)
│
├── Move(2, A → B)
│     ├── Move(1, A → C)
│     ├── Move(1, A → B)
│     └── Move(1, C → B)
│
├── Move disk 3 (A → C)
│
└── Move(2, B → C)
├── Move(1, B → A)
├── Move(1, B → C)
└── Move(1, A → C)

0

Reply

Anonymous_Geek4 months agoMay 11, 2026 12:46 (GMT +5:30)

hi

0

Reply
(Show 2 Replies)

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed20 / 20
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:188

Time Taken0.03

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

class Solution:
def  towerOfHanoi(self, n, fromm, to, aux):
# code here
if n==0:
return 0
else:
return pow(2,n)-1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed20 / 20
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:188

Time Taken0.03

Custom Input

## Problem Link

[Tower Of Hanoi](https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)
