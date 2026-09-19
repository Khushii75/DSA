# Python solution using `heapq` module:

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

Maximum Overlapping Intervals
Solved

Difficulty: HardAccuracy: 49.41%Submissions: 27K+Points: 8

You are given an array of intervals arr[][], where each interval is represented by two integers [start, end] (inclusive). Return the maximum number of intervals that overlap at any point in time.

Examples :

Input: arr[][] = [[1, 2], [2, 4], [3, 6]]
Output: 2
Explanation: The maximum overlapping intervals are 2(between (1, 2) and (2, 4) or between (2, 4) and (3, 6))

Input: arr[][] = [[1, 8], [2, 5], [5, 6], [3, 7]]
Output: 4
Explanation: The maximum overlapping intervals are 4 (between (1, 8), (2, 5), (5, 6) and (3, 7))

Constraints:
2 ≤ arr.size() ≤ 2 * 104
1 ≤ arr[i][0] < arr[i][1] ≤ 4*106

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(n)

Topic Tags

Prefix SumSortingArraysHash

Related Articles

Maximum Number Of Overlapping Intervals

Discussions ( 56 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Kritika2 months agoJun 28, 2026 15:57 (GMT +5:30)

/*
Pattern:
1. Store all start and end times separately.
2. Sort both arrays.
3. Use two pointers to count active intervals.
4. Update the maximum overlap.

Time Complexity: O(n log n)
Space Complexity: O(n)

Author: Kritika
LinkedIn: https://www.linkedin.com/in/kritika-33312b278/
*/

class Solution {
public:
int overlapInt(vector<vector<int>> &arr) {

int n = arr.size();

vector<int> start;
vector<int> end;

// Store all start and end times
for (int i = 0; i < n; i++) {
start.push_back(arr[i][0]);
end.push_back(arr[i][1]);
}

// Sort start and end times
sort(start.begin(), start.end());
sort(end.begin(), end.end());

int i = 0;
int j = 0;
int curr = 0;
int maxi = 0;

// Count maximum overlapping intervals
while (i < n && j < n) {

if (start[i] <= end[j]) {
curr++;
maxi = max(maxi, curr);
i++;
}
else {
curr--;
j++;
}
}

return maxi;
}
};

0

Reply

Gurshan Grewal7 months agoFeb 20, 2026 18:40 (GMT +5:30)

JAVA SOLUTION
Time Complexity - O(N)
Space Complexity - O(M), where 'M' is maximum element of array

class Solution {
public static int overlapInt(int[][] arr) {

int max = 0;
int n = arr.length;

for(int i=0; i<n; i++){
max = Math.max(max, arr[i][1]);
}

int pref[] = new int[max+1];

for(int i=0; i<n; i++){

int l = arr[i][0];
int r = arr[i][1];

pref[l]++;
if(r+1<=max) pref[r+1]--;
}

int ans = 0;
int sum = 0;

for(int i=0; i<=max; i++){
sum+=pref[i];
ans = Math.max(ans, sum);
}

return ans;
}
}

1

Reply

Julian Hader (Psienix)7 months agoFeb 19, 2026 21:02 (GMT +5:30)

Did this in C. With 2 hardcoded test arrays in main().

#include <stdio.h>
#include <stdlib.h>

void FindDomain(int* arr, int elements, int* min, int* max){
for(int i = 0; i < elements; i++){
int* currentValPTR = arr + i;
if(*currentValPTR < *min) *min = *currentValPTR;
if(*currentValPTR > *max) *max = *currentValPTR;
}
}

int OverlapIntervals(int* arr, int elements, int* min, int* max){
int rangeValue = (*max - *min) + 1;
int* freqArr = calloc(rangeValue, sizeof(int));
for(int i = 0; i < elements; i+=2){
if((arr[i]-*min) < rangeValue) freqArr[(arr[i]-*min)]++;
if((arr[i+1]-*min)+1 < rangeValue)	freqArr[(arr[i+1]-*min)+1]--;
}
int maxOverlap = 0;
int runningCount = 0;
for(int i = 0; i < rangeValue; i++){
runningCount += freqArr[i];
if(runningCount>maxOverlap) maxOverlap = runningCount;
}
free(freqArr);
return maxOverlap;
}

int main(){
int arr1[3][2] = {{1,2},{2,4},{3,6}};
int arr1Min = 4000000;
int arr1Max = 0;
int arr1Elements = sizeof(arr1)/sizeof(arr1[0][0]);
FindDomain(&arr1[0][0], arr1Elements, &arr1Min, &arr1Max);

int arr2[5][2] = {{3,9}, {1,12}, {9,12}, {4,8}, {1,2}};
int arr2Min = 4000000;
int arr2Max = 0;
int arr2Elements = sizeof(arr2)/sizeof(arr2[0][0]);
FindDomain(&arr2[0][0], arr2Elements, &arr2Min, &arr2Max);

printf("%d\n", OverlapIntervals(&arr1[0][0], arr1Elements, &arr1Min, &arr1Max));
printf("%d\n", OverlapIntervals(&arr2[0][0], arr2Elements, &arr2Min, &arr2Max));
return 0;
}

0

Reply

Praharshitha dasari7 months agoFeb 19, 2026 10:59 (GMT +5:30)

class Solution {

public static int overlapInt(int[][] arr) {

// code here

List<int[]> events = new ArrayList<>();

for (int[] log : arr) {

events.add(new int[]{log[0], +1}); // birth

events.add(new int[]{log[1], -1}); // death

}

//if same number then +1 comes before -1

Collections.sort(events, (a, b) -> {

if (a[0] == b[0])

return b[1] - a[1]; // +1 first

return a[0] - b[0];

});

int curr = 0;

int maxPop = 0;

for (int[] e : events) {

curr += e[1];

maxPop=Math .max(curr,maxPop);

}

return maxPop;

}

}

0

Reply

Dharavath Sunil7 months agoFeb 18, 2026 14:54 (GMT +5:30)

class Solution {

public static int overlapInt(int[][] arr) {

// code here

List<int[]> events = new ArrayList<>();

for (int[] log : arr) {

events.add(new int[]{log[0], +1}); // birth

events.add(new int[]{log[1], -1}); // death

}

//if same number then +1 comes before -1

Collections.sort(events, (a, b) -> {

if (a[0] == b[0])

return b[1] - a[1]; // +1 first

return a[0] - b[0];

});

int curr = 0;

int maxPop = 0;

for (int[] e : events) {

curr += e[1];

maxPop=Math .max(curr,maxPop);

}

return maxPop;

}

}

0

Reply

Yachika Mittal7 months agoFeb 18, 2026 14:01 (GMT +5:30)

class Solution {

public:

int overlapInt(vector<vector<int>>& arr) {

vector<pair<int, int>> events;

for(auto& interval : arr) {

events.push_back({interval[0], 1});

events.push_back({interval[1] + 1, -1});

}

sort(events.begin(), events.end());

int max_overlap = 0;

int current = 0;

for(auto& event : events) {

current += event.second;

max_overlap = max(max_overlap, current);

}

return max_overlap;

}

};

0

Reply

Mateusz Dereniowski7 months agoFeb 17, 2026 21:01 (GMT +5:30)

Python solution using `heapq` module:
def overlapInt(self, arr):
from heapq import heappop, heappush
arr.sort()
ends = []
max_overlap = 0
for start, end in arr:
while ends and ends[0] < start:
heappop(ends)
heappush(ends, end)
if (l := len(ends)) > max_overlap:
max_overlap = l
return max_overlap

2

Reply

Mrittika Kundu(Edited)17/02/2026, 21:23
7 months agoFeb 17, 2026 20:44 (GMT +5:30)

Java Solution
Idea:

Why checking the ends and starts fail here?!
- You must have tried the comparison of ending time and starting time of sorted starting time intervals, but it failed.
- It's because unlike the problem "Meeting Rooms" where we needed to detect only "pairwise overlaps", we need to detect "globally active intervals" as well.
- Meeting rooms problem: “Can I attend all meetings without conflict?” -> Just check if any two overlap.
- Maximum overlap problem: “How many meetings are happening at the same time?” -> Need to count all overlaps, not just detect them.
- Meeting rooms -> pairwise conflict detection (adjacency check works).
- Maximum overlap -> global overlap counting (requires sweep line).

Sweep Line Algorithm Approach:

- Collect all start times and end times separately.
- Sort them.
- Traverse through them:
- When you encounter a start -> increment active count.
- When you encounter an end -> decrement active count.
- Track the maximum active count at any point -> that’s the maximum overlap.

Time Complexity: O(n)
Space Complexity: O(n)

Code with comments (for help):

class Solution {
public static int overlapInt(int[][] arr) {

int n = arr.length; //Total number of intervals

//Store start and end times separately
int start[] = new int[n];
int end[] = new int[n];
for(int i = 0;i < n;i++){
start[i] = arr[i][0];
end[i] = arr[i][1];
}

//Sort them
Arrays.sort(start);
Arrays.sort(end);

//Count overlapping intervals
int curr = 0, res = 0, i = 0, j = 0;
while(i < n && j < n){
if(start[i] <= end[j]){
//An interval starts here
//count it
//check if it's the max count
//and move on to the next start with the same end
//as there may be more intervals starting before this end
//waiting to get counted
curr++;
res = Math.max(res, curr);
i++;
}
else{
//No more interval are waiting to get counted before this end
//It's time to move on our end
//to find the correct end for the current start
//But it's necessary to decrement curr count
//As we leave behind the interval which ends here.
//Yes, an interval ends here.
curr--;
j++;
}
}

//Return result
return res;
}
}

Code without comments:

class Solution {
public static int overlapInt(int[][] arr) {

int n = arr.length;

int start[] = new int[n];
int end[] = new int[n];
for(int i = 0;i < n;i++){
start[i] = arr[i][0];
end[i] = arr[i][1];
}

Arrays.sort(start);
Arrays.sort(end);

int curr = 0, res = 0, i = 0, j = 0;
while(i < n && j < n){
if(start[i] <= end[j]){
curr++;
res = Math.max(res, curr);
i++;
}
else{
curr--;
j++;
}
}

return res;
}
}

Things to remember:

- Only update max when an interval starts, not when it ends.
- Don't forget to decrement curr when an interval ends.
- Also, don't forget to move forward even when an interval ends. Never walk backwards.
- After an interval ends, always stay prepared for the next intervals as they may start any moment.
- Get the while loop condition right to make your program terminate properly.
- This is where all your testcases pass!

"In life, it's only the happy memories out of which we find the happiest experience we have ever lived.
Sometimes, we just forget that their end is the ultimate truth.
When happy times start to decline, and become blurred,
Fear not, my friend.
You need to keep walking forward.
End is the sign that another start is nearby.
Instead, do respect the end.
As it's actually the ends that make your happiest memories even HAPPIER."

Hope it helped.

3

Reply

Anonymous_Geek(Edited)17/02/2026, 19:17
7 months agoFeb 17, 2026 19:14 (GMT +5:30)

// thought process of difference array and prefixSum approach                                                                               // Key Idea is that "how many meetings are active at time t(t is discrete value)"                                                             // calculate the "maximum subarray sum on diffArray" -> all the meetings are active at certain time t                            // worst solution :: time ranges >=1e6, use sweep line(almost solves 90% ques) -> in interval question             // best soluttion ::  time range is small && startTime and endTime are discrete values                                                    // Time Complexity : O(N)                                                       // Space Complexity : O(N)

class Solution {
public:
int overlapInt(vector<vector<int>> &arr) {

int maxTime = 0;
for (auto &vec : arr) {
maxTime = max(maxTime, vec[1]);
}

vector<int> diffArray(maxTime + 2, 0);

for (auto &interval : arr) {
int startTime = interval[0];
int endTime   = interval[1];

diffArray[startTime]++;      // meeting starts
diffArray[endTime + 1]--;    // meeting ends AFTER endTime
}

int active = 0, ans = 0;
for (int x : diffArray) {
active += x;
ans = max(ans, active);
}

return ans;
}
};

1

Reply

JEBA   SHINBA7 months agoFeb 17, 2026 18:32 (GMT +5:30)

class Solution:
def overlapInt(self, arr):
n = len(arr)

# Separate start and end times
start = sorted([interval[0] for interval in arr])
end = sorted([interval[1] for interval in arr])

i = 0  # pointer for start
j = 0  # pointer for end
curr_overlap = 0
max_overlap = 0

while i < n and j < n:
# If next event is start (inclusive overlap)
if start[i] <= end[j]:
curr_overlap += 1
max_overlap = max(max_overlap, curr_overlap)
i += 1
else:
curr_overlap -= 1
j += 1

return max_overlap

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 8 / 8Your Total Score:207

Time Taken0.61

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

class Solution:
def overlapInt(self, arr):
# code here
event=[]
for i in arr:
start=i[0] #1st part is starting point
end=i[1]    #2nd part is ending point

event.append([start, 0])
event.append([end, 1])
event.sort()
inside=0
best=0

for j in event:
k=j[1]
if k==0:
inside+=1
best= max(best, inside)
else:
inside-=1
return best

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 8 / 8Your Total Score:207

Time Taken0.61

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Python solution using `heapq` module:](https://www.geeksforgeeks.org/problems/intersecting-intervals/1)
