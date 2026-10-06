# Sort 0s, 1s and 2s

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

Sort 0s, 1s and 2s
Solved

Difficulty: MediumAccuracy: 50.58%Submissions: 889K+Points: 4Average Time: 10m

Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Examples:
Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 2

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(1)

Company Tags

PaytmFlipkartMorgan StanleyAmazonMicrosoftOYO RoomsSamsungSnapdealHikeMakeMyTripOla CabsWalmartMAQ SoftwareAdobeYatra.comSAP LabsQualcomm

Topic Tags

ArraysSorting

Related Interview Experiences

Paytm Interview Experience Set 14 For Senior Android DeveloperOla Cabs Interview Experience Set 4 For Sde 2Paytm Interview Experience Set 5 Recruitment DriveAmazon Interview Experience For Sde Intership

Related Articles

Sort An Array Of 0s 1s And 2s

Discussions ( 2864 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ayush Kumar2 years agoSep 09, 2024 20:27 (GMT +5:30)

Sorting an Array of 0s, 1s, and 2s Using the Dutch National Flag Algorithm | One Traversal Code.

Intuition

The problem here involves sorting an array containing only 0s, 1s, and 2s. Instead of using standard sorting algorithms (like quicksort or mergesort), we can take advantage of the fact that the array only has three unique values. This enables us to use a more efficient approach called the Dutch National Flag Algorithm, proposed by Edsger W. Dijkstra. This algorithm processes the array in a single pass (O(n) time complexity) by maintaining three pointers to segregate 0s, 1s, and 2s.

Approach

The algorithm maintains three pointers:

low: marks the boundary for 0s (elements before low are all 0).

mid: is used to traverse the array.

high: marks the boundary for 2s (elements after high are all 2).

As we traverse the array:

If the element at mid is 0, we swap it with the element at low and increment both low and mid pointers.

If the element at mid is 1, we simply move mid to the next element.

If the element at mid is 2, we swap it with the element at high and decrement high (without moving mid because the swapped element might need further processing).

This way, we can sort the array in one linear pass without using extra space.

Steps

Initialize three pointers:

low = 0: marks the boundary for 0s.

mid = 0: starts the traversal.

high = n - 1: marks the boundary for 2s.

Traverse the array:

If arr[mid] == 0: Swap arr[mid] with arr[low], and increment both low and mid.

If arr[mid] == 1: Simply move mid forward.

If arr[mid] == 2: Swap arr[mid] with arr[high], and decrement high.

Continue the process until mid surpasses high.

Code with Comments

class Solution {
public:
// Helper function to print the array (for debugging or checking steps)
void printArr(vector<int> &arr) {
for (int x : arr) cout << x << " ";
cout << endl;
}

// Function to sort the array containing 0s, 1s, and 2s
void sort012(vector<int>& arr) {
int n = arr.size();

// Initialize pointers
int low = 0, mid = 0, high = n - 1;

// Traverse the array using the Dutch National Flag Algorithm
while (mid <= high) {
switch(arr[mid]) {
// Case when the element is 0
case 0:
swap(arr[low++], arr[mid++]);  // Swap 0 to the low region and move both pointers
break;

// Case when the element is 1
case 1:
mid++;  // 1 is already in the correct region, so just move mid forward
break;

// Case when the element is 2
case 2:
swap(arr[mid], arr[high--]);  // Swap 2 to the high region and move high backward
break;
}
}
}
};

Explanation of the Code

printArr function: This helper function prints the elements of the array. It is used to help visualize the array at different stages of the algorithm.

sort012 function: Implements the Dutch National Flag Algorithm to sort the array of 0s, 1s, and 2s.

low points to the boundary where 0s end.

mid is used to traverse the array.

high points to the boundary where 2s begin.

Depending on the value of arr[mid], the algorithm performs swaps to place the numbers in the correct region.

Time and Space Complexity

Time Complexity:

The algorithm traverses the array once, making it O(n) where n is the length of the array.

Space Complexity:

The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Key Takeaways

Dutch National Flag Algorithm is perfect for sorting arrays with only three unique elements in linear time.

Two-pointer technique is employed to manage the 0 and 2 boundaries, ensuring the array is sorted efficiently.

The algorithm is in-place, meaning no extra array or significant memory is needed.

32

Reply
(Show 3 Replies)

GeeksforGeeks2 years agoSep 09, 2024 10:14 (GMT +5:30)

Hi Geek,

Only Solution 🤡 Explanation + Approches 🗿

Guideline for everyone to follow for "Comment Of the Day" :-

It will be purely selected by the best explanation and visualization of the problem and approaches.

*One can use Pictures, GIFs, Slideshow or Video for better clarity.*

Upvotes, downvotes, or multiple comments on a thread will not be justified for the Comment of the Day.

Copy-pasting someone's comment or adding the same comment multiple times, will not be considered and leads you into spam/blocked.

Post your submission in a new thread and for any suggestions or feedback, leave a comment below.

Be the 'Comment of the Day' and win a GFG T-shirt daily! Our Marketing Team will contact the winner via email. Check your inbox!

"Marketing team will reach out to the winner a.c to the availability of the stock"

Keep Coding!!

Regards

Practice Team

10

Reply

yuvakishore Varanasi4 weeks agoSep 08, 2026 09:05 (GMT +5:30)

class Solution:
def sort012(self, arr):
# code here
zeros=[]
ones=[]
twos=[]

result=zeros+ones+twos

for i in arr:
if i==0:
zeros.append(i)
elif i==1:
ones.append(i)
else:
twos.append(i)

arr[:]=zeros+ones+twos

0

Reply

Himanshu1 month agoSep 04, 2026 11:56 (GMT +5:30)

class Solution:
def sort012(self, arr):
i = 0
j = 0
k = len(arr) - 1
while j <= k:
if arr[j] == 0:
arr[i],arr[j] = arr[j],arr[i]
i += 1
j += 1
elif arr[j] == 1:
j += 1
else:
arr[j],arr[k] = arr[k],arr[j]
k -= 1
return arr

1

Reply

Yuvraj Kumar(Edited)23/08/2026, 23:59
1 month agoAug 23, 2026 23:58 (GMT +5:30)

So i came up with two appraoches

1. place 0's and 1's correctly using swap functing and two pointer method
the 2's will take care of themselves.

2. traverse the array once and using three variables count the frequency of each digit
Now traverse again and keep checking and changing the values by using which frequency is still pending

0

Reply

Kalam1 month agoAug 19, 2026 22:21 (GMT +5:30)

In JAVA:

class Solution {
public void sort012(int[] arr) {
int zero = 0;
int one = 0;
int two = arr.length - 1;

while (one <= two) {

if (arr[one] == 0) {
int temp = arr[zero];
arr[zero] = arr[one];
arr[one] = temp;

zero++;
one++;
}

else if (arr[one] == 1) {
one++;
}

else {
int temp = arr[one];
arr[one] = arr[two];
arr[two] = temp;

two--;
}
}
}
}

1

Reply

Sachin Kumar1 month agoAug 13, 2026 13:15 (GMT +5:30)

class Solution {
public:
void sort012(vector<int>& arr) {
// code here
vector <int> ans;

sort (arr.begin(), arr.end());

for (int i = 0; i < arr.size(); i++) {
ans.push_back(arr[i]);
}

}
};

0

Reply

Anonymous_Geek2 months agoJul 31, 2026 10:18 (GMT +5:30)

int n=arr.size();
int ones=0;
int zeroes=0;
for(int i=0;i<n;i++){
if(arr[i]==0){zeroes++;}
else if(arr[i]==1){ones++;}
}

for(int i=0;i<zeroes;i++){arr[i]=0;}
for(int i=zeroes;i<zeroes+ones;i++){arr[i]=1;}
for(int i=zeroes+ones;i<n;i++){arr[i]=2;}

1

Reply

Anonymous_Geek2 months agoJul 31, 2026 10:16 (GMT +5:30)

sort(arr.begin(),arr.end());

0

Reply

Christy Xavier2 months agoJul 27, 2026 15:20 (GMT +5:30)

class Solution {
public void sort012(int[] arr) {
// code here
int p = 0;
int q = 0;
int r = arr.length - 1;
while(p <= r){
if(arr[p] == 0){
int a = arr[p];
arr[p] = arr[q];
arr[q] = a;
p++;
q++;
}
else if(arr[p] == 1){
p++;
}
else {
int a = arr[p];
arr[p] = arr[r];
arr[r] = a;
r--;
}

}
}
}

2

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:266

Time Taken0.65

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

class Solution:
def sort012(self, arr):
arr.sort()
return arr

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:266

Time Taken0.65

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Sort 0s, 1s and 2s](https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1)
