# comments on graph types

## 1 individual graphs

* cyclic + acyclic instances
* undirected + directed instances

## 2 random graphs

* no structure (?)

## 3 word graphs

* words (5-letter) as vertices
* edge joins u and v if: corresponding words are anagrams OR u and v differ in k positions
* "weights 1"

### 3.1 rusty flavour

* s: "begin"
* t: "rusty" - also only red vertex in graph

### 3.2 common flavour

* None (shortest path avoiding red) is always impossible

## 4 grid graphs

* $N^2$ vertices
* red vertices form "maze-like barriers"
* 1 unique path from s to t, which avoids red vertices
* 1 unique path from s to t, which alternates color of vertices
* in grid-N-1 some random red vertices have turned non-red (so there are ‘holes’ in the hedges)
* in grid-N-2 some random non-red vertices have turned red (so some passages are blocked)

## 5 wall graphs

implementation of __Some.py__ is especially tricky for this

* undirected
* made of bricks
* bricks are walls of height 2
* each wall has a single red vertex `w`, the right-most vertex at same level as vertex 0
* what are n, p, z ?

## 6 ski graphs

* directed
* right or left from every vertex (until last layer)
* has to "look forward" more than one layer, in order to not get stuck on a path that will lead to the Yeti (red vertex)

## 7 increasing numbers

* directed
* u --> v; can only exist if u < v
* odd numbers are red
* s = $α_1$
* t = $α_n$
* There is an edge from $α_i$ to $α_j$ if i<j and $α_i$ < $α_j$.
