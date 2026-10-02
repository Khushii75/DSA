# Count Islands

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

Count Islands
Solved

Difficulty: MediumAccuracy: 42.12%Submissions: 273K+Points: 4Average Time: 20m

Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'],
['W', 'L', 'W', 'W', 'L'],
['L', 'W', 'W', 'L', 'L'],
['W', 'W', 'W', 'W', 'W'],
['L', 'W', 'L', 'L', 'W']]
Output: 4
Explanation:
The image below shows all the 4 islands in the grid.

Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'],
['W', 'W', 'L', 'L', 'W', 'L', 'W']]
Output: 2
Explanation:
The image below shows 2 islands in the grid.

Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'L', 'W'}

Expected Complexities

Time Complexity: O(n * m)
Auxiliary Space: O(n * m)

Company Tags

PaytmFlipkartAmazonMicrosoftOYO RoomsSamsungSnapdealCitrixD-E-ShawMakeMyTripOla CabsVisaIntuitGoogleLinkedinOperaOne97Streamoid TechnologiesInformaticaWalmartNPCI

Topic Tags

DFSGraph

Related Interview Experiences

Paytm Interview Experience Set 14 For Senior Android DeveloperIntuit Interview Set 8 On CampusPaytm Interview Experience Set 6 Recruitment DrivePaytm Interview Experience Set 7 Written Test HyderabadSamsung Rd Bangalore Freshers Full TimeinternshipAmazon Interview Experience For Software Developer InternMakemytrip Interview Experience Senior Software Engineer Android 3 Years Experienced

Related Articles

Find The Number Of Islands Using Dfs

Discussions ( 1057 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Manish Sah1 year agoOct 06, 2024 23:50 (GMT +5:30)

Key Observations:

Islands: An island is defined as a connected component of adjacent '1's.

Traversal of the Grid: To explore all connected components (islands), we can start from any unvisited '1', then mark all reachable '1's (i.e., part of the same island) as visited using BFS or DFS.

Approach:

This problem can be approached using a graph traversal technique, where we treat each land cell ('1') as a node and an edge exists between two nodes if they are adjacent either horizontally, vertically, or diagonally.

To count the number of islands, we will traverse the grid:

Every time we encounter an unvisited '1', it represents the start of a new island.

From that '1', we will explore all connected land cells (i.e., all cells that are part of this island) using Breadth-First Search (BFS).

We will mark all the connected cells as visited so that we don’t count them again.

Once BFS completes for one island, we increment the island count and continue searching for other unvisited land cells.

Steps to Solve:

Initialization:

Create a visited array to track whether each cell has been visited.

Initialize a counter count to 0, which will store the number of islands.

Grid Traversal:

Traverse through each cell of the grid.

If a cell contains a '1' and hasn’t been visited, it means we’ve found a new island.

Breadth-First Search (BFS):

Use a queue to explore all cells connected to the current starting cell (land '1').

For each cell, check its 8 possible neighbors (up, down, left, right, and the 4 diagonal directions).

If a neighbor is also land ('1') and hasn’t been visited, mark it as visited and add it to the queue for further exploration.

Count Islands:

Every time a new BFS is initiated from an unvisited '1', increment the island count.

Continue this process until all cells in the grid have been visited.

void bfs(int row, int col, vector<vector<int>>& vis, vector<vector<char>>& grid) {
vis[row][col] = 1; // Mark the starting cell as visited
queue<pair<int, int>> q;
q.push({row, col}); // Push the starting cell into the queue

int n = grid.size();
int m = grid[0].size();

// BFS loop: explore all connected '1's (i.e., the current island)
while (!q.empty()) {
int currentRow = q.front().first;
int currentCol = q.front().second;
q.pop();

// Traverse the 8 possible directions (up, down, left, right, and 4 diagonals)
for (int delRow = -1; delRow <= 1; delRow++) {
for (int delCol = -1; delCol <= 1; delCol++) {
int newRow = currentRow + delRow;
int newCol = currentCol + delCol;

// Check if the new position is within bounds, is land, and not visited
if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m
&& grid[newRow][newCol] == '1' && !vis[newRow][newCol]) {
vis[newRow][newCol] = 1; // Mark the new land cell as visited
q.push({newRow, newCol}); // Add it to the queue for further exploration
}
}
}
}
}

int numIslands(vector<vector<char>>& grid) {
int n = grid.size();
int m = grid[0].size();

// Visited array to keep track of explored cells
vector<vector<int>> vis(n, vector<int>(m, 0));
int count = 0; // Island counter

// Traverse the grid cell by cell
for (int row = 0; row < n; row++) {
for (int col = 0; col < m; col++) {
// If the current cell is land and has not been visited, it is a new island
if (!vis[row][col] && grid[row][col] == '1') {
count++; // Increment the island count
bfs(row, col, vis, grid); // Perform BFS to mark the entire island as visited
}
}
}

return count; // Return the total number of islands found
}

Time Complexity:

O(n * m): The grid has n×m cells and each cell is processed exactly once during the traversal and BFS.

Space Complexity:

O(n * m): The space required for the visited array and the BFS queue is proportional to the size of the grid.

4

Reply
(Show 1 Replies)

GeeksforGeeks1 year agoOct 06, 2024 10:56 (GMT +5:30)

Comment of the Day Challenge!

Got a knack for problem-solving? 🧠 Showcase your skills with the most insightful comment and snag a GFG T-shirt!

🔍 Guidelines:

Your comment should offer the clearest explanation and best visualization of the problem and solution.

Think pics or GIFs (Drag and Drop) or slideshows!

No copy-pasting or spamming – originality is key!

Submit your comment in a new thread. For any feedback, drop a comment below. 💬👇

💡 Upvotes, downvotes, or duplicate comments won't make the cut for Comment of the Day.

Winning: Our Marketing Team will ping you via email about your T-shirt and stock availability.

Keep coding, keep cracking, and may your comments be ever insightful!

Regards

Practice Team

4

Reply
(Show 2 Replies)

Ronak Mulani1 month agoAug 27, 2026 15:10 (GMT +5:30)

//Graph (BFS Approach)
class Pair{
int first;
int second;
Pair(int i, int j){
first = i;
second = j;
}
}

class Solution {

int[] rows = {-1,-1,-1,1,1,1,0,0};
int[] columns = {-1,0,1,-1,0,1,-1,1};
int count = 0;
int row;
int col;

boolean valid(int i, int j){

return i>=0 && i<row && j>=0 && j<col;
}

public int countIslands(char[][] grid) {
// Code here
row = grid.length;
col = grid[0].length;
Queue<Pair> q = new LinkedList<>();
for(int i=0;i<row;i++){
for(int j=0;j<col;j++){
if(grid[i][j]=='L'){
//when found L then increse count
count++;
q.offer(new Pair(i,j));
//once it is visited we make it as W. SO, it will not count same cell again
grid[i][j] = 'W';
while(!q.isEmpty()){
Pair p = q.poll();
int r = p.first;
int c = p.second;
for(int k=0;k<8;k++){
if(valid(r+rows[k],c+columns[k]) && grid[r+rows[k]][c+columns[k]]=='L'){
//once it is visited we make it as W. SO, it will not count same cell again
grid[r+rows[k]][c+columns[k]] = 'W';
q.offer(new Pair(r+rows[k],c+columns[k]));
}
}
}
}
}
}
return count;
}
}

0

Reply

Md Musharraf Qurishi4 months agoJun 04, 2026 11:42 (GMT +5:30)

class Solution {
class pair{
int row;
int col;
pair(int row,int col){
this.row = row;
this.col = col;
}
}
private void BFS(int i,int j,char[][]grid,boolean[][]vis){
int m =grid.length, n = grid[0].length;
Queue<pair> q = new LinkedList<>();
q.add(new pair(i,j));
while(q.size()>0){
pair front = q.remove();
int row = front.row , col = front.col;
//top-> row-1,col
if(row>0){
if(vis[row-1][col]==false && grid[row-1][col]=='L'){
q.add(new pair(row-1,col));
vis[row-1][col] = true;
}
}
// bottom-> row+1,col
if((row+1)<m){
if(vis[row+1][col]==false && grid[row+1][col]=='L'){
q.add(new pair(row+1,col));
vis[row+1][col] = true;
}
}
//left->row,col-1.
if(col>0){
if(vis[row][col-1]==false && grid[row][col-1]=='L'){
q.add(new pair(row,col-1));
vis[row][col-1] = true;
}
}
//right->row,col+1.
if((col+1)<n){
if(vis[row][col+1]==false && grid[row][col+1]=='L'){
q.add(new pair(row,col+1));
vis[row][col+1] = true;
}
}
// top-left
if (row > 0 && col > 0) {
if (!vis[row - 1][col - 1] && grid[row - 1][col - 1] == 'L') {
q.add(new pair(row - 1, col - 1));
vis[row - 1][col - 1] = true;
}
}
// top-right
if (row > 0 && (col + 1) < n) {
if (!vis[row - 1][col + 1] && grid[row - 1][col + 1] == 'L') {
q.add(new pair(row - 1, col + 1));
vis[row - 1][col + 1] = true;
}
}
// bottom-left
if ((row + 1) < m && col > 0) {
if (!vis[row + 1][col - 1] && grid[row + 1][col - 1] == 'L') {
q.add(new pair(row + 1, col - 1));
vis[row + 1][col - 1] = true;
}
}
// bottom-right
if ((row + 1) < m && (col+1) < n) {
if (!vis[row + 1][col + 1] && grid[row + 1][col + 1] == 'L') {
q.add(new pair(row + 1, col + 1));
vis[row + 1][col + 1] = true;
}
}
}
}
public int countIslands(char[][] grid) {
// Code here
int m = grid.length,n=grid[0].length;
int count=0;
// create a visited 2-D array.
boolean[][] vis = new boolean[m][n];
// traversal 2D array
for(int i=0;i<m;i++){ // for rwo traversal.
for(int j=0;j<n;j++){ // for column traversal.
if(grid[i][j]=='L' && vis[i][j]==false){
BFS(i,j,grid,vis);
count++;
}
}
}
return count;
}
} // md musharraf (7717764805)for any query.

0

Reply

Ravish Awasthy(Edited)29/04/2026, 21:47
5 months agoApr 29, 2026 21:45 (GMT +5:30)

C++ SOLUTION APPROACH USING DFS AND QUEUES

class Solution {
private:
int rows[8] = { 0 , 0 , -1 , 1, 1, 1, -1, -1};
int cols[8] = { 1, -1 ,  0 , 0, 1, -1, -1, 1};
int tempRow, tempCol;

void solveCountIslands(vector<vector<char>>& grid, int r, int c, int &rowSize, int& colSize)
{
grid[r][c] = 'V';
for(int k = 0 ; k < 8 ; k++)
{
tempRow = r + rows[k];
tempCol = c + cols[k];

if( (tempRow<rowSize && tempRow>=0) && (tempCol<colSize && tempCol>=0))
{
if(grid[tempRow][tempCol]=='L')
solveCountIslands(grid, tempRow, tempCol, rowSize, colSize);
}
}
return;
}
public:
int countIslands(vector<vector<char>>& grid) {
// Code here
queue< pair<int,int> > q;
for(int i = 0 ; i<grid.size(); i++)
{
for(int j=0 ; j<grid[0].size(); j++)
{
if(grid[i][j]=='L')
q.push(make_pair(i,j));
}
}

if(q.empty())
return 0;
int islandCount = 0,r,c;
int rowSize = grid.size(), colSize = grid[0].size();
int firstRow , firstCol;
while(!q.empty())
{
r = q.front().first;
c = q.front().second;
q.pop();
if( grid[r][c] == 'V')
{
grid[r][c] = 'L'; // 2-d vector grid values will remain unchanged, visited nodes
//are still present in queue, so when they will be at upfront for pop, we can assigned it back
// 'L'
continue;
}
else if(grid[r][c] == 'L')
{
firstRow = r;
firstCol = c;
/** for cell marked with 'L', we cannot revert it changes throught queue, so need to assign the row,col value**/
solveCountIslands(grid, r, c, rowSize, colSize);
/** after above functino gets processed, we revert its value**/
grid[firstRow][firstCol] = 'L';
islandCount +=1;
}
}
return islandCount;
}
};

0

Reply

Mukesh Kumar Pathak5 months agoApr 17, 2026 18:18 (GMT +5:30)

class Solution {
public:
int dx[8]={-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8]={-1, 0, 1, 1, 1, 0, -1, -1};

virtual void dfs(int i, int j, vector<vector<char>> &grid){
if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size() || grid[i][j]!='L') return;

grid[i][j]='Z';

for(int k=0; k<8; k++){
int di=i+dx[k];
int dj=j+dy[k];

dfs(di, dj, grid);
}

return;
}

virtual int countIslands(vector<vector<char>>& grid){
if (grid.empty() || grid[0].empty()) return 0;

int n=grid.size(), m=grid[0].size();
int ans=0;

for(int i=0; i<n; i++){
for(int j=0; j<m; j++){
if(grid[i][j]=='L') { ans++; dfs(i, j, grid); }
}
}

for(int i=0; i<n; i++){
for(int j=0; j<m; j++){
if(grid[i][j]=='Z') grid[i][j]='L';
}
}

return ans;
}
};

0

Reply

guhan umashankar5 months agoApr 09, 2026 15:01 (GMT +5:30)

class Solution {
public int countIslands(char[][] grid) {
// Code here
if(grid==null||grid.length==0)return 0;
int rows=grid.length;
int cols=grid[0].length;
// boolean[][]visited=new boolean[rows][cols];
int count=0;
int[][]dirs={{-1, 0}, {1, 0}, {0, -1}, {0, 1},
{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

for(int i=0;i<rows;i++){
for(int j=0;j<cols;j++){
if(grid[i][j]=='L'){
count++;
Queue<int[]>q=new LinkedList<>();
q.add(new int[]{i,j});
grid[i][j]='W';
while(!q.isEmpty()){
int[]curr=q.poll();
int r = curr[0], c = curr[1];
for(int[]d:dirs){
int nr=r+d[0];
int nc=c+d[1];
if(nr>=0&&nr<rows&&nc>=0&&nc<cols&&grid[nr][nc]=='L'){
grid[nr][nc]='W';
q.add(new int[]{nr,nc});
}
}
}
}
}
}
return count;
}
}

0

Reply

Jayanta Nath6 months agoMar 15, 2026 15:35 (GMT +5:30)

Python Clean Approch

class Solution:

def numIslands(self, grid):
# code here
n = len(grid)
m = len(grid[0])
visited = [[0]*m for _ in range(n)]

def find_island(a, b):
if a >= n or b >= m or a < 0 or b < 0: # check the bounds
return
if (grid[a][b] == 'W') or (visited[a][b] == 1): # if visited or water
return

visited[a][b] = 1

directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

for dx, dy in directions:
new_i = a + dx
new_j = b + dy
find_island(new_i, new_j)

ans = 0
for i in range(n):
for j in range(m):
if visited[i][j] == 0 and grid[i][j] != 'W':
ans += 1
find_island(i, j)

return ans

Thanks!

0

Reply

Jayanta Nath6 months agoMar 15, 2026 15:30 (GMT +5:30)

1

Reply

Jayanta Nath6 months agoMar 15, 2026 15:29 (GMT +5:30)

1

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:259

Time Taken0.1

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
24
25
26
27
28
29
30
31

class Solution:
def dfs(self, i, j, vis, grid):
if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
return
if grid[i][j]=="W":
return
if vis[i][j]==1:
return
vis[i][j]=1
self.dfs(i+1, j, vis,grid)
self.dfs(i-1, j, vis,grid)
self.dfs(i, j+1, vis,grid)
self.dfs(i, j-1, vis,grid)
self.dfs(i+1, j-1, vis,grid)
self.dfs(i+1, j+1, vis,grid)
self.dfs(i-1, j-1, vis,grid)
self.dfs(i-1, j+1, vis,grid)

def countIslands(self, grid):
# code here
row=len(grid)
col=len(grid[0])
vis=[[0 for _ in range(col)] for _ in range(row)]
cnt=0
for r in range(row):
for c in range(col):
if grid[r][c]=="L" and vis[r][c]==0:
cnt+=1
self.dfs(r,c,vis,grid)
return cnt

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:259

Time Taken0.1

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Count Islands](https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1)
