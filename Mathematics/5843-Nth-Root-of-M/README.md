# Nth Root of M

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

Nth Root of M
Solved

Difficulty: MediumAccuracy: 25.06%Submissions: 302K+Points: 4Average Time: 15m

You are given 2 numbers n and m, the task is to find n√m (nth root of m). If the root is not integer then return -1.

Examples :

Input: n = 3, m = 8
Output: 2
Explanation: 23 = 8

Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.

Input: n = 4, m = 16
Output: 2
Explanation: 24 = 16

Constraints:
1 ≤ n ≤ 9
0 ≤ m ≤ 20

Expected Complexities

Time Complexity: O(n log m)
Auxiliary Space: O(1)

Company Tags

DirectiAccenture

Topic Tags

MathematicsBinary Search

Related Interview Experiences

Directi Interview Set 3

Related Articles

N Th Root Number

Discussions ( 357 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Nikhil4 days agoSep 07, 2026 17:22 (GMT +5:30)

class Solution {
public int nthRoot(int n, int m) {
// code here
if(n == 1 || m <= 1) return m;
if(n == 2){
if(m == 4) return 2;
else if(m == 9) return 3;
else if(m == 16) return 4;
}
if(n == 3 && m == 8) return 2;
if(n == 4 && m == 16) return 2;
return -1;
}
}

lol i did this for fun and worked

0

Reply

Mohammad Ibrahim1 month agoAug 08, 2026 18:00 (GMT +5:30)

class Solution {
public:
long long power(int base, int expo) {
long long result = 1;
long long b = base;

while (expo > 0) {
if (expo % 2 == 1)          // odd exponent -> multiply extra base
result *= b;
b *= b;                     // square the base
expo /= 2;                  // halve the exponent
}
return result;
}
int nthRoot(int n, int m) {
bool negative = false;
if ( m == 0)
return 0;
if (m < 0) {
if (n % 2 == 0) return -1;  // even root of negative number = no real solution
negative = true;
m = -m;
}

int low = 1, high = m;
while (low <= high) {
int mid = (low + high) / 2;
long long val = power(mid, n);

if (val == m)
return negative ? -mid : mid;
else if (val < m)
low = mid + 1;
else
high = mid - 1;
}
return -1;
// Code here

}
};

TC: O(log m * log n)
SC: O(1)

0

Reply

Rohit Kumar1 month agoAug 03, 2026 20:51 (GMT +5:30)

class Solution {
private:
int power(int base, int expo, int limit){
int result=1;
for(int i=0; i<expo; i++){
result*=base;

if(result > limit){
return result;
}
}
return result;
}
public:
int nthRoot(int n, int m) {
// Code here
if(m == 0) return 0;

if(n==1) return m;

int low=1;
int high=m;

while(low <= high){
int mid = (high+low)/2;

int val = power(mid, n, m);

if(val == m) return mid;

else if(val < m) low=mid+1;

else high=mid-1;
}
return -1;
}
};

1

Reply

FAIZAN AHMED2 months agoJun 26, 2026 17:12 (GMT +5:30)

class Solution:
def power(self, mid, n, m):
res = 1
for _ in range(n):
res *= mid
if res > m:
return 2
if res == m:
return 1
return 0

def nthRoot(self, n, m):
if m == 0:
return 0

l, r = 1, m

while l <= r:
mid = (l + r) // 2
val = self.power(mid, n, m)

if val == 1:
return mid
elif val == 2:
r = mid - 1
else:
l = mid + 1

return -1

0

Reply

Shrey(Edited)24/06/2026, 23:20
2 months agoJun 24, 2026 23:12 (GMT +5:30)

Mathematical way - k power n is m, taking log on both sides will make nlogk = logm . by which we can estimate that logk=logm/n. and k is antilog(logm/n).  First you can take log of any base and then take antilog which is just power of the bas to log i.e k= pow(base, logm/n);  Also check if the integer type of this is equal to the boolean type then yes else no.                                                                                                              int nthRoot(int n, int m) {
if(n==1) return m;

double logged=log2(m);
logged=logged/n;
double result=pow(2,logged);
int temp=result;
if((double)temp != result) return -1;
else return temp;
}

0

Reply

Jayanta Nath2 months agoJun 20, 2026 13:33 (GMT +5:30)

# Binary search + Early stopping (avoids overflow)

class Solution:
def power(self, mid, n, m):
res = 1
for _ in range(n):
res *= mid
if res > m:
return 2
return 1 if res == m else 0

def nthRoot(self, n, m):
# code here
l, r = 0, m

while l <= r:
mid = l + (r-l)//2
val = self.power(mid, n, m)

if val == 1:
return mid
if val == 2:
r = mid - 1
else:
l = mid + 1

return -1

0

Reply

ved patel2 months agoJun 19, 2026 14:14 (GMT +5:30)

here it's simple solution with binary search case

class Solution {

public:

long long power(int mid, int n, int m) {

long long res = 1;

for (int i = 0; i < n; i++) {

res *= mid;

if (res > m)

return res;

}

return res;

}

int nthRoot(int n, int m) {

if (m == 0)

return 0;

if (n == 1)

return m;

int low = 1;

int high = m;

while (low <= high) {

long long mid = low + (high - low)/2;

long long val = power(mid, n, m);

if (val == m) {

return mid;

} else if (val < m) {

low = mid + 1;

} else {

high = mid - 1;

}

}

return - 1; }

};

1

Reply

Praneeth(Edited)18/06/2026, 08:06
2 months agoJun 18, 2026 08:06 (GMT +5:30)

Simple C++ Solution | O (log m * log n) Quick Power (Binary Exponentiation) | Binary Search

class Solution {
public:
int nthRoot(int n, int m) {
// Code here
int l = 0, r = m;
while(l<=r) {
int mid = l + (r-l)/2;
if(q_power(mid, n) == m) return mid;
else if(q_power(mid,n) > m) r = mid-1;
else l = mid+1;
}

return -1;
}

long long q_power(long long base, int power) {
long long res = 1;
for(;power;power>>=1){
if(power & 1) {
res = 1ll * base * res;
}
base = 1ll * base * base;
}

return res;
}
};

0

Reply

Shivam(Edited)07/06/2026, 16:33
3 months agoJun 07, 2026 16:29 (GMT +5:30)

To find the n-th root of m efficiently, we can use Binary Search.

Since we are looking for an integer root, our search space ranges from 1 to m. If n = 1, the answer is always m. For any other case, we can search for an integer mid such that mid^n = m.

Step-by-Step Approach

Base Cases: * If m = 0 or m = 1, the n-th root is m itself.

If n = 1, the n-th root is m.

Binary Search: Set low = 1 and high = m.

While low <= high:

Calculate mid = low + (high - low) / 2.

Create a helper function multiply(mid, n, m) to calculate mid^n.

If the product equals m, return 1.

If at any point the product exceeds m, return 2 (prevents overflow).

If the loop finishes and the product is less than m, return 0.

If the helper returns 1, we found our exact integer root; return mid.

If it returns 2, mid is too large; search the left half (high = mid - 1).

If it returns 0, mid is too small; search the right half (low = mid + 1).

If the loop ends without finding an exact match, return -1

class Solution {
// Helper function to check mid^n against m
// Returns:
// 1 if mid^n == m
// 0 if mid^n < m
// 2 if mid^n > m
private int checkPower(int mid, int n, int m) {
long ans = 1;
for (int i = 1; i <= n; i++) {
ans = ans * mid;
if (ans > m) return 2; // Overflew m, so mid is too big
}
if (ans == m) return 1;
return 0;
}

public int NthRoot(int n, int m) {
int low = 1, high = m;

while (low <= high) {
int mid = low + (high - low) / 2;
int status = checkPower(mid, n, m);

if (status == 1) {
return mid; // Found the exact integer root
} else if (status == 2) {
high = mid - 1; // mid^n > m, look for smaller numbers
} else {
low = mid + 1; // mid^n < m, look for larger numbers
}
}

return -1; // Not an integer root
}
}

0

Reply

DUDDI JOTISH KUMAR3 months agoJun 03, 2026 14:47 (GMT +5:30)

# Intuition

We need to find an integer `x` such that:

:contentReference[oaicite:0]{index=0}

If such an integer exists, return `x`; otherwise return `-1`.

Since the value of `xⁿ` increases as `x` increases, the search space is monotonic. This allows us to use binary search on the possible values of `x`.

Instead of directly computing `midⁿ`, we use a helper function that:

- Returns `1` if `midⁿ = m`
- Returns `0` if `midⁿ < m`
- Returns `2` if `midⁿ > m`

The helper also stops early whenever the value exceeds `m`, preventing unnecessary computations and avoiding overflow issues.

---

# Approach

1. Handle the special case:
- If `m = 0`, return `0`.

2. Apply binary search on the range `[1, m]`.

3. For each `mid`:
- Compute the relation between `midⁿ` and `m` using the helper function.
- If equal, return `mid`.
- If smaller, search the right half.
- If larger, search the left half.

4. If no integer root is found, return `-1`.

---

# Helper Function

The helper function computes `midⁿ` iteratively:

```cpp
func(mid, n, m)
```

Returns:

```cpp
0 -> midⁿ < m
1 -> midⁿ = m
2 -> midⁿ > m
```

As soon as the value exceeds `m`, it immediately returns `2`.

---

# Example

### Input

```cpp
n = 3
m = 27
```

Binary Search:

```cpp
mid = 14 → 14³ > 27
```

Search left half.

```cpp
mid = 7 → 7³ > 27
```

Search left half.

```cpp
mid = 3 → 3³ = 27
```

Return `3`.

---

# Complexity Analysis

- **Time Complexity:** `O(n · log m)`
- Binary search takes `O(log m)` iterations.
- Each iteration computes `midⁿ` in `O(n)` time.

- **Space Complexity:** `O(1)`
- Only constant extra space is used.

---

# Code

```cpp
class Solution {
public:
int func(int mid, int n, int m) {
long long ans = 1;

for (int i = 1; i <= n; i++) {
ans *= mid;

if (ans > m) {
return 2;
}
}

if (ans < m) return 0;

return 1;
}

int nthRoot(int n, int m) {
if (m == 0) {
return 0;
}

int low = 1;
int high = m;

while (low <= high) {
int mid = (low + high) / 2;

int midN = func(mid, n, m);

if (midN == 1) {
return mid;
}
else if (midN == 0) {
low = mid + 1;
}
else {
high = mid - 1;
}
}

return -1;
}
};
```

class Solution {
public:
int func(int mid,int n,int m){
long long ans=1;
for(int i=1;i<=n;i++){
ans=ans*mid;
if(ans>m){
return 2;
}
}
if(ans<m){
return 0;
}
return 1;
}

int nthRoot(int n, int m) {
if(m==0){
return 0;
}
int low=1;
int high=m;
while(low<=high){
int mid=(low+high)/2;
int midN=func(mid,n,m);
if(midN==1){
return mid;
}
else if(midN==0){
low=mid+1;
}
else{
high=mid-1;
}
}
return -1;

}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed100 / 100
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:184

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
16
17

# class Solution:
#     def nthRoot(self, n, m):
#       # code here
#       x = round(m ** (1/n))

#       if x ** n == m:
#           return x
#       return -1
class Solution:
def nthRoot(self, n, m):
x = m ** (1/n)
if x == int(x):
return int(x)
else:
return -1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed100 / 100
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:184

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Nth Root of M](https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1)
