# EASIEST PYTHON SOLUTION !

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

Last Digit of a^b
Solved

Difficulty: MediumAccuracy: 23.8%Submissions: 115K+Points: 4

Given two integers a and b in the form of strings. Return the last digit of ab.

Examples:

Input: a = "3", b = "10"
Output: 9
Explanation: 310 = 59049. Last digit is 9.

Input: a = "6", b = "2"
Output: 6
Explanation: 62 = 36. Last digit is 6.

Constraints:
1 ≤ a.size(), b.size() ≤ 1000
a and b consist only of numeric digits ('0' - '9')
a and b do not contain any leading zeros, except when number itself is "0"

Expected Complexities

Time Complexity: O(|b|)
Auxiliary Space: O(1)

Company Tags

Samsung

Topic Tags

Mathematics

Related Articles

Find Last Digit Of Ab For Large Numbers

Discussions ( 125 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Vennela Sri Muthu2 weeks agoAug 26, 2026 15:06 (GMT +5:30)

class Solution:
def getLastDigit(self, a, b):
first_no=int(a[-1])
cycles = {
2:[2,4,8,6],
3:[3,9,7,1],
4:[4,6],
7:[7,9,3,1],
8:[8,4,2,6],
9:[9,1]
}
if b=="0":
return 1
elif first_no in [0,1,5,6]:
return first_no
cycle = cycles[first_no]
length = len(cycle)
rem=0
for digit in b:
rem = (rem*10+int(digit))%length
return cycle[rem-1]

0

Reply

Vaishnavi Khandelwal4 weeks agoAug 13, 2026 15:36 (GMT +5:30)

class Solution:
def getLastDigit(self, a, b):
a1 = int(a) % 10
b1 = int(b)
if b1 == 0: return 1
if a1 == 0 or a1 == 1 or a1 == 5 or a1 == 6: return a1
if a1 == 2:
c = b1 % 4
if c == 0: return 6
elif c == 1: return 2
elif c == 2: return 4
else: return 8
elif a1 == 3:
c = b1 % 4
if c == 0: return 1
elif c == 1: return 3
elif c == 2: return 9
else: return 7          ]
elif a1 == 4:
c = b1 % 2
return 6 if c == 0 else 4
elif a1 == 7:
c = b1 % 4
if c == 0: return 1
elif c == 1: return 7
elif c == 2: return 9
else: return 3
elif a1 == 8:
c = b1 % 4
if c == 0: return 6
elif c == 1: return 8
elif c == 2: return 4
else: return 2
elif a1 == 9:
c = b1 % 2
return 1 if c == 0 else 9

0

Reply

adithyasakthi2572 months agoJul 04, 2026 22:59 (GMT +5:30)

There is a built in function in PYTHON

pow(a,b,10)
means a ** b mod 10
which gives the last digit

since it's a string , convert it to int

class Solution:
def getLastDigit(self, a, b):
# code here
return (pow(int(a[-1]),int(b),10))

1

Reply

Aman Kumar2 months agoJul 02, 2026 20:35 (GMT +5:30)

class Solution {
public:
int getLastDigit(string& a, string& b) {
int n=a.size();
int m=b.size();

if(m==1 && b[0]=='0') return 1;

int num= a[n-1]-'0';

int l=b[m-1]-'0';
int sl=0;
if(m-2>=0) sl=b[m-2]-'0';

int mod=(sl*10+l)%4;
if(mod==0) mod=4;

int ans=num;
mod--;
while(mod--){
ans= (ans*num)%10;
}

return ans;
}
};

0

Reply

Sarthak Raj2 months agoJun 21, 2026 11:00 (GMT +5:30)

class Solution:
def getLastDigit(self, a, b):
# Any number to the power 0 is 1
if b == "0":
return 1

last = int(a[-1])

cycles = {
0: [0],
1: [1],
2: [2, 4, 8, 6],
3: [3, 9, 7, 1],
4: [4, 6],
5: [5],
6: [6],
7: [7, 9, 3, 1],
8: [8, 4, 2, 6],
9: [9, 1]
}

cycle = cycles[last]
m = len(cycle)

rem = 0
for ch in b:
rem = (rem * 10 + int(ch)) % m

if rem == 0:
rem = m

return cycle[rem - 1]

2

Reply
(Show 1 Replies)

Anonymous_Geek2 months agoJun 21, 2026 01:11 (GMT +5:30)

class Solution {
public:
int getLastDigit(string& a, string& b) {
if(b == "0")return 1;
int ld = (a.back() - '0');
int nb;
if(b.size()>=2){
nb = (b[b.size()-2]-'0')*10 + (b.back()-'0');
}
else{
nb = (b.back() - '0');
}
if(ld == 0 or ld == 1 or ld == 5 or ld == 6)return ld;
if(ld == 2 or ld == 3 or ld == 7 or ld == 8){
int p = (nb - 1 + 4)%4 + 1;
return int(pow(ld, p))%10;
}
if(ld == 4 or ld == 9){
int p = (nb - 1 + 2)%2 + 1;
return int(pow(ld, p))%10;
}
}
};

0

Reply

Anonymous_Geek(Edited)20/06/2026, 23:22
2 months agoJun 20, 2026 23:21 (GMT +5:30)

class Solution:

def getLastDigit(self, a, b):

# code here

if b== '0':

return 1

if a[-1] in ('1','5','6'):

return int(a[-1])

elif a[-1] in ('4','9'):

v= int(b)%2

if v ==0:

return (int(a[-1])**2) %10

else:

return (int(a[-1])**v) %10

else:

v= int(b)%4

if v==0:

return (int(a[-1])**4) %10

else:

return (int(a[-1])**v) %10

0

Reply

Abhishek Chaturvedi2 months agoJun 20, 2026 22:01 (GMT +5:30)

class Solution {
public:
int getLastDigit(string& a, string& b) {
// code here
if(b=="0")return 1;
int last_digit= a.back()-'0';
int mod= 0;
for(char ch: b){
mod= (mod*10 + (ch-'0'))%4;
}
if(mod==0){
mod=4;
}
int ans=1;
for(int i=0; i<mod; i++){
ans= (ans*last_digit) %10;
}

return ans;
}

};

0

Reply

Dhruvil Sheth2 months agoJun 20, 2026 21:12 (GMT +5:30)

EASIEST PYTHON SOLUTION !
class Solution:
def getLastDigit(self, a, b):
# code here
a = int(a)
b = int(b)
if b == 0:
return 1
a = a%10
rem = b % 4
vals = {
0: {1:0, 2:0, 3:0, 0:0},
1: {1:1, 2:1, 3:1, 0:1},
2: {1:2, 2:4, 3:8, 0:6},
3: {1:3, 2:9, 3:7, 0:1},
4: {1:4, 2:6, 3:4, 0:6},
5: {1:5, 2:5, 3:5, 0:5},
6: {1:6, 2:6, 3:6, 0:6},
7: {1:7, 2:9, 3:3, 0:1},
8: {1:8, 2:4, 3:2, 0:6},
9: {1:9, 2:1, 3:9, 0:1}}

return vals[a][rem]

0

Reply

Venkatesh Kulkarni2 months agoJun 20, 2026 19:26 (GMT +5:30)

NO DOUBT, GO For this Code
class Solution {
int powerCycle(int x) {
if (x == 2 || x == 3 || x == 7 || x == 8) return 4;
if (x == 4 || x == 9) return 2;
return 1;
}

public:
int getLastDigit(string& a, string& b) {
if (b == "0") return 1;

int y = a.back() - '0';
int cycle = powerCycle(y);

int exp = 0;
for (char ch : b) {
exp = (exp * 10 + (ch - '0')) % cycle;
}

if (exp == 0) exp = cycle;

int ans = 1;
for (int i = 0; i < exp; i++) {
ans = (ans * y) % 10;
}

return ans;
}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1113 / 1113
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 4 / 4Your Total Score:172

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
6
7
8
9
10
11
12
13

class Solution:
def getLastDigit(self, a, b):
# code here
# a= int(a[-1])
# x=a**int(b)
# x=str(x)
# return x[-1]  Takes much time due to high val of b

a=int(a[-1])
b=int(b)
return pow(a,b,10)

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1113 / 1113
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 4 / 4Your Total Score:172

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[EASIEST PYTHON SOLUTION !](https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1)
