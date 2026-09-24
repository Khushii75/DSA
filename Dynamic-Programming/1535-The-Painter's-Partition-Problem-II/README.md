# The Painter's Partition Problem-II

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

The Painter's Partition Problem-II
Solved

Difficulty: HardAccuracy: 27.52%Submissions: 197K+Points: 8

Given an array arr[] where each element denotes the length of a board, and an integer k representing the number of painters available. Each painter takes 1 unit of time to paint 1 unit length of a board.
Determine the minimum amount of time required to paint all the boards, under the constraint that each painter can paint only a contiguous sequence of boards (no skipping or splitting allowed).
Examples:
Input: arr[] = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The optimal allocation of boards among 3 painters is -
Painter 1 → [5, 10] → time = 15
Painter 2 → [30] → time = 30
Painter 3 → [20, 15] → time = 35
Job will be done when all painters finish i.e. at time = max(15, 30, 35) = 35
Input: arr[] = [10, 20, 30, 40], k = 2
Output: 60
Explanation: A valid optimal partition is -
Painter 1 → [10, 20, 30] → time = 60
Painter 2 → [40] → time = 40
Job will be complete at time = max(60, 40) = 60
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 1000
Explanation: There is only one painter, so the painter must paint all boards sequentially. The total time taken will be the sum of all board lengths, i.e., 100 + 200 + 300 + 400 = 1000.

Constraints:
1 ≤ arr.size(), k ≤ 105
1 ≤ arr[i] ≤ 104

Expected Complexities

Time Complexity: O(n * log(sum(arr)))
Auxiliary Space: O(1)

Company Tags

MicrosoftGoogleCodenation

Topic Tags

SearchingDynamic ProgrammingDivide and ConquerBinary Search

Related Articles

Painters Partition Problem

Discussions ( 216 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

guptadivyanshu6063 weeks agoSep 02, 2026 12:02 (GMT +5:30)

can anyone please provide me the link for the problem 1 ?

0

Reply

SUDIPTA GHOSH1 month agoAug 08, 2026 14:18 (GMT +5:30)

2. Defining the Search Space

We define the absolute minimum and maximum possible answers:

The Minimum (low): The largest single element in the array (maxi). Why? Because even if you split every single element into its own subarray, the largest sum will be that biggest element.

The Maximum (high): The total sum of the array (sum). Why? This is the worst-case scenario where $k=1$, meaning we cannot make any splits and one subarray must hold everything.

3. The Helper Function (calculate_alloc)

This function greedily checks if a specific limit (mid) is valid.

It iterates through the array, adding elements to a tempSum.

If adding the next element pushes tempSum over the mid limit, it means the current subarray is full. It then forces a split, starts a new subarray (parts++), and resets the sum.

It returns the total number of partitions (parts) needed for that specific limit.

4. The Binary Search Logic

Inside the while loop, we test the middle point (mid) of our search space:

If reqAlloc <= k (Valid): We successfully divided the array into $k$ (or fewer) parts without any part exceeding mid. We save this as a potential answer (ans = mid). However, because we want to minimize the maximum sum, we check if we can get away with an even smaller limit by searching the left half (high = mid - 1).

If reqAlloc > k (Invalid): Our mid limit was too tight. It forced us to slice the array into too many pieces (greater than $k$). We have no choice but to relax the limit by searching the right half (low = mid + 1).

0

Reply

Avantika Deshmukh1 month agoAug 07, 2026 15:40 (GMT +5:30)

class Solution:
def minTime(self, arr, k):
def is_feasible(max_time_allowed):
painters_count = 1
current_board_sum = 0

for board in arr:
if board > max_time_allowed:
return False

if current_board_sum + board > max_time_allowed:
painters_count += 1
current_board_sum = board

if painters_count > k:
return False
else:
current_board_sum += board

return True

if not arr:
return 0

low = max(arr)
high = sum(arr)
ans = high

while low <= high:
mid = (low + high) // 2

if is_feasible(mid):
ans = mid
high = mid - 1
else:
low = mid + 1

return ans

0

Reply

Anonymous_Geek2 months agoJun 30, 2026 13:20 (GMT +5:30)

I think the framing of the question is not correct. What do you guys think?

2

Reply

FAIZAN AHMED2 months agoJun 27, 2026 11:42 (GMT +5:30)

This problem is identical to Allocate Minimum Pages and Split Array Largest Sum. Only the interpretation changes (books → boards, students → painters).

Python 3 Accepted Solution

class Solution:
def minTime(self, arr, k):
def canPaint(maxTime):
painters = 1
curr = 0

for board in arr:
if curr + board <= maxTime:
curr += board
else:
painters += 1
curr = board

return painters <= k

low = max(arr)
high = sum(arr)
ans = high

while low <= high:
mid = (low + high) // 2

if canPaint(mid):
ans = mid
high = mid - 1
else:
low = mid + 1

return ans

Approach

Minimum possible time = max(arr) (a painter must paint the longest board).

Maximum possible time = sum(arr) (one painter paints all boards).

Binary search on the answer.

For each candidate maxTime, greedily assign contiguous boards to the current painter.

If adding the next board exceeds maxTime, assign it to the next painter.

If the required painters are <= k, try a smaller time; otherwise, increase it.

Complexity

Time: O(n × log(sum(arr)))

Space: O(1)

Pattern to Remember

These problems all use the same Binary Search on Answer template:

Allocate Minimum Pages

Split Array Largest Sum

Capacity To Ship Packages Within D Days

Painter's Partition Problem

Book Allocation Problem

Only the names change—the algorithm remains the same.

0

Reply

Ayush Bhardwaj3 months agoJun 08, 2026 17:10 (GMT +5:30)

class Solution {
public:
int minTime(vector<int>& arr, int k) {
// code here
int n = arr.size();

int low = *max_element(arr.begin(),arr.end());
int high = accumulate(arr.begin(),arr.end(),0);

int ans = high;

while(low<=high){
int mid = low + (high-low)/2;
int kt = 1;
int sum = 0;

for(int j=0;j<arr.size();j++){
sum += arr[j];

if(sum>mid){
kt++;
sum = arr[j];
}

if(kt>k)break;
}

if(kt>k){
low = mid+1;
}
else{
ans = mid;
high = mid-1;
}
}

return ans;

}
};

0

Reply

Ayush Bhardwaj3 months agoJun 08, 2026 17:07 (GMT +5:30)

class Solution {
public:
int minTime(vector<int>& arr, int k) {
// code here
int n = arr.size();

int low = *max_element(arr.begin(),arr.end());
int high = accumulate(arr.begin(),arr.end(),0);

for(int i=low;i<=high;i++){
int kt = 1;
int sum = 0;

for(int j=0;j<arr.size();j++){
sum += arr[j];

if(sum>i){
kt++;
sum = arr[j];
}

if(kt>k)break;
}

if(kt<=k)return i;
}

return -1;
}
};

0

Reply

ashok Sakuru4 months agoMay 24, 2026 00:17 (GMT +5:30)

class Solution {
public:
bool solve(vector<int>&arr,int k,int m){
int diff=m;
int cnt=1;
for(int i=0;i<arr.size();i++){
if(diff>=arr[i]){
diff-=arr[i];
}
else{
cnt++;
diff=m-arr[i];
}
}
if(cnt<=k)return true;
return false;
}
int minTime(vector<int> &arr, int k) {
if(k>arr.size())return -1;
int l=*max_element(arr.begin(),arr.end());
int r=accumulate(arr.begin(),arr.end(),0);
int ans=-1;
while(l<=r){
int m=l+(r-l)/2;
if(solve(arr,k,m)){
ans=m;
r=m-1;
}
else{
l=m+1;
}
}
return ans;
}
};

0

Reply

guhan umashankar(Edited)10/04/2026, 11:15
5 months agoApr 10, 2026 11:15 (GMT +5:30)

code in java like a=shortest code 100% working

class Solution {
public int minTime(int[] arr, int k) {
int s = 0, h = 0, a = 0;
for (int x : arr) { s = Math.max(s, x); h += x; }
for (a = h; s <= h; ) {
int m = s + (h - s) / 2, c = 0, p = 1;
for (int x : arr) if ((c += x) > m) { p++; c = x; }
if (p <= k) { a = m; h = m - 1; } else s = m + 1;
}
return a;
}
}

0

Reply

ArnabDey5 months agoApr 09, 2026 21:29 (GMT +5:30)

class Solution {
public:
int minTime(vector<int>& arr, int k) {
// code here
//find max element
int ans = INT_MIN, n=arr.size(),sum=0;
for(int i=0;i<n;i++){
if(arr[i]>ans)
ans = arr[i];
sum += arr[i];
}

int st = ans, end = sum,result=-1;
while(st<=end){
int mid = st+(end-st)/2;

int page = 0, painters =1;
for(int i=0;i<n;i++){
page += arr[i];

if(page>mid)
{
painters ++;
page = arr[i];
}
}

if(painters <= k){
result = mid;
end = mid-1;
}
else st = mid+1;
}

return result;
}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1112 / 1112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 8 / 8Your Total Score:235

Time Taken1.9

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
18
19
20
21
22
23
24
25
26
27

class Solution:
def painting(self, arr, mid):
pntCnt=0
p=1
for i in arr:
if pntCnt+i <= mid:
pntCnt+=i
else:
p+=1
pntCnt=i
return p

def minTime (self, arr, k):
# code here
if (len(arr)<k):
return -1
l=max(arr)
h=sum(arr)
while l<=h:
mid=(l+h)//2
painter=self.painting(arr,mid)
if(painter <= k):
h=mid-1
else:
l=mid+1
return l

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1112 / 1112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 8 / 8Your Total Score:235

Time Taken1.9

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[The Painter's Partition Problem-II](https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1)
