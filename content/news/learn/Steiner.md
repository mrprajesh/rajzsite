Title: Steiner Tree - PACE 2018
Date: 23.05.2018 13:03:28
Category: Learning Curve
Status: draft
 
 
## Problem Description
- Input : Graph $G(V,E)$, $w: E \rightarrow \mathbb{N}$ and terminals $L \subseteq V$
- Output: Find the minimum weighted $T(V',E')$ that contains all the terminals.

###Initial  Observations:
- If $T = V$ then the problems reduces to Minimum Spannning Tree(MST) Problem.
- If $T = 2$ then the problems reduces to Shortest Path(SP) between two terminal vertices.

## Implementations
There are several exact as well as approximation algorithms for Minimal Steiner tree.
Lets start with the approximation algorithm. The below are few of our implementations:
* MST/Greedy Algorithm - 2 approx
* Sticky tongue Algorithm 
* Snake tongue Algorithm
* Rand Sticky tongue
* Rand Snake tongue

### Code
- Code in C++ - Rajz
- Code in Python - Vj 

## Results 
We are ranked  **16th overall** (scoring 94.57) in PACE 2018 Track C!

## Other links
- [PACE 2018](https://pacechallenge.wordpress.com/pace-2018) 
- Optil.io - [All tracks](https://pacechallenge.wordpress.com/2017/12/12/optil-io/)
- [Optil.io Track C - public Standings!](https://www.optil.io/optilion/problem/3025#tab-4)
- [IPEC](http://algo2018.hiit.fi/ipec/)
