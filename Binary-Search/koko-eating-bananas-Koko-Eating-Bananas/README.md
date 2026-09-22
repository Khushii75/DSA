# Koko Eating Bananas

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

Koko Eating Bananas
Solved

Difficulty: MediumAccuracy: 50.27%Submissions: 66K+Points: 4Average Time: 20m

Koko is given an array arr[], where each element represents a pile of bananas. She has exactly k hours to eat all the bananas.

Each hour, Koko can choose one pile and eat up to s bananas from it.

If the pile has atleast s bananas, she eats exactly s bananas.

If the pile has fewer than s bananas, she eats the entire pile in that hour.

Koko can only eat from one pile per hour.

Your task is to find the minimum value of s (bananas per hour) such that Koko can finish all the piles within k hours.

Examples:

Input: arr[] = [5, 10, 3], k = 4
Output: 5
Explanation: If Koko eats at the rate of 5 bananas per hour:
First pile of 5 bananas will be finished in 1 hour.
Second pile of 10 bananas will be finished in 2 hours.
Third pile of 3 bananas will be finished in 1 hours.
Therefore, Koko can finish all piles of bananas in 1 + 2 + 1 = 4 hours.

Input: arr[] = [5, 10, 15, 20], k = 7
Output: 10
Explanation: If Koko eats at the rate of 10 bananas per hour, it will take 6 hours to finish all the piles.

Constraint:
1 ≤ arr.size() ≤ k ≤ 106
1 ≤ arr[i] ≤ 106

Expected Complexities

Time Complexity: O(n * log(max(arr[i])))
Auxiliary Space: O(1)

Company Tags

BloombergAmazonMicrosoftWalmartAdobeArcesiumUberNPCI

Topic Tags

Binary SearchArrays

Related Articles

Koko Eating Bananas

Discussions ( 170 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ajinkya Nangare1 week agoSep 14, 2026 16:34 (GMT +5:30)

class Solution {

int speedCalculator(int [] arr,int speed,int k){

int totalHours = 0;

for(int pile : arr){

int hours = pile/speed;

if(pile%speed!=0){
hours++;
}
totalHours+=hours;
if(totalHours > k) return totalHours;
}

return totalHours;

}

public int kokoEat(int[] arr, int k) {
int low = 1;
int high = Integer.MIN_VALUE;
int minimumSpeed = Integer.MAX_VALUE;
for(int piles : arr){

high = Math.max(high,piles);

}

while(low<=high){

int mid = low + (high-low)/2;

int totalHours = speedCalculator(arr,mid,k);

if(totalHours <= k){
minimumSpeed = mid;
high = mid -1;

}
else{

low = mid +1;

}

}

return minimumSpeed;

}
}

0

Reply

Sriram Mulukuntla1 month agoAug 09, 2026 12:35 (GMT +5:30)

class Solution {
public static int findMaxEl(int arr[])
{
int max = Integer.MIN_VALUE;
for(int i = 0;i<arr.length;i++)
{
max = Math.max(max,arr[i]);
}
return max;
}
public static int findTotalHours(int arr[],int hourly)
{
int total = 0;
for(int i = 0;i<arr.length;i++)
{
total += (arr[i] + hourly - 1) / hourly;

}
return total;
}
public int kokoEat(int[] arr, int k) {
// code here
int low = 1;
int high = findMaxEl(arr);
while(low <= high)
{
int mid = (low+high)/2;
int totalHours = findTotalHours(arr,mid);
if(totalHours <= k)
{
high = mid - 1;
}
else
{
low = mid + 1;
}
}
return low;
}
}

0

Reply

Kanika Rajput2 months agoJul 13, 2026 23:35 (GMT +5:30)

class Solution {
public:

long long calhours(vector<int>& arr, int speed) {
long long totalHours = 0;

for (int bananas : arr) {
totalHours += (bananas + speed - 1) / speed;
}

return totalHours;
}
int kokoEat(vector<int>& arr, int k) {
int low=1;
int high=*max_element(arr.begin(),arr.end());
int ans=high;
while(low<=high){
int mid=low+(high-low)/2;
long long hours=calhours(arr,mid);
if (hours <= k) {
ans = mid;
high = mid - 1;
}
else {
low = mid + 1;
}
}

return ans;
}

};

1

Reply

FAIZAN AHMED2 months agoJun 26, 2026 17:27 (GMT +5:30)

class Solution:
def kokoEat(self, arr, k):
def canEat(speed):
hours = 0
for bananas in arr:
hours += (bananas + speed - 1) // speed  # Ceiling division
return hours <= k

low, high = 1, max(arr)
ans = high

while low <= high:
mid = (low + high) // 2

if canEat(mid):
ans = mid
high = mid - 1
else:
low = mid + 1

return ans

0

Reply

ved patel3 months agoJun 20, 2026 15:09 (GMT +5:30)

here compleat solution with handel all error cases

class Solution {
public:
int findmaxi(vector<int>& p) {
int m = 0;
for (int i = 0; i < p.size(); i++) {
m = max(m, p[i]);
}
return m;
}
long long findhr(vector<int>& r, int v) {
long long totalhr = 0;
for (int i = 0; i < r.size(); i++) {
totalhr += ((long long)r[i] + v - 1) / v;
}
return totalhr;
}
int kokoEat(vector<int>& arr, int k){
if (k < arr.size()) return -1;
int low = 1;
int high = findmaxi(arr);
while (low <= high) {
int mid = low + (high - low) / 2;
long long th = findhr(arr, mid);
if (th <= k) {
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

Chandrika Naidu3 months agoJun 03, 2026 23:58 (GMT +5:30)

public int kokoEat(int[] arr, int k) {
int size = arr.length;
int max = Arrays.stream(arr).max().getAsInt();
int l = 1;
int h = max;
int answer = max;
while(l<=h){
int mid = l + ((h-l)/2);
long result = calculateHours(arr, mid);
if (result <= k) {
h = mid-1;
answer = mid;
}
else {
l = mid + 1;
}
}

return answer;
}

private long calculateHours(int[] piles, int speed) {

long hours = 0;

for (int pile : piles) {
hours += (pile + speed - 1) / speed;
}

return hours;
}

0

Reply

RAJAN  KUMAR6 months agoMar 24, 2026 09:30 (GMT +5:30)

class Solution {

public boolean canEat(int[] arr, int k, int s) {
long hours = 0;

for (int bananas : arr) {
hours += (bananas + s - 1) / s;
}

return hours <= k;
}

public int kokoEat(int[] arr, int k) {
int low = 1;
int high = 0;

for (int x : arr) {
high = Math.max(high, x);
}

int ans = high;

while (low <= high) {
int mid = low + (high - low) / 2;

if (canEat(arr, k, mid)) {
ans = mid;
high = mid - 1;
} else {
low = mid + 1;
}
}

return ans;
}
}

0

Reply

Rohit Joshi7 months agoFeb 24, 2026 11:04 (GMT +5:30)

class Solution {
public int kokoEat(int[] arr, int k) {
// code here
int low=1, high=0;

for(int elem:arr){
high=Math.max(high,elem);
}

while(low<high){
int m=low+(high-low)/2;
int Totalhrs=0;
for(int elem :arr){
Totalhrs+=(elem +m-1)/m;
}
if(Totalhrs>k){
low=m+1;
}
else{
high=m;
}
}
return low;
}
}

0

Reply

Dharavath Sunil7 months agoFeb 18, 2026 15:22 (GMT +5:30)

class Solution {
public int kokoEat(int[] arr, int k) {
int low=1;

int high = maxValue(arr);
while(low<=high){
int mid = (low+high)/2;
if(mid==0){
low=mid+1;
continue;
}
int totalHrs = func(arr, mid);
if(totalHrs<=k){
high=mid-1;
}else{
low=mid+1;
}
}
return low;
}

public int func(int[] arr, int mid){
int hours = 0;
for(int i=0;i<arr.length;i++){
hours += Math.ceil((double)arr[i]/(double)mid);
}
return hours;
}

public int maxValue(int[] arr){
int max=Integer.MIN_VALUE;
for(int i=0;i<arr.length;i++){
if(arr[i]>max) max=arr[i];
}
return max;
}
}

0

Reply

Anonymous_Geek7 months agoFeb 11, 2026 09:27 (GMT +5:30)

class Solution {
public:
bool isFeasible(vector<int>& arr, int k, int s){
int cnt = 0;
for(int i = 0;i<arr.size();i++){
cnt += ceil((1.0*arr[i])/s);
if(cnt>k)return false;
}
return true;
}
int kokoEat(vector<int>& arr, int k) {
int l = 1, r = 1e6+1, ans = -1;
while(l<=r){
int m = l+(r-l)/2;
if(isFeasible(arr, k, m)){
ans = m;
r = m-1;
}
else{
l = m+1;
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

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:215

Time Taken1.9

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
21
22
23

import math
class Solution:
def banana(self, arr, mid):
s=0
for i in arr:
s+=math.ceil(i/mid)
return s
def kokoEat(self, arr, k):
# Code here
l=1
h=max(arr)
while l<=h:
mid=(l+h)//2
b=self.banana(arr,mid)
if b<=k:
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

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:215

Time Taken1.9

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Koko Eating Bananas](https://www.geeksforgeeks.org/problems/koko-eating-bananas/1)
