# Factorial

## Problem

Factorial

The most important part of a GSM network is so called Base Transceiver Station (BTS). These transceivers form the areas called cells (this term gave the name to the cellular phone) and every phone connects to the BTS with the strongest signal (in a little simplified view). Of course, BTSes need some attention and technicians need to check their function periodically.

The technicians faced a very interesting problem recently. Given a set of BTSes to visit, they needed to find the shortest path to visit all of the given points and return back to the central company building. Programmers have spent several months studying this problem but with no results. They were unable to find the solution fast enough. After a long time, one of the programmers found this problem in a conference article. Unfortunately, he found that the problem is so called "Traveling Salesman Problem" and it is very hard to solve. If we have 
𝑁
N BTSes to be visited, we can visit them in any order, giving us 
𝑁
!
N! possibilities to examine. The function expressing that number is called factorial and can be computed as a product:

1.2.3.4....
𝑁
1.2.3.4....N. The number is very high even for a relatively small 
𝑁
N.

The programmers understood they had no chance to solve the problem. But because they have already received the research grant from the government, they needed to continue with their studies and produce at least some results. So they started to study behaviour of the factorial function.

For example, they defined the function 
𝑍
Z. For any positive integer 
𝑁
N, 
𝑍
Z(
𝑁
N) is the number of zeros at the end of the decimal form of number 
𝑁
!
N!. They noticed that this function never decreases. If we have two numbers 
𝑁
1
<
𝑁
2
N
1
 ​

<N
2
 ​

 then 
𝑍
(
𝑁
1
)
≤
𝑍
(
𝑁
2
)
Z(N
1
 ​

)≤Z(N
2
 ​

). It is because we can never "lose" any trailing zero by multiplying by any positive number. We can only get new and new zeros. The function 
𝑍
Z is very interesting, so we need a computer program that can determine its value efficiently.

Input:

There is a single positive integer 
𝑇
T on the first line of input (equal to about 
100000
100000). It stands for the number of numbers to follow. Then there are 
𝑇
T lines, each containing exactly one positive integer number 
𝑁
N, 
1
≤
𝑁
≤
10
9
1≤N≤10
9
.

Output:

For every number 
𝑁
N, output a single line containing the single non-negative integer 
𝑍
(
𝑁
)
Z(N).

Sample 1:
Input
Output
6
3
60
100
1024
23456
8735373
0
14
24
253
5861
2183837
Did you like the problem statement?
96 users found this helpful
More Info
Time limit8 secs
Memory limit1.5 GB
Source Limit50000 Bytes
Contributors

## Problem Link

[Factorial](https://www.codechef.com/problems/FCTRL)
