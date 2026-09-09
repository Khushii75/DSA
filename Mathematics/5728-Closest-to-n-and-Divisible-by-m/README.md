# Closest to n and Divisible by m

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

Closest to n and Divisible by m
Solved

Difficulty: BasicAccuracy: 15.77%Submissions: 161K+Points: 1

Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

Examples :

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the Closest Number to 13 which is divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15 and divisible by 6, but -18 has the maximum absolute value. So, output is -18.

Constraints:
-105 ≤ n, m ≤ 105

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Company Tags

Microsoft

Topic Tags

Mathematics

Related Interview Experiences

Microsoft Interview Experience Set 125 Campus Idc

Related Articles

Find Number Closest N Divisible M

Discussions ( 217 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

vishal yadav7 hours agoSep 09, 2026 13:55 (GMT +5:30)

class Solution:
def closestNumber(self, n, m):
# code here
c1=0
c2=0
k=n
k1=n
k2=n
while n%m!=0:
n=n-1
c1=c1+1
k1=n
while k%m!=0:
k=k+1
k2=k
c2=c2+1
if c1==c2:
if abs(k1)>abs(k2):
return k1
else:
return k2
elif c1>c2:
return k2
else:
return k1

0

Reply

Sylvester1 week agoSep 01, 2026 17:32 (GMT +5:30)

class Solution:
def closestNumber(self, n, m):
# code here
m = abs(m)

rem = n % m

lower = n - rem
upper = lower + m

lower_distance = abs(n - lower)
upper_distance = abs(n - upper)

if lower_distance < upper_distance:
return lower

elif upper_distance < lower_distance:
return upper

else:
if abs(lower) > abs(upper):
return lower
else:
return upper

0

Reply

Sankeerthana1 week agoAug 31, 2026 19:51 (GMT +5:30)

Easiest approach     class Solution {
static int closestNumber(int n, int m) {
// code here
int q=n/m;
int a=q*m;
int b;
if(n*m>0)
b=(q+1)*m;
else
b=(q-1)*m;
int d1=Math.abs(n-a);
int d2=Math.abs(n-b);
if(d1<d2)
return a;
else if(d2<d1)
return b;
else
return Math.abs(a)>Math.abs(b)?a:b;
}
}

0

Reply

Anonymous_Geek1 week agoAug 31, 2026 16:46 (GMT +5:30)

@tapob2r934

You Are Wrong

1

Reply

spy kartikey2 weeks agoAug 26, 2026 11:56 (GMT +5:30)

class Solution {
public:
int closestNumber(int n, int m) {
// code here
int remainder= abs(n % m);
if(n>0 && m>0){
if(remainder<m/2)
return (n/m)*m;
else if(remainder>=m/2)
return ((n/m)+1)*m;
}
else if(n<0 && m>0){
if(remainder<m/2)
return (n/m)*m;
else if(remainder>m/2)
return ((n/m)-1)*m;
else if(remainder==m/2)
return ((n/m)-1)*m;
}
else if(n>0 && m<0){
if(remainder<m/2*(-1))
return (n/m)*m;
else if(remainder>m/2*(-1))
return ((abs(n/m))+1)*m*(-1);
else if(remainder==m/2*(-1))
return ((abs(n/m))+1)*m*(-1);
}
else if(n<0 && m<0){
if(remainder<m/2*(-1))
return (n/m)*m;
else if(remainder>m/2*(-1))
return ((n/m)+1)*m;
else if(remainder==m/2*(-1))
return ((n/m)+1)*m;
}

}
};

0

Reply

Anonymous_Geek2 weeks agoAug 25, 2026 15:16 (GMT +5:30)

class Solution {
public:
int closestNumber(int n, int m) {
// code here
int closest = 0;
int minDifference = INT_MAX;
for (int i = n - abs(m); i <= n + abs(m); ++i) {
if (i % m == 0) {
int difference = abs(n - i);

if (difference < minDifference ||
(difference == minDifference && abs(i) > abs(closest))) {
closest = i;
minDifference = difference;
}
}
}
return closest;
}
};

0

Reply

AEHSAN ALAM3 weeks agoAug 17, 2026 12:13 (GMT +5:30)

class Solution {
public:
int closestNumber(int m, int n) {
// code here
int ans;
int minus=0;
if(m<0||n<0){
if(m<0) minus=1;
if(m<0) m=m*-1;
if(n<0) n=n*-1;

}

if(m>=n){
if(m==n){
ans= m;
}
if(n>m){
return 0;
}
}

int rem=m%n;
if(rem>=n/2){
ans=m+n-rem;
}
else ans=m-rem;

if(minus) return -ans;
else return ans;
}
};

0

Reply

Chandu Bantu1 month agoAug 08, 2026 14:07 (GMT +5:30)

class Solution:
def closestNumber(self, n, m):
# code here
q = int(n / m)
n1 = m * q
if (n* m) > 0:
n2 = m * (q+1)
else:
n2 = m * (q-1)

if abs(n - n1) < abs(n - n2):
return n1
elif abs(n - n2)<(n - n1):
return n2
else:
if abs(n1) > abs(n2):
return n1
return n2

0

Reply

AGIDI VINITH1 month agoAug 08, 2026 10:59 (GMT +5:30)

class Solution {
public:
int closestNumber(int n, int m) {
int q=n/m;//quotient
int a=m*(q-1);//immediate neighbour when (n*m<0)
int b=m*q;
int c=m*(q+1);//immediate neighbour when (n*m>=0)
if(n*m>=0){
int abs1=abs(n-b);
int abs2=abs(n-c);
if(abs1==abs2){
if(abs(b)>abs(c)){
return b;
}else{
return c;
}
}else if(abs1<abs2){
return b;
}else{
return c;
}
}else{//when (n*m<0(means that either the quotient is negative or m is negative)
int abs3=abs(n-b);
int abs4=abs(n-a);
if (abs3==abs4){
if(abs(a)>abs(b)){
return a;
}else{
return b;
}
}else if(abs3<abs4){
return b;
}else{
return a;
}
}

}
};

0

Reply

AGIDI VINITH1 month agoAug 08, 2026 10:59 (GMT +5:30)

class Solution {
public:
int closestNumber(int n, int m) {
int q=n/m;//quotient
int a=m*(q-1);//immediate neighbour when (n*m<0)
int b=m*q;
int c=m*(q+1);//immediate neighbour when (n*m>=0)
if(n*m>=0){
int abs1=abs(n-b);
int abs2=abs(n-c);
if(abs1==abs2){
if(abs(b)>abs(c)){
return b;
}else{
return c;
}
}else if(abs1<abs2){
return b;
}else{
return c;
}
}else{//when (n*m<0(means that either the quotient is negative or m is negative)
int abs3=abs(n-b);
int abs4=abs(n-a);
if (abs3==abs4){
if(abs(a)>abs(b)){
return a;
}else{
return b;
}
}else if(abs3<abs4){
return b;
}else{
return a;
}
}

}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 5Accuracy : 20%

Points Scored 1 / 1Your Total Score:152

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
14
15

class Solution:
def closestNumber(self, n, m):
# code here
div= n//m
l = div*m
u = (div + 1)*m
if abs(n-l) < abs(n-u):
return l
elif abs(n-l)> abs(n-u):
return u
else:
if abs(l)>abs(u):
return l
else:
return u

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 5Accuracy : 20%

Points Scored 1 / 1Your Total Score:152

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Closest to n and Divisible by m](https://www.geeksforgeeks.org/problems/closest-number5728/1)
