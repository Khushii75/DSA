# Palindrome Digit Sum

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

Discussions ( 296 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sankeerthana1 week agoAug 28, 2026 22:47 (GMT +5:30)

class Solution {
boolean isDigitSumPalindrome(int n) {
// code here
int sum=0;
while(n!=0){
int digit=n%10;
sum+=digit;
n=n/10;
}
int target=sum;
int rev=0;
while(sum>0){
int d=sum%10;
rev=rev*10+d;
sum/=10;
}
return target==rev;
}
}

0

Reply

Pulak Kanti Pramanik4 weeks agoAug 11, 2026 16:14 (GMT +5:30)

class Solution {
boolean isDigitSumPalindrome(int n) {
// code here
int sum = 0 ;
while(n>0){
int digit = n%10 ;
sum =  sum + digit ;
n=n/10;
}
int originalSum=sum;
int reverse =  0 ;
while(sum>0){
int digits = sum%10 ;
reverse = reverse*10 + digits;
sum = sum/10;
}
if(originalSum==reverse){
return true ;
}
else {
return false ;
}

}

}

0

Reply

Gautham Krishna6 months agoFeb 28, 2026 11:58 (GMT +5:30)

Easiest method in python:

class Solution:
def isDigitSumPalindrome(self, n):
#code here
sum=0
for number in str(n):
sum+=int(number)
sum=str(sum)
return sum==sum[::-1]

Even shorter:

class Solution:
def isDigitSumPalindrome(self, n):
s = str(sum(int(d) for d in str(n)))
return s == s[::-1]

1

Reply

DAYAPULI SRINIVASULA RAO6 months agoFeb 28, 2026 10:18 (GMT +5:30)

class Solution:
def isDigitSumPalindrome(self, n):
#code here
res=0
for i in str(n):
res=res+int(i)
z=str(res)
l=z[::-1]
if res==int(l):
return True
else:
return False

1

Reply

Ashutosh Paswan8 months agoDec 27, 2025 21:09 (GMT +5:30)

// User function Template for Java

class Solution {
boolean isDigitSumPalindrome(int n) {

// Step 1: Find sum of digits
int sum = 0;
while (n > 0) {
sum += n % 10;
n /= 10;
}

// Step 2: Check if sum is palindrome
int original = sum;
int rev = 0;
while (sum > 0) {
rev = rev * 10 + sum % 10;
sum /= 10;
}

// Step 3: Return result
return original == rev;

}

}

1

Reply

Mukesh Kumar Pathak10 months agoNov 09, 2025 13:32 (GMT +5:30)

class Solution {
public:
virtual int rev(int x){
int y=0;
while(x>0){
y = y*10 + (x%10);
x/=10;
}
return y;
}

virtual bool isDigitSumPalindrome(int n) {
int digSum=0;
while(n>0){
digSum += (n%10);
n/=10;
}

int revValue = rev(digSum);

return (revValue == digSum);
}
};

0

Reply

Sai Vishnu Vardhan Bathini10 months agoNov 02, 2025 12:48 (GMT +5:30)

For Python3 Platform

class Solution:
def isDigitSumPalindrome(self, n):
sum_of_digits = 0

while(n > 0):
sum_of_digits = sum_of_digits + n % 10

n = n//10

if(str(sum_of_digits) == str(sum_of_digits)[::-1]):
return True
else:
return False

0

Reply

Adithya B R1 year agoSep 05, 2025 14:26 (GMT +5:30)

class Solution {
boolean isDigitSumPalindrome(int n) {
// code here
int sum=0;

while(n>0){
int digit = n%10;
sum += digit;
n /= 10;
}

int rev = 0;
n = sum;

while(n>0){
int digit = n%10;
rev = rev*10+digit;
n /= 10;
}

return sum == rev;
}
}

0

Reply

k sandeep1 year agoAug 30, 2025 07:53 (GMT +5:30)

python class Solution:
def isDigitSumPalindrome(self, n):

sum_digits = 0

while n > 0:
sum_digits += n % 10

n //= 10

red = str(sum_digits)

name = red[::-1]

if str(sum_digits) == name:

return True

else:

return False

0

Reply

Anonymous_Geek1 year agoJun 17, 2025 10:57 (GMT +5:30)

// User function Template for Java

class Solution {
boolean isDigitSumPalindrome(int n) {
// code here
int sum=0;
String str_n=n+"";

for(int i=0;i<str_n.length();i++){
sum+=str_n.charAt(i)-'0';
}

String str_sum=sum+"";
int start=0,end=str_sum.length()-1;

while(start<end){
if(str_sum.charAt(start)!=str_sum.charAt(end)){
return false;
}
start++;
end--;
}

return true;

}
}

0

Reply

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:156

Time Taken0.04

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
def isDigitSumPalindrome(self, n):
#code here
n= str(n)
sum=0
for i in n:
sum += int(i)
sum = str(sum)
return sum == sum[::-1]

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:156

Time Taken0.04

Custom Input

## Problem Link

[Palindrome Digit Sum](https://www.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1)
