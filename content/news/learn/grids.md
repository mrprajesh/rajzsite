Title: Grids!
Date: 20.12.2017 15:15:38
Category: Learning Curve
Status: draft
 

## Abstract
The aim is to solve the NP-hard problems(in general graphs) on grids.
Grid is smaller class graph with a nice structural property. 
It is a planar, bipartite and non-chordal graph. 
A $n$ vertex grid has a treewidth $\sqrt n$. 
As we know that the grid can be recognised in linear time, what other problems
on grid can be solved in linear time. 
This is one of the motivation for writing this article. 

#Problem statement
* Input: Finite square grid on $m$ rows and $n$ columns.
* Output: Minimum Vertex cover(MVC), Maximum Independant set(MIS), 
Minimum Dominating set(MDS) and Minimum Fill-in.

## Introduction

Problems that are hard on general graphs
might be solvable in polynomial time in smaller class of graphs. 
If the problem is NP-hard on some _smaller class_ of graphs, then
the problem is also NP hard on _arbitrary_ graphs. Whereas,
if the problem is NP hard on arbitrary graphs, 
then it need not be hard on smaller class of graphs.


## Preliminaries and Notations
Given a $m \times n$- square grid and let the graph corresponding to it is $G(V,E)$.
The total number of vertices and edges of $G$ is $|V|$ and $|E|$ respectively. 
$|V|=mn$ and $|E|=m(n-1)+n(m-1)=2mn-(m+n)$. 
In case the rows and columns are equal i.e $m=n$ then $|V|=n^2$ and $|E|=2n^2-2n$.
Let the vertex set $V = \{0,1, \dots, n^2-1 \}$ 
	represents the vertex numbers from top left
to the right bottom of the grid.

## Algorithms on grid.
### Minimum vertex cover(MVC) Problem and Maximum Independent Set (MIS) Problem
In bipartite graph it is well known that the size of minimum vertex cover 
	is equal to the size of the maximum carnality matching. 
This is the most celebrated König's theorem.
The fastest algorithm known (to the best of our knowledge) for maximum
	cardinality matching on bipartite graphs runs in $O(m \sqrt n )$ time 
Here, $m$ and $n$ represents edges and nodes respectively.
Therefore, the same algorithm can be used to find the MVC on grids.
However we have simpler algorithm which runs linear time.
It does not need to look at the graph to output the MVC.
The independent set and vertex cover are dual to each other. 
If we compute the Minimum vertex cover(MVC) say $S \subset V$ 
	then the Maximum Independent Set(MIS) is $V \setminus S$ and it is straight forward.

#### Vertex Cover algorithm

- $S = \emptyset$
- for(int i=0; i<  m; i++){
	- for(int j=0; j< n; j++){
		- if ( (i+j) % 2 == 1) { // if the sum is an odd value
			- $S = S \cup \{ v_{i+j} \}$

#### Correctness and analysis
**Claim** : Let $G(V,E)$ be a $m,n$ grid and $S \subseteq V$ be a vertex cover of $G$ with the following property: 
If for each edge $e \in E$ there exactly one vertex in $S$ that covers $e$
then, $S$ is a MVC of $G$ 

**Proof** : This claim says it is a minimal vertex cover.

#### Size of the vertex Cover
- The size of the vertex cover is $\lfloor \frac{mn}{2} \rfloor$
- If $n$ and $m$ are both odd number only then the floor would come into picture.

- _Observation_ If any one of $n$ or $m$ is an even number then the MVC and MIS is same.
- Therefore if $n$ and $m$ are both odd, then MIS is V $\setminus S$.

### Minimum Dominating Set(MDS) Problem
The main observations 
### Minimum Fill-in Problem

Claim: There exits a tree decomposition for a graph $G(V,E)$,
such that completing the bags yeilds the minimum fill in edges. 

## Conclusion
      
