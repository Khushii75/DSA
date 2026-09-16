# Replace all 0's with 5

## Problem

CoursesSale

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

Replace all 0's with 5
Solved

Difficulty: BasicAccuracy: 75.55%Submissions: 156K+Points: 1Average Time: 15m

You are given an integer n. You need to convert all zeroes of n to 5.

Examples:

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.

Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.

Constraints:
0 <= n <= 105

Expected Complexities

Time Complexity: O(k)
Auxiliary Space: O(1)

Company Tags

Amazon

Topic Tags

ArraysMathematics

Related Articles

Replace 0 5 Input Integer

Discussions ( 575 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sidhartha mandal2 weeks agoSep 01, 2026 10:39 (GMT +5:30)

class Solution {
public int convertFive(int n) {
// code here
int final_reasult = 0;
int fr = 0;
if(n==0){
return 5;
}
while(n>0){
int last_digit = n%10;
if(last_digit==0){
last_digit = 5;
}
final_reasult = final_reasult*10+last_digit;
n=n/10;
}

while(final_reasult>0){
int ld= final_reasult%10;

fr = fr*10+ld;
final_reasult=final_reasult/10;
}
return fr;

}
}

0

Reply

Nandini Singarajupalle2 weeks agoAug 29, 2026 22:13 (GMT +5:30)

class Solution:
def convertFive(self, n):
# code here
return int(str(n).replace('0','5'))

1

Reply
(Show 1 Replies)

Vikash Kumar bharti3 weeks agoAug 23, 2026 04:44 (GMT +5:30)

Java Solution :

class Solution {
public int convertFive(int n) {

if(n==0) return 5;
// code here
int res = 0;
int i = 1;
while(n>0){

int dig = n%10;

if(dig == 0){
res = (5 * i) + res;
}else{
res = (dig * i) + res;
}

i *= 10;

n /= 10;

}

return res;
}
}

0

Reply

Chandu Bantu3 weeks agoAug 22, 2026 13:48 (GMT +5:30)

class Solution:
def convertFive(self, n):
# code here
return int(str(n).replace('0' , '5'))

0

Reply

KARTHIK YADAV3 weeks agoAug 19, 2026 22:38 (GMT +5:30)

public int convertFive(int n) {

if(n==0){

return 5;

}

int rev=0;

while(n!=0) {

int rem=n%10;

if(rem==0) {

rem+=5;

}

rev=rev*10+rem;

n/=10;

}

while(rev!=0) {

int rem=rev%10;

n=n*10+rem;

rev/=10;

}

return n;

}

}

1

Reply

sumatew7a1 month agoAug 13, 2026 12:25 (GMT +5:30)

class Solution{
convertFive(n){
return Number(String(n).replaceAll('0','5'));
}
}

0

Reply

CHARAN BIRRU1 month agoAug 06, 2026 12:11 (GMT +5:30)

class Solution:
def convertFive(self, n):
return int(str(n).replace('0', '5'))

0

Reply

Nivedhitha K3 months agoJun 15, 2026 11:24 (GMT +5:30)

# Function should return an integer value
class Solution:
def convertFive(self, n):
# Code here
j=str(n)
j = j.replace('0', '5')
return int(j)

0

Reply

Swagata Battacharya3 months agoMay 29, 2026 12:45 (GMT +5:30)

class Solution {
public:
int convertFive(int n) {
if(n == 0)
return 5;
vector<int> arr;
while(n > 0) {
arr.push_back(n % 10);
n /= 10;
}
reverse(arr.begin(), arr.end());
for(int &x : arr) {
if(x == 0) {
x = 5;
}
}
int updatedNumber = 0;
for(int x : arr) {
updatedNumber = updatedNumber * 10 + x;
}

return updatedNumber;
}
};

0

Reply

SteveKevlar3 months agoMay 28, 2026 20:11 (GMT +5:30)

python code
return int(str(n).replace('0', '5'))

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:194

Time Taken0.03

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

class Solution:
def convertFive(self, n):
# code here
n_s = str(n)
return n_s.replace('0', '5')

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:194

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Replace all 0's with 5](https://www.geeksforgeeks.org/problems/replace-all-0s-with-5/1)
