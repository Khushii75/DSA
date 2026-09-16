# Peak element

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

Peak element
Solved

Difficulty: MediumAccuracy: 38.86%Submissions: 652K+Points: 4Average Time: 30m

Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist).

If there are multiple peak elements, Return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].

Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.

Constraints:
1 ≤ arr.size() ≤ 106
-231 ≤ arr[i] < 231

Expected Complexities

Time Complexity: O(log n)
Auxiliary Space: O(1)

Company Tags

AccoliteAmazonVisaAdobeGoogle

Topic Tags

ArraysSearchingBinary Search

Related Interview Experiences

Amazon Interview Experience Set 257 Off Campus

Related Articles

Find A Peak In A Given Array

Discussions ( 1660 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sarika Kumar3 weeks agoAug 23, 2026 11:51 (GMT +5:30)

class Solution:
def peakElement(self, arr):
for i in range(len(arr)-1):
if arr[i] < arr[i+1] and arr[i+1] >arr[i+2]:
print(i+1)
break

0

Reply
(Show 1 Replies)

Anjali Gupta3 weeks agoAug 20, 2026 10:20 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int s =0;
int e = arr.size()-1;
int mid;
while(s<e){
mid=s+(e-s)/2;
if(arr[mid]<arr[mid+1]){
s=mid+1;
}
else{
e=mid;
}

}
return s;
}
};

0

Reply

VINIT KUMAR4 weeks agoAug 18, 2026 23:26 (GMT +5:30)

while(lo<hi) {
int mid=(lo+hi)/2;
if(arr[mid]>arr[mid+1]) hi=mid;
else lo=mid+1;
}
return lo;

0

Reply

Anonymous_Geek1 month agoJul 31, 2026 10:49 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int n=arr.size();
int i=0;
while(arr[i]<arr[i+1]&&i<n-1){i++;}

return i;
}
};

0

Reply

Anonymous_Geek1 month agoJul 31, 2026 10:33 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int n=arr.size();
for(int i=0;i<n;i++){
if((i==0||arr[i]>arr[i-1])&&(i==n-1||arr[i]>arr[i+1])){
return i;
}
}
return -1;
}
};

0

Reply

Shubham Kumar2 months agoJul 18, 2026 20:51 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {
// code here
int start = 0 , end = arr.length-1;
while(start<end){
int mid = (start+end)/2;
if(arr[mid]<arr[mid+1]){
start = mid+1;
}else{
end = mid;
}

}
return start;

}
}

2

Reply

Sai Kiran Ganta2 months agoJul 10, 2026 18:50 (GMT +5:30)

test cases are invalid for the problem

2

Reply

Shivanshu Srivastava(Edited)02/07/2026, 01:51
2 months agoJul 02, 2026 01:46 (GMT +5:30)

int n=arr.size();
int low=1;
int high=n-2;
if(n==1) return 0;
if(arr[0]>arr[1]) return 0;
else if(arr[n-1]>arr[n-2]) return n-1;
while(low<=high){
int mid=low+(high-low)/2;
if(arr[mid]>arr[mid+1] && arr[mid]>arr[mid-1]) return mid;
else if(arr[mid]<arr[mid+1]) low=mid+1;
else high=mid-1;
}
return -1;                                                                                                                                                                                     In this approach when we are deciding whether peak will be on left or right we are checking by if (arr[mid]<arr[mid+1]). This approach because if this condition is satisfied there will be atleast the last element which will be the peak and same for first element.

0

Reply

Shivanshu Srivastava2 months agoJul 02, 2026 01:46 (GMT +5:30)

int n=arr.size();
int low=1;
int high=n-2;
if(n==1) return 0;
if(arr[0]>arr[1]) return 0;
else if(arr[n-1]>arr[n-2]) return n-1;
while(low<=high){
int mid=low+(high-low)/2;
if(arr[mid]>arr[mid+1] && arr[mid]>arr[mid-1]) return mid;
else if(arr[mid]<arr[mid+1]) low=mid+1;
else high=mid-1;
}
return -1;

0

Reply

BODDU NEHRU2 months agoJul 01, 2026 11:08 (GMT +5:30)

class Solution:
def peakElement(self, arr):
low = 0
high = len(arr) - 1

while low <= high:
mid = (low + high) // 2

# Check if mid is a peak element
if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
return mid

# If the left neighbor is greater, the peak lies in the left half
if mid > 0 and arr[mid - 1] > arr[mid]:
high = mid - 1
else:  # Else, the peak lies in the right half
low = mid + 1

return -1  # This case will never be reached

1

Reply

MOHAMED IRFAN A2 months agoJul 01, 2026 09:11 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {
int low = 0;
int high = arr.length - 1;

while (low < high) {
int mid = low + (high - low) / 2;

if (arr[mid] < arr[mid + 1]) {
low = mid + 1;
} else {
high = mid;
}
}

return low;
}
}

0

Reply

FAIZAN AHMED2 months agoJun 26, 2026 16:21 (GMT +5:30)

class Solution:
def peakElement(self, arr):
low = 0
high = len(arr) - 1

while low <= high:
mid = (low + high) // 2

# Check if mid is a peak element
if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
return mid

# If the left neighbor is greater, the peak lies in the left half
if mid > 0 and arr[mid - 1] > arr[mid]:
high = mid - 1
else:  # Else, the peak lies in the right half
low = mid + 1

return -1  # This case will never be reached

0

Reply

SHUBHANG  S RAO2 months agoJun 26, 2026 12:03 (GMT +5:30)

class Solution {

public:

int peakElement(vector<int> &arr) {

/* APPROACH - 1

int n = arr.size();

for (int i = 0; i<n; i++) {

if ((i == 0 || arr[i]>arr[i - 1]) && (i == n - 1 || arr[i]>arr[i + 1])) {return i; }

}

return - 1; */

int n = arr.size();

int i = 0;

while (arr[i]<arr[i + 1] && i<n - 1) {i++; }

return i;

}

};

0

Reply

SHUBHANG  S RAO2 months agoJun 26, 2026 12:03 (GMT +5:30)

class Solution {

public:

int peakElement(vector<int> &arr) {

/* APPROACH - 1

int n = arr.size();

for (int i = 0; i<n; i++) {

if ((i == 0 || arr[i]>arr[i - 1]) && (i == n - 1 || arr[i]>arr[i + 1])) {return i; }

}

return - 1; */

int n = arr.size();

int i = 0;

while (arr[i]<arr[i + 1] && i<n - 1) {i++; }

return i;

}

};

0

Reply

SHUBHANG  S RAO2 months agoJun 26, 2026 12:03 (GMT +5:30)

class Solution {

public:

int peakElement(vector<int> &arr) {

/* APPROACH - 1

int n = arr.size();

for (int i = 0; i<n; i++) {

if ((i == 0 || arr[i]>arr[i - 1]) && (i == n - 1 || arr[i]>arr[i + 1])) {return i; }

}

return - 1; */

int n = arr.size();

int i = 0;

while (arr[i]<arr[i + 1] && i<n - 1) {i++; }

return i;

}

};

0

Reply

SHUBHANG  S RAO2 months agoJun 26, 2026 12:03 (GMT +5:30)

class Solution {

public:

int peakElement(vector<int> &arr) {

/* APPROACH - 1

int n = arr.size();

for (int i = 0; i<n; i++) {

if ((i == 0 || arr[i]>arr[i - 1]) && (i == n - 1 || arr[i]>arr[i + 1])) {return i; }

}

return - 1; */

int n = arr.size();

int i = 0;

while (arr[i]<arr[i + 1] && i<n - 1) {i++; }

return i;

}

};

0

Reply

Vadarevula Venkata Krishna Syam prasad2 months agoJun 22, 2026 12:01 (GMT +5:30)

For this problem, I use a Binary Search approach instead of checking every element. The key observation is that we do not need to find all peak elements; we only need to find any one peak element.

The idea is based on the slope around the middle element. At every step, I compare the middle element with its next element.

If:

arr[mid] < arr[mid + 1]

then I am currently on an increasing slope. This means a peak element must exist on the right side. The reason is that either the array continues increasing until the end, making the last element a peak, or it starts decreasing at some point, creating a peak before that decrease. Therefore, I move to the right half by updating:

low = mid + 1

If:

arr[mid] > arr[mid + 1]

then I am on a decreasing slope. In this case, a peak element must exist on the left side, possibly at the current middle element itself. Therefore, I move to the left half by updating:

high = mid

By repeatedly eliminating half of the search space, the pointers eventually meet at a single index. When "low == high", that position is guaranteed to be a peak element, and I return its index.

One important advantage of this approach is that it automatically handles all edge cases. Whether the peak element is at the first position, last position, or somewhere in the middle, the Binary Search naturally converges to it without requiring any separate checks.

Example

[1,2,3,4]

The array keeps increasing, so the last element becomes the peak.

Output:

index = 3

---

[4,3,2,1]

The array keeps decreasing, so the first element becomes the peak.

Output:

index = 0

Time Complexity

O(log n)

Because the search space is reduced by half in every iteration.

Space Complexity

O(1)

Because only a few variables are used and no extra space is required.

Important Observation

arr[mid] < arr[mid + 1]
→ Peak exists on the right side.

arr[mid] > arr[mid + 1]
→ Peak exists on the left side (including mid).

This observation is the monotonic property that makes Binary Search possible in this problem.

class Solution {
public int peakElement(int[] arr) {
int n=arr.length;
int l=0,h=n-1;

while(l<h){
int mid=l+(h-l)/2;
if(arr[mid]<arr[mid+1]){
l=mid+1;
}else{
h=mid;
}
}
return l;
}
}

2

Reply

Aditya Sharma2 months agoJun 19, 2026 17:49 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {
// code here
int left = 0;
int right = arr.length-1;
while(left<right){
int mid = left +(right-left)/2;
if(arr[mid]>arr[mid+1]){
right = mid;
}else{
left = mid+1;
}
}
return left;
}
}

0

Reply

Madan Mohan3 months agoJun 16, 2026 02:33 (GMT +5:30)

class Solution:
def peakElement(self, arr):
pk_els=-1
if len(arr)==1:
return 0

for i in range(0,len(arr),1):
if i == 0 and ( arr[i]> arr[i+1]):
pk_els = i
elif i==1 and ( arr[i-1]< arr[i]):
pk_els = i
elif i==len(arr)-1 and ( arr[i-1]< arr[i]):
pk_els = i
elif arr[i-1] < arr[i] > arr[i+1]:
pk_els = i

return pk_els

0

Reply

TANISHKA UTEKAR3 months agoJun 06, 2026 18:14 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {

// code here
if(arr.length == 1)return 0;

for (int i = 0 ; i < arr.length; i++){
if(i == 0){
if(arr[0]>arr[1])return i;
}
else if(i == arr.length - 1){
if(arr[arr.length - 1]>arr[arr.length - 2])return i;
}
else{
if(arr[i]>arr[i+1] && arr[i]>arr[i-1])return i;

}
}
return 0;
}
}

0

Reply

PSR YOGESHWAR3 months agoJun 06, 2026 15:17 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int n=arr.size();
int low,mid,high;

if(n==1){
return 0;
}
if(arr[0]>arr[1]){
return 0;
}
if(arr[n-1]>arr[n-2]){
return n-1;
}
low=1;high=n-2;
while(low<=high){
mid=low+(high-low)/2;
if(arr[mid]>arr[mid+1]&&arr[mid]>arr[mid-1]){
return mid;
}
if(arr[mid] < arr[mid + 1]){
low = mid + 1;
}
// Otherwise, it will exist in left subarray
else{
high = mid - 1;}
}
return -1;
}

};

0

Reply

Mayank Ekbote3 months agoJun 06, 2026 11:21 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {

int l = 0 , h = arr.length -1 ;
while(l<h){
int mid = l + (h-l) /2;
if(arr[mid] > arr[mid+1]) h = mid;
else l = mid + 1;
}
return l;
}
}

2

Reply

Mayank Ekbote3 months agoJun 06, 2026 11:21 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {

int l = 0 , h = arr.length -1 ;
while(l<h){
int mid = l + (h-l) /2;
if(arr[mid] > arr[mid+1]) h = mid;
else l = mid + 1;
}
return l;
}
}

1

Reply

Tarun P3 months agoJun 06, 2026 08:54 (GMT +5:30)

python

class Solution:
def peakElement(self, arr):
# Code here
#by using Binary search approach
n=len(arr)
low=0
high=n-1
while low<high:
mid=(low+high)//2
if arr[mid]<arr[mid+1]:
low=mid+1
else:
high=mid
return low
#or return arr.index(max(arr))

0

Reply

Swagata Battacharya3 months agoMay 30, 2026 11:06 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int n=arr.size();
int low,mid,high;

if(n==1){
return 0;
}
if(arr[0]>arr[1]){
return 0;
}
if(arr[n-1]>arr[n-2]){
return n-1;
}
low=1;high=n-2;
while(low<=high){
mid=low+(high-low)/2;
if(arr[mid]>arr[mid+1]&&arr[mid]>arr[mid-1]){
return mid;
}
if(arr[mid] < arr[mid + 1]){
low = mid + 1;
}
// Otherwise, it will exist in left subarray
else{
high = mid - 1;}
}
return -1;
}

};

0

Reply

ashok Sakuru3 months agoMay 23, 2026 21:00 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
int n=arr.size();
int l=0;
int r=n-1;
while(l<=r){
int m=l+(r-l)/2;
if(!(m>0 && arr[m-1]>arr[m]) && !(m<n-1 && arr[m+1]>arr[m]))return m;
if(m>0 && arr[m-1]>arr[m]){
r=m-1;
}
else{
l=m+1;
}
}
}
};

0

Reply

Chetan Bhatt4 months agoMay 08, 2026 15:44 (GMT +5:30)

easy to understand soln in c++...

int peakElement(vector<int> &arr) {
// code here

if(arr.size()<=1) return 0;
//check for
for(int i=0;i<arr.size()-1;i++)
{
if(i==0)
{
if(arr[i]>arr[i+1]) return i;
}

else
if(arr[i]>arr[i-1] && arr[i]>arr[i+1])
return i;
}

//check for 1 ele
//if(arr.size()>=2) if(arr[0]>arr[1]) return true;
if(arr[arr.size()-1] > arr[arr.size()-2]) return arr.size()-1;

return -1;

}

0

Reply

Anonymous_Geek5 months agoApr 18, 2026 21:09 (GMT +5:30)

C++ code

class Solution {
public:
int peakElement(vector<int> &nums) {
int n= nums.size();
if(n==1) return 0;
if(nums[0]>nums[1]) return 0;
if(nums[n-1] > nums[n-2]) return (n-1);
int low = 1,high = n-2;
while(low<=high)
{
int mid = (low+high)/2;

if(nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1])
return mid;

else if(nums[mid] > nums[mid-1] && nums[mid] < nums[mid+1])
{
low = mid+1;
}
else if (nums[mid] < nums[mid-1] && nums[mid] > nums[mid+1])
{
high = mid-1;
}
else
{
low = mid+1;
}
}
return -1;
}
};

0

Reply

Sai Shree G6 months agoMar 13, 2026 14:03 (GMT +5:30)

PYTHON CODE:
class Solution:
def peakElement(self, arr):
low = 0
high = len(arr)-1

while low < high:
mid = (low + high)//2
if arr[mid] < arr[mid + 1]:
low = mid +1
else:
high = mid

return low

0

Reply

Riddhi Agrawal7 months agoFeb 15, 2026 13:19 (GMT +5:30)

class Solution {
public int peakElement(int[] arr)
{
// code here
int n= arr.length;
if(n==1)
return 0;
if(arr[0]>arr[1])
return 0;

if(arr[n-1]>arr[n-2])
return n-1;

int low=1, high=n-2, mid=0;
while(low<=high)
{
mid= (low+high)/2;
if(arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1])
return mid;
if(arr[mid-1]<arr[mid] && arr[mid]<arr[mid+1])
low=mid+1;
else
high=mid-1;
}

return -1;

}
}

1

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 4 / 4Your Total Score:199

Time Taken0.37

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
13
14
15
16
17
18
19
20

class Solution:
def peakElement(self, arr):
n = len(arr)

if n == 1:
return 0

for i in range(n):
if i == 0:
if arr[i] > arr[i + 1]:
return i

elif i == n - 1:
if arr[i] > arr[i - 1]:
return i

elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
return i

return -1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 4 / 4Your Total Score:199

Time Taken0.37

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Peak element](https://www.geeksforgeeks.org/problems/peak-element/1)
