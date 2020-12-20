#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappop, heappush, heapify

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#


##############################################################################
#                        Louis Sugy 2019, MIT license                        #
#                                for INSAlgo                                 #
##############################################################################
class UnionFind:
    """An implementation of a Union-Find data structure for hashable types.
       All the elements are given at the start and this class supports only
       the union and find operations, as well as checking if two elements
       belong to the same set.
       These 3 operations have a time complexity O(a(n)), where a is the
       inverse Ackermann function, such that a(n) < 5 for any n that can be
       written in this physical universe.
    """

    def __init__(self, singletons):
        """Initialize the data structure with the elements of the given
           iterable as singletons.
        """
        self.parents = {e: e for e in singletons}
        self.rank = {e: 0 for e in singletons}

    def find(self, e):
        """Return the root of the tree containing the given element, or None
           if the element cannot be found. Applies path compression.
        """
        if e not in self.parents:
            return None
        if self.parents[e] != e:
            self.parents[e] = self.find(self.parents[e])
        return self.parents[e]

    def union(self, e1, e2):
        """Merge the sets containing the elements e1 and e2, by rank.
        """
        r1, r2 = self.find(e1), self.find(e2)
        if r1 == r2:  # The elements are already in the same set
            return
        # We choose that r1 will be the root with highest rank
        if self.rank[r1] < self.rank[r2]:
            r1, r2 = r2, r1
        # We choose r1 as the parent of r2 and update r1's rank
        self.parents[r2] = r1
        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1

    def is_same_set(self, e1, e2):
        """Determines whether e1 and e2 are in the same set.
        """
        return (self.find(e1) == self.find(e2))


def kruskals(g_nodes, g_edges, edges):
    edges.sort()
    uf = UnionFind([i for i in range(1, g_nodes+1)])
    heapify(edges)

    cost = 0
    while edges:
        weight, start, end = heappop(edges)
        if not uf.is_same_set(start, end):
            cost += weight
            uf.union(start, end)
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    edges = []

    for _ in range(g_edges):
        g_from, g_to, g_weight = map(int, input().rstrip().split())
        edges.append((g_weight, g_from, g_to))

    res = kruskals(g_nodes, g_edges, edges)

    # Write your code here.
    fptr.write(str(res) + '\n')
    fptr.close()
