# Minimum Days to Make m Bouquets

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

Minimum Days to Make m Bouquets
Solved

Difficulty: MediumAccuracy: 46.85%Submissions: 40K+Points: 4Average Time: 30m

In a row of flowers, each flower blooms on a specific day. Given an integer array arr[], where arr[i] denotes the day on which the flower at position i blooms.

To make a bouquet, you need to collect k adjacent flowers that have already bloomed. Each flower can be used in at most one bouquet.

Find the minimum number of days required to make m bouquets. If it is impossible to do so, return -1.

Examples:

Input: arr[] = [3, 4, 2, 7, 13, 8, 5], m = 3, k = 2
Output: 8
Explanation: We need to make 3 bouquets, each consisting of 2 adjacent flowers.
-> By day 8, all flowers have bloomed except the flower at position 5 (1-indexed).
-> Form the 1st bouquet using the first 2 flowers.
-> Form the 2nd bouquet using the next 2 flowers.
-> Form the 3rd bouquet using the last 2 flowers.

Input: arr[] = [5, 5, 5, 5, 10, 5, 5], m = 2, k = 3,
Output: 10
Explanation: We need to make 2 bouquets, each consisting of 3 adjacent flowers.
-> By day 5, all flowers have bloomed except the flower at position 5 (1-indexed).
-> We can form the 1st bouquet using the first 3 bloomed flowers.
-> It is not possible to form the 2nd bouquet now.
-> By day 10, all the flowers have bloomed.
-> We can then form 2 bouquets, each consisting of 3 adjacent flowers.

Input: m = 3, k = 2, arr[] = [1, 10, 3, 10, 2]
Output: -1
Explanation: We need to make 3 bouquets, each consisting of 2 flowers.
-> This requires a total of 6 flowers.
-> There are only 5 flowers available.
-> Therefore, it is impossible to make the required bouquets.

Constraints:
1 ≤ k ≤ arr.size() ≤ 105
1 ≤ m ≤ 105
1 ≤ arr[i] ≤ 109

Expected Complexities

Time Complexity: O(n * log(max(arr[i])))
Auxiliary Space: O(1)

Company Tags

BloombergAmazonMicrosoftGoogleFlipkartNPCI

Topic Tags

Binary SearchArrays

Related Articles

Minimum Days To Make M Bouquets

Discussions ( 125 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ajinkya Nangare1 week agoSep 15, 2026 19:34 (GMT +5:30)

class Solution {

public boolean canMakeBouquets(int[] arr,int k,int m ,int day){

int consequtive =0;
int bouquets = 0;

for(int flower : arr){

if(flower <= day){

consequtive++;

if(consequtive == k){

bouquets++;
consequtive =0;

}

}
else{

consequtive=0;

}

if(bouquets>=m) return true;

}

return false;

}

public int minDaysBloom(int[] arr, int k, int m) {
int low = arr[0];
int high = arr[0];
int minDay = -1;
for(int day : arr){

low = Math.min(low,day);
high = Math.max(high,day);

}

while(low<=high){

int mid = low + (high - low)/2;

if(canMakeBouquets(arr,k,m,mid)){

high = mid -1;
minDay = mid;

}
else{

low = mid +1;

}

}

return minDay;
}
}

0

Reply

Kritika2 months agoJul 04, 2026 12:28 (GMT +5:30)

/* BRUTE FORCE
If the total number of flowers required to make all bouquets is more than the flowers available, it is not possible to make the bouquets. So, return -1.
Loop through each day starting from the earliest bloom day to the latest bloom day to test all possible answers.
For each day, check if it's possible to make the required number of bouquets using the flowers that have bloomed by that day. If yes, return that day as the answer.
If no suitable day is found after checking all possibilities, it means it's impossible to make the bouquets. So, return -1.
*/
/* OPTIMAL
If m*k > arr.size: This means we have insufficient flowers. So, it is impossible to make m bouquets and we will return -1.
Next, we will find the maximum element i.e. max(arr[]), and the minimum element i.e. min(arr[]) in the array.
Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to min(arr[]) and the high will point to max(arr[]).
Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division)
Eliminate the halves based on the value returned by possible(): We will pass the potential answer, represented by the variable 'mid' (which corresponds to a specific day), to the 'possible()' function.
If possible() returns true: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
Otherwise, the value mid is smaller than the number we want. This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

-------------------------------------------
PSEUDO CODE
1. If m*k > total flowers -> return -1.
2. Search on answer (days) using Binary Search.
3. For every mid(day), check if making m bouquets is possible.
4. If possible:
Store answer and search left half
(try to find an even smaller day)
5. Otherwise:
Search right half.
Time Complexity: O(N * log(maxBloom-minBloom))
Space Complexity: O(1)
---------------------------------------------------------
*/
class Solution {
public:
bool isPossible(vector<int>& arr, int mid, int m, int k) {
int number = 0;
int count = 0;

for (int i = 0; i < arr.size(); i++) {
if (arr[i] <= mid) {
count++;
} else {
number += count / k;
count = 0;
}
}

number += count / k;

return number >= m;
}

int minDaysBloom(vector<int>& arr, int k, int m) {
long long total = 1LL * k * m;   // ✅ overflow safe
if (total > arr.size()) return -1;

int low = *min_element(arr.begin(), arr.end());
int high = *max_element(arr.begin(), arr.end());

while (low <= high) {
int mid = low + (high - low) / 2;  // ✅ better

if (isPossible(arr, mid, m, k)) {
high = mid - 1;
} else {
low = mid + 1;
}
}

return low;   // ✅ important change
}
};

0

Reply

FAIZAN AHMED2 months agoJun 26, 2026 17:38 (GMT +5:30)

class Solution:
def minDaysBloom(self, arr, k, m):
if m * k > len(arr):
return -1

def canMake(day):
bouquets = 0
flowers = 0

for bloom in arr:
if bloom <= day:
flowers += 1
if flowers == k:
bouquets += 1
flowers = 0
else:
flowers = 0

return bouquets >= m

low, high = min(arr), max(arr)
ans = -1

while low <= high:
mid = (low + high) // 2

if canMake(mid):
ans = mid
high = mid - 1
else:
low = mid + 1

return ans

0

Reply

ved patel3 months agoJun 21, 2026 14:36 (GMT +5:30)

class Solution {
public:
bool possible(vector<int>& arr, int mid, int m, int k) {
int count = 0;
int fools = 0;
for (int i = 0; i < arr.size(); i++) {
if (arr[i] <= mid) {
count++;
} else {
fools += (count / k);
count = 0;
}
}
fools += (count / k);
return fools >= m;
}

int minDaysBloom(vector<int>& bloomDay, int k, int m) {
long long val = 1LL * m * 1LL * k;
if (val > bloomDay.size())
return -1;
int mini = INT_MAX;
int maxi = INT_MIN;
for (int i = 0; i < bloomDay.size(); i++) {
mini = min(mini, bloomDay[i]);
maxi = max(maxi, bloomDay[i]);
}
int low = mini;
int high = maxi;
while (low <= high) {
int mid = low + (high - low) / 2;
if (possible(bloomDay, mid, m, k)) {
high = mid - 1;
} else {
low = mid + 1;
}
}
return low;
}
};

0

Reply

Kritika6 months agoMar 23, 2026 19:20 (GMT +5:30)

class Solution {
public:
bool isPossible(vector<int>& arr, int mid, int m, int k) {
int number = 0;
int count = 0;

for (int i = 0; i < arr.size(); i++) {
if (arr[i] <= mid) {
count++;
} else {
number += count / k;
count = 0;
}
}

number += count / k;

return number >= m;
}

int minDaysBloom(vector<int>& arr, int k, int m) {
long long total = 1LL * k * m;
if (total > arr.size()) return -1;

int low = *min_element(arr.begin(), arr.end());
int high = *max_element(arr.begin(), arr.end());

while (low <= high) {
int mid = low + (high - low) / 2;

if (isPossible(arr, mid, m, k)) {
high = mid - 1;
} else {
low = mid + 1;
}
}

return low;
}
};

0

Reply

Aadityaraj Singh Mandloi6 months agoMar 16, 2026 18:35 (GMT +5:30)

class Solution {
public:
bool isPossible(vector<int> arr, int mid, int m, int k){
int number = 0;
int count = 0;

for(int i = 0; i < arr.size(); i++){
if(arr[i] <= mid) count++;
else {
number += count / k;
count = 0;
}
}

number += count / k;

if(number >= m) return true;
else return false;
}

int minDaysBloom(vector<int>& arr, int k, int m) {
if((k * m) > arr.size()) return -1;

int low = *min_element(arr.begin(), arr.end());
int high = *max_element(arr.begin(), arr.end());
int ans = high;

while(low <= high){
int mid = (low + high) / 2;

int possibility = isPossible(arr, mid, m, k);
if(possibility) {
ans = min(ans, mid);
high = mid - 1;
} else {
low = mid + 1;
}
}

return ans;
}
};

0

Reply

Rohit Joshi7 months agoFeb 24, 2026 15:51 (GMT +5:30)

class Solution {
public int minDaysBloom(int[] arr, int k, int m) {
// code here
int n=arr.length;

int low=Integer.MAX_VALUE;
int high=Integer.MIN_VALUE;

for(int day : arr){
low=Math.min(low,day);
high=Math.max(high,day);
}
int ans=-1;
while(low<=high){
int mid=low+(high-low)/2;
boolean isPossible=canMake(arr,k,m,mid);
if(isPossible){
ans=mid;
high=mid-1;
}
else{
low=mid+1;
}
}
return ans;

}
static boolean canMake(int[] arr,int k, int m, int day){
int flo=0, bou=0;
for(int curday : arr){
if(curday <= day){
flo++;
if(flo==k){
bou++;
flo=0;
}
}else{
flo=0;
}
}
if(bou<m) return false;
else return true;
}
}

0

Reply

Viswanath Reddy Kanagala8 months agoJan 15, 2026 20:40 (GMT +5:30)

class Solution {
public:
bool isValid(vector<int>& arr, long long mid, int k, int m){
int n=arr.size();
int cnt=0;
int bouquets=0;
for(int i=0;i<n;i++){
if(arr[i]<=mid){
cnt++;
if(cnt==k){
bouquets++;
cnt=0;
}
} else{
cnt=0;
}
}
return bouquets>=m;
}

int minDaysBloom(vector<int>& arr, int k, int m) {
int n=arr.size();
long long min=INT_MAX;
long long max=INT_MIN;
for(int i=0;i<n;i++){
if(arr[i]>max){
max=arr[i];
}
if(arr[i]<min){
min=arr[i];
}
}
long long  low=min;
long long high=max;
long long  ans=-1;
while(low<=high){
long long mid=low+(high-low)/2;
bool isValidN=isValid(arr,mid,k,m);
if(isValidN){
ans=mid;
high=mid-1;
}
else{
low=mid+1;
}
}
return ans;
}
};

0

Reply

Krishn vallabh Kumar8 months agoJan 09, 2026 22:05 (GMT +5:30)

class Solution:

def minDaysBloom(self, arr, k, m):

n = len(arr)

# Impossible case

if m * k > n:

return -1

left = min(arr)

right = max(arr)

ans = -1

def canMake(day):

bouquets = 0

flowers = 0

for bloom in arr:

if bloom <= day:

flowers += 1

if flowers == k:

bouquets += 1

flowers = 0

else:

flowers = 0

return bouquets >= m

while left <= right:

mid = (left + right) // 2

if canMake(mid):

ans = mid

right = mid - 1

else:

left = mid + 1

return ans

1

Reply

Dhruv katariya9 months agoDec 09, 2025 17:05 (GMT +5:30)

class Solution {
public:
int solve(int mid, vector<int>& arr,int k){
int n=arr.size();
int count=0,ans=0;
for(int i=0;i<n;i++){
if(arr[i]<=mid){
count++;
if(count==k){
ans++;
count=0;
}
}else{
count=0;
}
}
return ans;
}
int minDaysBloom(vector<int>& arr, int k, int m) {
// Code here
// arrr is given in which we have the time taken for a flower to bloom
// k is the total no of flowers need to make a bouqets
// m is the total no of bouqet we need to make

//so if we see that m*k is the maximum no of bouqets we can make from the given array

int n=arr.size();
if(n<m*k) return -1;

//we know if we take maximum no of days we can make the required bouqets
//O(n)
int high=*max_element(arr.begin(),arr.end()),
low=*min_element(arr.begin(),arr.end());
int ans=high;
while(low<=high){
int mid=high-(high-low)/2;

// mid is the no of days
int bouqets=solve(mid,arr,k); // this will give the total no of bouqets with the given time

// l=2,h=13,m=7

// cout<<bouqets<<",";
if(bouqets>=m){
ans=min(ans,mid);
high=mid-1;
}else{
low=mid+1;
}

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
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:219

Time Taken0.19

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
28
29

class Solution:
def possible(self, arr, k, mid):
cnt=0
noB=0
for i in arr:
if i<=mid:
cnt+=1
if cnt==k:
noB+=1
cnt=0
else:
cnt=0
return noB

def minDaysBloom(self, arr, k, m):
# Code here
if k*m > len(arr):
return -1
l=1
h=max(arr)
while l<=h:
mid=(l+h)//2
b=self.possible(arr, k, mid)
if b>=m:
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

Test Cases Passed1113 / 1113
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:219

Time Taken0.19

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Minimum Days to Make m Bouquets](https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1)
