# Prime Number

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

Prime Number
Solved

Difficulty: EasyAccuracy: 22.2%Submissions: 655K+Points: 2

Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
Examples :

Input: n = 7
Output: true
Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.
Input: n = 25
Output: false
Explanation: 25 has more than two divisors: 1, 5, and 25, so it is not a prime number.
Input: n = 1
Output: false
Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.

Constraints:
1 ≤ n ≤ 109

Expected Complexities

Time Complexity: O(sqrt(n))
Auxiliary Space: O(1)

Company Tags

VMWareAmazonSAP Labs

Topic Tags

MathematicsPrime Number

Related Articles

Check For Prime Number

Discussions ( 426 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sarthak16 hours agoSep 11, 2026 15:14 (GMT +5:30)

I handled first two numbers separately and then looped remaining

0

Reply

Sylvester3 days agoSep 08, 2026 17:22 (GMT +5:30)

class Solution:
def isPrime(self, n):
# code here
if n <= 1:
return False
i = 2
for i in range(2, n):
if n % i == 0:
return False

return True

0

Reply

Sylvester3 days agoSep 08, 2026 17:19 (GMT +5:30)

/**

* @param {number} n

* @return s {boolean}

*/

class Solution {

isPrime(n) {

// code here

if (n <= 1) {

return false;

}

for (let i = 2; i < n; i++) {

if (n % i == 0) {

return false

}

}

return true;

}

}

0

Reply

Archana Kumari3 days agoSep 08, 2026 12:35 (GMT +5:30)

class Solution:

def isPrime(self, n):

# code here

if n<2:

return False

i=2

while i*i<=n:

if n%i==0:

return False

i+=1

return True

0

Reply

Anonymous_Geek1 week agoSep 02, 2026 05:31 (GMT +5:30)

class Solution {
public:
bool isPrime(int n) {
// code here
if(n<2||n>1e9){
return 0;
}

for(int x= 1; x<=sqrt(n);x++){
if(x>1 && n%x==0){
return false;
}

}

return true;

}
};

1

Reply

Anonymous_Geek3 weeks agoAug 19, 2026 18:05 (GMT +5:30)

class Solution {
static boolean isPrime(int n) {
if(n<2){
return false;
}
for(int i=2;i*i<=n;i++){
if(n%i == 0){
return false;
}
}
return true;
}
}

1

Reply

AVasaniya(Edited)17/08/2026, 12:01
3 weeks agoAug 17, 2026 11:59 (GMT +5:30)

class Solution {
static boolean isPrime(int n) {
// code here
int stm = n/2;
boolean isPrime = true;

if (n == 1) {
return false;
}

for (int i = 2; i <= stm; i++) {
if (n % i == 0) {
isPrime = false;
break;
}
}

return isPrime;
}
}

Simple Java Solution | Fully Optimized

1

Reply

AVasaniya3 weeks agoAug 17, 2026 11:59 (GMT +5:30)

class Solution {
static boolean isPrime(int n) {
// code here
int stm = n/2;
boolean isPrime = true;

if (n == 1) {
return false;
}

for (int i = 2; i <= stm; i++) {
if (n % i == 0) {
isPrime = false;
break;
}
}

return isPrime;
}
}

0

Reply

AVasaniya3 weeks agoAug 17, 2026 11:59 (GMT +5:30)

class Solution {
static boolean isPrime(int n) {
// code here
int stm = n/2;
boolean isPrime = true;

if (n == 1) {
return false;
}

for (int i = 2; i <= stm; i++) {
if (n % i == 0) {
isPrime = false;
break;
}
}

return isPrime;
}
}

0

Reply

AVasaniya3 weeks agoAug 17, 2026 11:59 (GMT +5:30)

class Solution {
static boolean isPrime(int n) {
// code here
int stm = n/2;
boolean isPrime = true;

if (n == 1) {
return false;
}

for (int i = 2; i <= stm; i++) {
if (n % i == 0) {
isPrime = false;
break;
}
}

return isPrime;
}
}

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 2 / 2Your Total Score:168

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
9
10
11
12

class Solution:
def isPrime(self, n):
# code here

if n<=2:
return False
for i in range(2, int(n**0.5)+1):
if n%i==0:
return False

return True

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 2 / 2Your Total Score:168

Time Taken0.04

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Prime Number](https://www.geeksforgeeks.org/problems/prime-number2314/1)
