# Distance of nearest cell having 1

## Problem

CoursesSale

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

Distance of nearest cell having 1
Solved

Difficulty: MediumAccuracy: 47.7%Submissions: 129K+Points: 4Average Time: 20m

Given a binary grid[][], where each cell contains either 0 or 1, find the distance of the nearest 1 for every cell in the grid.
The distance between two cells (i1, j1)  and (i2, j2) is calculated as |i1 - i2| + |j1 - j2|.
You need to return a matrix of the same size, where each cell (i, j) contains the minimum distance from grid[i][j] to the nearest cell having value 1.

Note: It is guaranteed that there is at least one cell with value 1 in the grid.

Examples

Input: grid[][] = [[0, 1, 1, 0],
[1, 1, 0, 0],
[0, 0, 1, 1]]
Output: [[1, 0, 0, 1],
[0, 0, 1, 1],
[1, 1, 0, 0]]
Explanation: The grid is -

- 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1), (0,2), (0,2), (2,3), (1,0) and (1,1) respectively.

Input: grid[][] = [[1, 0, 1],
[1, 1, 0],
[1, 0, 0]]
Output: [[0, 1, 0],
[0, 0, 1],
[0, 1, 2]]
Explanation: The grid is -

- 0's at (0,1), (1,2), (2,1) and (2,2) are at a  distance of 1, 1, 1 and 2 from 1's at (0,0), (0,2), (2,0) and (1,1) respectively.

Constraints:
1 ≤ grid.size() ≤ 200
1 ≤ grid[0].size() ≤ 200

Expected Complexities

Time Complexity: O(n * m)
Auxiliary Space: O(n * m)

Company Tags

BloombergAmazonMicrosoftAccentureGoogleFlipkartUberNPCI

Topic Tags

MatrixGraphBFS

Related Articles

Distance Nearest Cell 1 Binary Matrix

Discussions ( 370 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ankit Nayan3 years agoNov 02, 2022 19:19 (GMT +5:30)

Easy C++ Solution with explanation!!!

//Function to find distance of nearest 1 in the grid for each cell.
/*
Hello everyone this is a standerd bfs question as this question asks for
minimum distance from 1. To solve this question we need to follow thease steps.

1.Take all 1's as the base level like a root of tree.
2.Now make a answer matrix and initialize with -1.
3.Find all 1 and push it to queue and update its distance to 0 in the answer matrix.
4.Now traverse to all child of the 1's if the answer[i][j] of the child is -1 then update
the answer by adding 1 to the distance of its parent.
5.Finally return the answer matrix

Similar question:
Rotten oranges
Knight Walk

Upvote if you like!!
*/
vector<vector<int>>nearest(vector<vector<int>>grid)
{
// Code here
int row = grid.size();
int col = grid[0].size();

queue<pair<int,int>> q;
vector<vector<int>> ans(row,vector<int>(col,-1));

for(int i=0;i<row;i++)
{
for(int j=0;j<col;j++)
{
if(grid[i][j]==1) {
q.push({i,j});
ans[i][j]=0;
}
}
}

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0 , 0};

int level=0;

while(!q.empty())
{
int size = q.size();
for(int i=0;i<size;i++) {
int a = q.front().first;
int b = q.front().second;
q.pop();

for(int k=0;k<4;k++)
{
int na = a+dx[k];
int nb = b+dy[k];

if(na<0||nb<0||na>=row||nb>=col||ans[na][nb]!=-1) continue;
q.push({na,nb});
ans[na][nb]=ans[a][b]+1;
}
}
}
return ans;
}

84

Reply
(Show 1 Replies)

Shelly Garg4 days agoSep 26, 2026 09:39 (GMT +5:30)

from collections import deque

class Solution:
def nearest(self, grid):
n = len(grid)
m = len(grid[0])

# Initialize the distance matrix with -1 (representing unvisited)
dist = [[-1] * m for _ in range(n)]
q = deque()

# Multi-source setup: Add all cells with value 1 to the queue
for i in range(n):
for j in range(m):
if grid[i][j] == 1:
dist[i][j] = 0
q.append((i, j))

# Direction arrays for exploring 4 neighbors (Up, Down, Left, Right)
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

# Standard BFS traversal
while q:
r, c = q.popleft()

# Explore all 4 adjacent directions
for i in range(4):
next_r = r + d_row[i]
next_c = c + d_col[i]

# Check grid boundaries and see if the neighbor hasn't been visited yet
if 0 <= next_r < n and 0 <= next_c < m and dist[next_r][next_c] == -1:
dist[next_r][next_c] = dist[r][c] + 1
q.append((next_r, next_c))

return dist

0

Reply

Uday Gupta3 months agoJul 01, 2026 22:25 (GMT +5:30)

class Solution {

/*
* Function to perform Multi-Source BFS.
*
* We use the given grid itself to store:
* 1 -> Original source cell.
* 0 -> Unvisited cell.
* -d -> Visited cell whose distance from the nearest 1 is d.
*
* This avoids using an extra visited or distance matrix.
*/
void bfs(int[][] grid, Queue<ArrayList<Integer>> q) {

int n = grid.length;
int m = grid[0].length;

while (!q.isEmpty()) {

ArrayList<Integer> curr = q.poll();

int x = curr.get(0);
int y = curr.get(1);
int d = curr.get(2);

// Left
if (y - 1 >= 0 && grid[x][y - 1] == 0) {
grid[x][y - 1] = -(d + 1);
q.offer(new ArrayList<>(Arrays.asList(x, y - 1, d + 1)));
}

// Right
if (y + 1 < m && grid[x][y + 1] == 0) {
grid[x][y + 1] = -(d + 1);
q.offer(new ArrayList<>(Arrays.asList(x, y + 1, d + 1)));
}

// Up
if (x - 1 >= 0 && grid[x - 1][y] == 0) {
grid[x - 1][y] = -(d + 1);
q.offer(new ArrayList<>(Arrays.asList(x - 1, y, d + 1)));
}

// Down
if (x + 1 < n && grid[x + 1][y] == 0) {
grid[x + 1][y] = -(d + 1);
q.offer(new ArrayList<>(Arrays.asList(x + 1, y, d + 1)));
}
}
}

/*
* Function to find the distance of the nearest 1 for every cell.
*
* Hello everyone! This is a standard Multi-Source BFS problem.
*
* Instead of creating an extra visited array or distance matrix,
* this solution cleverly reuses the input grid itself.
*
* Approach:
*
* 1. Push every cell containing 1 into the queue.
*    These cells act as multiple BFS sources.
*
* 2. Start BFS simultaneously from all source cells.
*
* 3. Whenever an unvisited 0 is reached:
*      - Store -(distance + 1) inside the grid.
*      - Push the cell into the queue.
*
* 4. Negative values indicate:
*      - The cell has already been visited.
*      - Its absolute value represents the shortest distance
*        from the nearest 1.
*
* 5. Finally,
*      - Convert all negative values back to positive distances.
*      - Convert original 1's to distance 0.
*
*
* If you found this solution helpful, please consider upvoting. 😊
*/

public ArrayList<ArrayList<Integer>> nearest(int[][] grid) {

Queue<ArrayList<Integer>> q = new LinkedList<>();
ArrayList<ArrayList<Integer>> ans = new ArrayList<>();

int row = grid.length;
int col = grid[0].length;

// Push all source cells (1's) into the queue.
for (int i = 0; i < row; i++) {
for (int j = 0; j < col; j++) {
if (grid[i][j] == 1) {
q.offer(new ArrayList<>(Arrays.asList(i, j, 0)));
}
}
}

bfs(grid, q);

// Convert the modified grid into the required answer format.
for (int[] r : grid) {

ArrayList<Integer> temp = new ArrayList<>();

for (int val : r) {

if (val < 0)
temp.add(-val);
else
temp.add(0);
}

ans.add(temp);
}

return ans;
}
}

0

Reply

Ambati Indhu7 months agoMar 04, 2026 17:48 (GMT +5:30)

class Solution {
int x[]={0,1,0,-1};
int y[]={-1,0,1,0};
public ArrayList<ArrayList<Integer>> nearest(int[][] grid) {
// code here
int n=grid.length;
int m=grid[0].length;
boolean vis[][]=new boolean[n][m];
int dist[][]=new int[n][m];
for(int k[]:dist){
Arrays.fill(k,Integer.MAX_VALUE);
}
Queue<Pair>q=new LinkedList<>();
for(int i=0;i<n;i++){
for(int j=0;j<m;j++){
if(grid[i][j]==1){
q.add(new Pair(i,j,0));
vis[i][j]=true;
}
}
}
while(!q.isEmpty()){
Pair p=q.remove();
int row=p.row;
int col=p.col;
int steps=p.steps;
dist[row][col]=Math.min(steps,dist[row][col]);
for(int i=0;i<4;i++){
int ni=row+x[i];
int nj=col+y[i];
if(ni>=0 && nj>=0 && ni<n && nj<m && !vis[ni][nj]){
vis[ni][nj]=true;
q.add(new Pair(ni,nj,steps+1));
}
}

}

ArrayList<ArrayList<Integer>>ans=new ArrayList<>();
for(int i=0;i<n;i++){
ArrayList<Integer>l=new ArrayList<>();
for(int j=0;j<m;j++){
l.add(dist[i][j]);
}
ans.add(l);
}
return ans;
}
}
class Pair{
int row,col,steps;
public Pair(int row,int col,int steps){
this.row=row;
this.col=col;
this.steps=steps;
}
}

0

Reply

REHAN KUMAR7 months agoFeb 21, 2026 14:41 (GMT +5:30)

class Solution {
public:
vector<vector<int>> nearest(vector<vector<int>>& grid)
{
vector<vector<int>>dist(grid.size(),vector<int>(grid[0].size(),-1));
queue<pair<int,int>> q;

for(int i=0;i<grid.size();i++)
{
for(int j=0;j<grid[0].size();j++)
{
if(grid[i][j]==1)
{
q.push({i,j});
dist[i][j]=0;
}
}
}
vector<pair<int,int>>tmp={{-1,0},{0,-1},{1,0},{0,1}};

while(!q.empty())
{
int x=q.front().first;
int y=q.front().second;
q.pop();

for(int i=0;i<4;i++)
{
int nx = x+tmp[i].first;
int ny = y+tmp[i].second;

if(nx>=0 && ny>=0 && nx<n && ny<m && dist[nx][ny]==-1)
{
dist[nx][ny] = dist[x][y] + 1;
q.push({nx, ny});
}
}
}
return dist;
}
};

2

Reply

majnu7 months agoFeb 05, 2026 16:30 (GMT +5:30)

class Solution {
public:
vector<vector<int>> nearest(vector<vector<int>>& grid) {
//we're going to use BFS here as we've to calculate distance which can be calculated levelwise like
//if we've found a cell first level means distance is 1 if next level means 2 and so on....
int n = grid.size();
int m = grid[0].size();
vector<vector<int>> v(n,vector<int>(m));
vector<vector<int>> w(n,vector<int>(m,0));
queue<pair<int,int>> q;
for(int i = 0;i<grid.size();i++){
for(int j = 0;j<grid[0].size();j++){
if(grid[i][j] == 1){
q.push({i,j});
v[i][j] = 0;
}
}
}
int cnt = 0;
q.push({-1,-1});
while(!q.empty()){
int a = q.front().first;
int b = q.front().second;
q.pop();
if(a == -1 && b == -1){
cnt++;
if(!q.empty()){
q.push({-1,-1});
}
continue;
}
w[a][b] = 1;
if(a+1 >= 0 && a+1 < n && w[a+1][b] == 0){
if(grid[a+1][b] == 0){
v[a+1][b] = cnt+1;
w[a+1][b] = 1;
q.push({a+1,b});
}
}
if(a-1 >= 0 && a-1 < n && w[a-1][b] == 0){
if(grid[a-1][b] == 0){
v[a-1][b] = cnt+1;
w[a-1][b] = 1;
q.push({a-1,b});
}
}
if(b-1 >= 0 && b-1 < m && w[a][b-1] == 0){
if(grid[a][b-1] == 0){
v[a][b-1] = cnt+1;
w[a][b-1] = 1;
q.push({a,b-1});
}
}
if(b+1 >= 0 && b+1 < m && w[a][b+1] == 0){
if(grid[a][b+1] == 0){
v[a][b+1] = cnt+1;
w[a][b+1] = 1;
q.push({a,b+1});
}
}
}
return v;
}
};

0

Reply

Manoj Yadav8 months agoJan 12, 2026 13:36 (GMT +5:30)

class Solution {
static int[][] nDistance(int[][] grid)
{
int row=grid.length;
int col=grid[0].length;
int result[][]=new int[row][col];
int visited[][]=new int[row][col];
Queue<int[]> q=new LinkedList<>();
for(int i=0;i<row;i++)
{
for(int j=0;j<col;j++)
{
if(grid[i][j]==1)
{
visited[i][j]=1;
q.add(new int[]{i,j,0});
}
else
{
visited[i][j]=0;
}
}
}
int drow[]={0,-1,0,1};
int dcol[]={-1,0,1,0};

while(!q.isEmpty())
{
int it[]=q.poll();
int nr=it[0];
int nc=it[1];
int d=it[2];
result[nr][nc]=d;
for(int i=0;i<4;i++)
{
int r=nr+drow[i];
int c=nc+dcol[i];
if(r>=0 && r<row && c>=0 && c<col && grid[r][c]==0 && visited[r][c]==0)
{
q.add(new int[]{r,c,d+1});
visited[r][c]=1;
}
}
}
return result;

}
public ArrayList<ArrayList<Integer>> nearest(int[][] grid) {

int result[][]=nDistance(grid);
ArrayList<ArrayList<Integer>> adj=new ArrayList<>();
for(int i=0;i<grid.length;i++)
{
adj.add(new ArrayList<Integer>());
}
for(int i=0;i<grid.length;i++)
{
for(int j=0;j<grid[0].length;j++)
{
adj.get(i).add(result[i][j]);
}
}
return adj;
}
}     solution in java

0

Reply

MOHITH NAIDU SANAPATI9 months agoDec 29, 2025 16:44 (GMT +5:30)

class Solution {
public:
vector<vector<int>> nearest(vector<vector<int>>& grid) {
int n = grid.size();
int m = grid[0].size();
vector<vector<int>>vis(n,vector<int>(m,0));
vector<vector<int>>dist(n,vector<int>(m,0));
queue<pair<pair<int,int>,int>>q;
for(int i=0;i<n;i++){
for(int j=0;j<m;j++){
if(grid[i][j]==1){
q.push({{i,j},0});
vis[i][j]=1;
}else{
vis[i][j]=0;
}
}
}
int nr[] = {1,-1,0,0};
int nc[] = {0,0,1,-1};
while(!q.empty()){
int row = q.front().first.first;
int col = q.front().first.second;
int step = q.front().second;
q.pop();
dist[row][col]=step;
for(int i=0;i<4;i++){
int nrow = row+nr[i];
int ncol = col+nc[i];
if(nrow>=0&&nrow<n&&ncol>=0&&ncol<m&&vis[nrow][ncol]==0){
vis[nrow][ncol]=1;
q.push({{nrow,ncol},step+1});
}
}
}
return dist;
}
};

0

Reply

Krishn vallabh Kumar9 months agoDec 21, 2025 23:59 (GMT +5:30)

from collections import deque

class Solution:

def nearest(self, grid):

n, m = len(grid), len(grid[0])

dist = [[float('inf')] * m for _ in range(n)]

q = deque()

# Enqueue all 1's with distance 0

for i in range(n):

for j in range(m):

if grid[i][j] == 1:

dist[i][j] = 0

q.append((i, j))

directions = [(-1,0),(1,0),(0,-1),(0,1)]

while q:

x, y = q.popleft()

for dx, dy in directions:

nx, ny = x+dx, y+dy

if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] > dist[x][y] + 1:

dist[nx][ny] = dist[x][y] + 1

q.append((nx, ny))

return dist

1

Reply

Abhishek Chaturvedi9 months agoDec 13, 2025 03:42 (GMT +5:30)

class Solution {
public:
vector<vector<int>> nearest(vector<vector<int>>& grid) {
// code here
queue<pair<int, pair<int, int>>> q;
vector<vector<int>> vis(grid.size(), vector<int> (grid[0].size(), 0));
vector<vector<int>> ans(grid.size(), vector<int> (grid[0].size(), 0));
for(int i=0; i<grid.size(); i++){
for(int j=0; j<grid[0].size(); j++){
if(grid[i][j]==1){
q.push(make_pair(0, make_pair(i, j)));
vis[i][j]=1;
ans[i][j]=0;

}

}
}
while(!q.empty()){
auto front= q.front();
q.pop();
int dis= front.first;
int i= front.second.first;
int j= front.second.second;
//check for the 4 dircetions
//left;
if(j-1>=0 and !vis[i][j-1] and grid[i][j-1]==0){
ans[i][j-1]= dis+1;
q.push(make_pair(dis+1, make_pair(i, j-1)));
vis[i][j-1]=1;
}
//right=
if(j+1<grid[0].size() and !vis[i][j+1] and grid[i][j+1]==0){
ans[i][j+1]= dis+1;
q.push(make_pair(dis+1, make_pair(i, j+1)));
vis[i][j+1]= 1;
}
//down
if(i+1<grid.size() and !vis[i+1][j] and grid[i+1][j]==0){
ans[i+1][j]= dis+1;
q.push(make_pair(dis+1, make_pair(i+1, j)));
vis[i+1][j]=1;
}
if(i-1>=0 and !vis[i-1][j] and grid[i-1][j]==0){
q.push(make_pair(dis+1, make_pair(i-1, j)));
vis[i-1][j]=1;
ans[i-1][j]= dis+1;
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

Test Cases Passed1112 / 1112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:255

Time Taken1.26

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
30
31
32
33

from collections import deque
class Solution:
def nearest(self, grid):
# code here
row= len(grid)
col= len(grid[0])
vis=[[0 for _ in range(col)] for _ in range(row)]
dis=[[0 for _ in range(col)] for _ in range(row)]

q=deque()
for r in range(row):
for c in range(col):
if grid[r][c]==1:
q.append((r,c,0))
vis[r][c]=1
while q:
i,j,d=q.popleft()
dis[i][j]=d

for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
new_i=i+x
new_j=j+y
if new_i<0 or new_i>=row or new_j<0 or new_j>=col:
continue
if vis[new_i][new_j]==1:
continue

vis[new_i][new_j]=1
q.append((new_i, new_j, d+1))

return dis

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1112 / 1112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:255

Time Taken1.26

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Distance of nearest cell having 1](https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1)
