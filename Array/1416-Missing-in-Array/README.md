# Missing in Array

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

Missing in Array
Solved

Difficulty: EasyAccuracy: 29.59%Submissions: 1.8MPoints: 2Average Time: 15m

You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size() + 1

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(1)

Company Tags

FlipkartMorgan StanleyAccoliteAmazonMicrosoftD-E-ShawOla CabsPayuVisaIntuitAdobeCiscoQualcommTCSNPCI

Topic Tags

ArraysSearchingBit Magic

Related Interview Experiences

Ola Interview Experience Set 11 InternshipIntuit Interview Experience Set 12Flipkart Interview Experience For Sde 1

Related Articles

Find The Missing Number

Discussions ( 3787 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sarika Kumar1 week agoAug 27, 2026 19:49 (GMT +5:30)

class Solution:
def missingNum(self, arr):
n =len(arr)
for i in range(1, n+1):
if i not in arr:
return i

0

Reply

Anonymous_Geek2 weeks agoAug 18, 2026 14:33 (GMT +5:30)

fh

0

Reply

Prajjwal Kumar(Edited)07/08/2026, 15:59
1 month agoAug 07, 2026 15:46 (GMT +5:30)

class Solution {
public:
int missingNum(vector<int>& arr) {
// code here
int ans=0;
int size=arr.size();
for(int i=0;i<size;i++){

ans=ans^arr[i]^(i+1);
}

ans=ans^(size+1);
return ans;
}
};

LOGIC: Ex- array[4]={ 1, 2, 3, 5}
and we know our array have only digits from 1 to 5 which are also not repeating

we know a property of XOR that is x^x=0, x^y^x=y, x^y^z^z^y=x
(here x,y,z all are number)
which is if we do xor operation and any two same number come then it become zero and 0^x=x

so what we will do in our Ex is  ans=0^arr[o]^arr[1]^arr^[2]^arr[3]^[0+1]^[1+1]^[2+1]^[3+1]
and after loop we will do ans=ans^[size+1 which is 5 here]

so it does 0^1^2^3^5^1^2^3^4^5 and now we know only 4 is not repeating so ans is 4

2

Reply
(Show 1 Replies)

Neeradi Sravanthi1 month agoAug 02, 2026 16:18 (GMT +5:30)

class Solution:
def missingNum(self, arr):
n=len(arr)+1
actual_sum=0
expected_sum=n*(n+1)//2
for i in arr:
actual_sum+=i
return expected_sum-actual_sum

2

Reply

Lalith Narayanan1 month agoAug 02, 2026 13:09 (GMT +5:30)

class Solution {
int missingNum(int arr[]) {
int j=1;
Arrays.sort(arr);
for(int i=0;i<arr.length;i++){
if(arr[i]==j){
j++;
}
else{
break;
}
}

return j;
}

}

1

Reply

Prashant Thakur1 month agoJul 30, 2026 20:16 (GMT +5:30)

class Solution {
int missingNum(int arr[]) {
long n = arr.length + 1;
long sum = n*(n+1)/2;
long arraySum = 0;
for(int ele : arr) {
arraySum += ele;
}
return (int)(sum - arraySum);
}
}

0

Reply

Anonymous_Geek1 month agoJul 30, 2026 18:35 (GMT +5:30)

class Solution {
public:
int missingNum(vector<int>& arr) {
// code here
int n=arr.size();
sort(arr.begin(),arr.end());
int c=1;
for(int i=0;i<n;i++){
if(arr[i]!=c){return c;}
c++;
}
return c;
}
};

0

Reply

Anonymous_Geek1 month agoJul 30, 2026 18:34 (GMT +5:30)

class Solution {
public:
int missingNum(vector<int>& arr) {
// code here
int n=arr.size();
sort(arr.begin(),arr.end());
for(int i=0;i<n;i++){
if(arr[i]!=i+1)return i+1;
}
return n+1;
}
};

1

Reply

Gowrish Gowrish1 month agoJul 22, 2026 21:34 (GMT +5:30)

class Solution {
public:
int missingNum(vector<int>& arr) {
// code here
long long int n = arr.size()+1;
long long int sum = n *(n + 1) / 2;
long long int add = accumulate(arr.begin(), arr.end(), 0);
return sum - add;
}
};

0

Reply

Gowrish Gowrish1 month agoJul 22, 2026 21:34 (GMT +5:30)

class Solution {
public:
int missingNum(vector<int>& arr) {
// code here
long long int n = arr.size()+1;
long long int sum = n *(n + 1) / 2;
long long int add = accumulate(arr.begin(), arr.end(), 0);
return sum - add;
}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:144

Time Taken0.27

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

class Solution:
def missingNum(self, arr):
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
return expected_sum - actual_sum

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:144

Time Taken0.27

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Missing in Array](https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1)
