# Print the Kth Digit

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

Discussions ( 192 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sankeerthana1 week agoAug 31, 2026 20:13 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long s=(long)Math.pow(a,b);
long rem=0;
while(k>0){
rem=s%10;
s/=10;
k--;
}
return rem;
}
}

0

Reply

Kartik Nautiyal1 month agoAug 06, 2026 23:31 (GMT +5:30)

class Solution {
public:
int kthDigit(int a, int b, int k) {
// code here
long long cube = pow(a,b);
int rem;

while (k) {
rem = cube % 10;
cube /= 10;
k--;
}
return rem;
}
};

0

Reply

Amit Sharma1 month agoAug 05, 2026 16:34 (GMT +5:30)

class Solution {
public:
int kthDigit(int a, int b, int k) {
// code here

// i. pow(x, n) -> Binary exponentiation -> O(log b)
long long x = a; // value
long long binForm = b;  // power
long long ans = 1;

while(binForm > 0) {
int rem = binForm % 2;
binForm /= 2;

if(rem == 1) {
ans *= x; // 3 value * 1
}

x *= x; // value ka sq
}

// ii. print kth digit -> linear TC -> O(d)
int count = 0;
while(ans > 0) {  // pow(3, 3) -> ans = 27
int rem = ans % 10;
ans /= 10;

count++;
if(count == k) {
return rem;
}
}

return -1;

}
};

// Note: O(log b) means O(log n) but i have used variable b so that used bi instead of n.
// similarly for -> O(d) but this is -> O(n)

// Important:
// Kisi bhi number n ke binary representation me digits (bits) = log₂(n) + 1 (for n > 0)
// binForm = log₂(n) + 1
// log2(8)=3 -> means what power of 2 = 8

0

Reply

Deepal Shah1 month agoJul 13, 2026 16:56 (GMT +5:30)

Just use Math.pow. then convert no. Into string, use .charAt(str.length() -k ) to extract digit

0

Reply

BALAJI.R2 months agoJul 05, 2026 13:49 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long p = 1;
for(int i=1; i<=b; i++){
p = p*a;
}
for (int i=1; i<k; i++){
p = p/10;
}
return p%10;
}
}

3

Reply

Tharunkumar S2 months agoJul 05, 2026 13:36 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long n = (long) Math.pow(a, b);
int i = 1;
while (i < k) {
n = n / 10;
i++;
}
return n % 10;
}
}

2

Reply
(Show 1 Replies)

Adithya Gugloth5 months agoApr 07, 2026 09:56 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

Subhash Ch6 months agoFeb 28, 2026 15:06 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num>0 && i<k){
num = num/10;
i++;
}
return num%10;

}
}

2

Reply

Venkat M6 months agoFeb 28, 2026 11:53 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k)
{
long num = (long)Math.pow(a,b);
int i=1;
while(num>0 && i<k)
{
num = num/10;
i++;
}
return num%10;

}
}

0

Reply

Goutham Goutham6 months agoFeb 28, 2026 11:05 (GMT +5:30)

class Solution {
static int kthDigit(int a, int b, int k) {

// Step 1: Calculate a^b
long power = (long)Math.pow(a, b);

// Step 2: Remove last (k-1) digits
power = power / (long)Math.pow(10, k - 1);

// Step 3: Return last digit
return (int)(power % 10);
}
}

0

Reply

Manvith Ajay Peta6 months agoFeb 24, 2026 11:00 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num>0 && i<k){
num = num/10;
i++;
}
return num%10;

}
}

0

Reply

JAMPULA YASHWANTH6 months agoFeb 21, 2026 13:48 (GMT +5:30)

code in java

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num>0 && i<k){
num = num/10;
i++;
}
return num%10;

}
}

0

Reply

rishitha6 months agoFeb 19, 2026 10:26 (GMT +5:30)

Java code

// User function Template for Java

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num>0 && i<k){
num = num/10;
i++;
}
return num%10;
}
}

0

Reply

NIMMA REDDY SURYA TEJA REDDY6 months agoFeb 18, 2026 13:32 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

THAMMANAVENI ASHWAN6 months agoFeb 17, 2026 15:27 (GMT +5:30)

class Solution {
static int kthDigit(int a, int b, int k) {
long power = (long) Math.pow(a, b);
String str = Long.toString(power);
int len = str.length();
char ch = str.charAt(len - k);
return ch - '0';
}
}

1

Reply

Bittu Katkuri6 months agoFeb 17, 2026 15:27 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

Samisetty shravani6 months agoFeb 17, 2026 12:03 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

Navaneeth Kumar Panthula6 months agoFeb 17, 2026 10:42 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

1

Reply

Srikar6 months agoFeb 14, 2026 11:41 (GMT +5:30)

class Solution:
def kthDigit(self, A, B, K):
# code here
x=pow(A,B)
while K>0:
rem=x%10
K-=1
x=x//10
return rem

0

Reply

Ganesh goud6 months agoFeb 14, 2026 11:39 (GMT +5:30)

class Solution:
def kthDigit(self, A, B, K):
pow=str(A**B)
return pow[-K]

0

Reply

LATCHIPATRUNI PRADEEP NAIDU6 months agoFeb 13, 2026 15:19 (GMT +5:30)

result = a ** b
return (result // 10 ** (k-1)) % 10

0

Reply

Dharavath Sunil6 months agoFeb 13, 2026 13:26 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

godugu tarun6 months agoFeb 13, 2026 11:55 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply
(Show 1 Replies)

godugu tarun6 months agoFeb 13, 2026 11:53 (GMT +5:30)

hi

0

Reply
(Show 2 Replies)

CHARAN Reddy6 months agoFeb 13, 2026 11:41 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply
(Show 1 Replies)

Balakumaran M7 months agoFeb 09, 2026 20:01 (GMT +5:30)

class Solution:
def kthDigit(self, a, b, k):
# code here
result = a ** b
return (result // 10 ** (k-1)) % 10

0

Reply

247Y1A66J1 THATIKONDA SRIHARI7 months agoFeb 07, 2026 13:35 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

247Y1A66J1 THATIKONDA SRIHARI7 months agoFeb 07, 2026 13:35 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

247Y1A66J1 THATIKONDA SRIHARI7 months agoFeb 07, 2026 13:35 (GMT +5:30)

class Solution {
static long kthDigit(int a, int b, int k) {
// code here
long num = (long)Math.pow(a,b);
int i=1;
while(num > 0 && i < k){
num = num / 10;
i++;
}
return num % 10;
}
}

0

Reply

Denys Shmahailo7 months agoFeb 04, 2026 18:39 (GMT +5:30)

Js Solution:
kthDigit(a, b, k) {
let res= (a ** b) % (10 ** k);

for(let i = 1; i < k;i++) {
res = Math.floor(res / 10)
}
return res

}

0

Reply

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed110 / 110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:159

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
def kthDigit(self, a, b, k):
# code here
x= pow(a,b)

return str(x)[-k]

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed110 / 110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:159

Time Taken0.03

Custom Input

## Problem Link

[Print the Kth Digit](https://www.geeksforgeeks.org/problems/print-the-kth-digit3520/1)
