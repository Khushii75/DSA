# Count Perfect Squares

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

Count Perfect Squares
Solved

Difficulty: BasicAccuracy: 41.44%Submissions: 166K+Points: 1

Given a positive integer n, find the number of perfect squares that are less than n in the sample space of perfect squares. The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)

Examples :

Input: n = 9
Output: 2
Explanation: 1 and 4 are the only Perfect Squares less than 9. So, the Output is 2.

Input: n = 3
Output: 1
Explanation: 1 is the only Perfect Square less than 3. So, the Output is 1.

Constraints:
1 <= n <= 108

Expected Complexities

Time Complexity: sqrt(n)
Auxiliary Space: O(1)

Company Tags

AccoliteSnapdealOla Cabs

Topic Tags

Mathematics

Related Interview Experiences

Ola Interview Experience Set 11 InternshipAccolite Interview Experience Set 4 On Campus

Related Articles

Count Perfect Squares

Discussions ( 469 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

mohseen inamdar1 day agoSep 07, 2026 19:45 (GMT +5:30)

int count=0;

for(int i=1; i<=n/2; i++){
if(i*i < n ) count++;
else break;
}
return count;

0

Reply

Sankeerthana2 weeks agoAug 26, 2026 15:13 (GMT +5:30)

easy way                                                                                                                                     class Solution {
static int countSquares(int n) {
// code here
int count=0;
for(int i=1;i*i<=n;i++){
if(i*i<n)
count++;

}
return count;
}
}

0

Reply

Sumukh   B R2 weeks agoAug 24, 2026 12:13 (GMT +5:30)

class Solution:
def countSquares(self, n):
per_sq=[]
for i in range(1,int(n**0.5)+1):
if i**2<n:
per_sq.append(i**2)

return len(per_sq)

0

Reply

Keerthana Singirthi2 weeks agoAug 22, 2026 12:00 (GMT +5:30)

class Solution:
def countSquares(self, n):
num = n ** 0.5
new = int(num)
diff = num-new
if(diff>0):
return new
elif(diff==0):
return new-1

0

Reply

GATTU AKHIL2 weeks agoAug 20, 2026 12:03 (GMT +5:30)

import math

class Solution:
def countSquares(self, N):
if N <= 1:
return 0
return math.isqrt(N - 1)

0

Reply

Vijay Kothagolla3 weeks agoAug 13, 2026 10:43 (GMT +5:30)

class Solution:
def countSquares(self, n):
# code here
num = n ** 0.5
new = int(num)
diff = num-new
if(diff>0):
return new
elif(diff==0):
return new-1

0

Reply

Anonymous_Geek4 weeks agoAug 12, 2026 03:07 (GMT +5:30)

One line solution with O(1) time complexity?

class Solution {
public:
int countSquares(int n) {
// code here
return ceil(sqrt(n) - 1);
}
};

0

Reply

CHARAN BIRRU1 month agoAug 06, 2026 11:31 (GMT +5:30)

class Solution:
def countSquares(self, n):
count = 0
i = 1

while i * i < n:
count += 1
i += 1

return count

0

Reply

ASHUTOSH KUMAR1 month agoAug 05, 2026 07:53 (GMT +5:30)

easy way

class Solution {
public:
int countSquares(int n) {
// code here
int count = 0;
int i=1;

while(i<=n)
{
if((i*i)<n)
count++;

else
break;

i++;
}

return count;
}
};

0

Reply

Anonymous_Geek1 month agoAug 02, 2026 14:40 (GMT +5:30)

Please do not post the solution of code

2

Reply
(Show 1 Replies)

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:150

Time Taken0.06

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
9

class Solution:
def countSquares(self, n):
# code here
count=0
i=1
while i*i<n:
count += 1
i+=1
return count

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:150

Time Taken0.06

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Count Perfect Squares](https://www.geeksforgeeks.org/problems/count-squares3649/1)
