Title: Dynamic MDS
Date: 26.12.2017 15:03:28
Modified: 01.01.2018 14:53:42
Category: Learning Curve
Tags: Dynamic graphs, Algorithm
Status: draft

## Problem Description
* Input: Tree $T(V,E)$ or forest $F(V,E)$
* Output: Minimum Dominating set(MDS) $D \subseteq V$
* Update: Add leaf node or remove a leaf node.

## Abstract
The Minimum Dominating Set(MDS) problem on a general graph is NP-Hard.
However, MDS problem on an arbitrary graph is solvable in polynomial time(in fact linear time).
In the case of dynamic graphs is there an efficient way to solve MDS during  a
vertex/edge update. 

## Introduction

## Preliminaries and Notations
Objectives working on:

- Dynamic MDS on a tree/forest
	1. Add or remove leaf
	2. Add or remove edge such that $G$ is forest
	3. Add or remove vertex
Let $T$ represent a tree (and $F$ represents the forest).


## Algorithm and Data structure

For each $v \in V$
 
- $v$.dominates = set of vertices that $v$ dominates.
- $v$.dominatedBy = set of vertices dominated by vertex $v$.

### Minimal Dominating Set on trees
A set $D$ is said to be minimal dominating set if not proper subset 
of $D$ is a dominating set.

InsertLeafOf$(u,v)$ {

// $u$ is the existing vertex and $v$ is new vertex

- if $u \notin D$ 
	- add $v$ to $D$
	
}

DeleteLeaf($v$) {

// $v$ is a leaf and $u$ its only neighbour.

- if $v \in D$
	- Remove $v$ from $D$

}

Unlike maximum matching and maximal matching where the relationship is at at most 2, 
the relationship between minimum dominating set and minimal dominating set can be 
arbitrarily large. For example,Star graph has a Minimal DS $D_l$ where $|D_l|= n-1$ and minimum DS $D$ where $|D|=1$.

### Minimum Dominating Set
 status: hidden
Let the forest be represented as $F(V,E)$ where $V$ and $E$ represents
the vertex and edges set at the time instant during the update. 
Let the minimum dominating set is represented as $D$.
The remaining vertices is represented as $\bar D = V \setminus D$.
Assuming the trees in the forest is rooted at some arbitrary vertex.


**Critical vertex:** A vertex $v$ in $D$ is said to be critical if there exist a $u$ 
	in $N[v]$  such that $u$ is dominated only by $v$ and no other vertex.
	It is referred as $v$ is critical because of $u$.
	The vertex $v \in D$ is said to be non-critical if it is not a critical vertex.
	
This following is the crucial observation

**Invariant**: There exist an MDS in $T$ with only the non-leaf nodes
in the dominating set $D$.

This helps in achieving a faster update time.

## Correctness and analysis

## Conclusion
