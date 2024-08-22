## Problem Statement:

Given a list of connections between individuals in a social network, identify the individuals most likely to be involved in fraudulent activities and those least likely. The problem assumes that:

Fraud occurs only between directly connected individuals.
The top 5 most connected individuals and the next 5 are most and least likely to be involved in fraud, respectively.
Connections are bidirectional.

## Solution Approach:

1- Create a graph: Represent the network as a graph, where nodes are individuals and edges are connections.\
2- Calculate degrees: Determine the degree of each node (number of connections).\
3- Sort nodes: Sort nodes based on their degrees in descending order.

### Calculate percentages:
1- Calculate the total number of connections.\
2- Calculate the total connections for the top 5 and bottom 5 most connected nodes.\
3- Compute the percentage of total connections represented by these two groups.