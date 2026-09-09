# Check for Power

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

Discussions ( 182 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sankeerthana2 weeks agoAug 26, 2026 20:31 (GMT +5:30)

class Solution {
public boolean isPower(int x, int y) {
// code here
if(x==1)
return y==1;
while(y%x==0){
y/=x;
}
return y==1;
}
}

0

Reply

MOHAMED IRFAN A2 months agoJul 02, 2026 09:47 (GMT +5:30)

class Solution {
static boolean isPower(int x, int y) {
if (x == 1)
return y == 1;
while (y % x == 0) {
y /= x;
}

return y == 1;
}
}

0

Reply

Nishiraj Singh Panwar3 months agoMay 18, 2026 10:02 (GMT +5:30)

class Solution {
public boolean isPower(int x, int y) {
// code here
int i=0;
if(x==1) return false;
if (Math.pow(x,(int)Math.round(((Math.log(y)/Math.log(x)))))==y) return true;
return false;
}
}

0

Reply

Moksh Shah3 months agoMay 15, 2026 09:56 (GMT +5:30)

class Solution {
public boolean isPower(int x, int y) {
// code here
if(x<2||y<x&&y!=1){
return false;
}
int b=0;
while(Math.pow(x,b)<=y){

if(Math.pow(x,b)==y){
return true;
}
b++;
}
return false;
}

}

0

Reply

KEYUR NANDVANA3 months agoMay 15, 2026 09:56 (GMT +5:30)

class Solution {
public boolean isPower(int x, int y) {
// code here
if (x==1 || y<x && y!=1){
return false ;

}

for ( int i =0; Math.pow(x,i)<=y;i++){
if( Math.pow(x,i)==y){
return true ;
}
}
return false;
}
}

0

Reply

Jacob Galloway4 months agoApr 27, 2026 09:46 (GMT +5:30)

how could 100 to any power ever equal 1?

0

Reply
(Show 1 Replies)

Parikshit4 months agoApr 22, 2026 22:53 (GMT +5:30)

class Solution {
public boolean isPower(int x, int y) {
// code here
if(x==1 && y!=1)
return false;

if(x>=1 && y==1)
return true;

while(y>x)
{
if(y%x!=0)
return false;
y=y/x;

}
if(x==y)
return true;
return false;

}
}

0

Reply

Atal   Sharma(Edited)19/04/2026, 22:43
4 months agoApr 19, 2026 22:38 (GMT +5:30)

C++ soluton --class Solution {
public:
bool isPower(int x, int y) {
for(int i=0;i<1000;i++){
if(pow(x,i)==y){
return true;
}
}

}
};

2

Reply

simrn(Edited)19/04/2026, 22:35
4 months agoApr 19, 2026 22:34 (GMT +5:30)

Java Competitive Programming Code:

class Solution {
public boolean isPower(int x, int y) {
if(x == 1 && y > x)
{
return false;
}

double exponent = Math.log(y) / Math.log(x);   //step a.
int power = (int)Math.round(exponent);            //step b.

return Math.round(Math.pow(x, power)) == y;
}
}

Explanation of step a.

1. y is said to be a power of x, if there exists an integer exponent k >= 0, i.e. y = x^k
2. Taking the natural logarithm (ln) of both sides of y=x^k.
3. it becomes as, ln(y) = ln(x^k) or ln(y) = k*ln(x).
4. or we can write it as, k = ln(y) / ln(x). And only this thing we have computed in step a.
5. the output given by Math.log is always in double format.

Explanation of step b.

1. first we have round off the exponent value. the round off is very important to handle the floating point error.
2. after rounding off, we just typecast into int format.

PLEASE UPVOTE IF THIS HELPS.

2

Reply

simrn(Edited)19/04/2026, 22:01
4 months agoApr 19, 2026 21:59 (GMT +5:30)

Java Code:-

class Solution {
public boolean isPower(int x, int y) {
if(x == 1 && y > x)
{
return false;
}
boolean flag = false;
for(int i = 0; i < y; i++)
{
int pow = (int)Math.pow(x, i);
if(pow == y)
{
flag = true;
break;
}
if(pow > y)
{
break;
}
}
return flag;
}
}

PLEASE UPVOTE IF THIS HELPS

5

Reply

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1135 / 1135
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 1 / 1Your Total Score:155

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

class Solution:
def isPower(self, x, y):
# code here
if x==1:
return y==1
while y%x ==0:
y = y//x
return y==1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1135 / 1135
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 1 / 1Your Total Score:155

Time Taken0.03

Custom Input

## Problem Link

[Check for Power](https://www.geeksforgeeks.org/problems/check-if-a-number-is-power-of-another-number5442/1)
