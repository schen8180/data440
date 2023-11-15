# HW5 - Graph Partitioning
### Sophia Chen
### DS 440, Fall 2023
### November 14, 2023

# Assignment

You will investigate the split of the Karate Club (Zachary, 1977), described starting on slide 92 in the Module-07 Social Networks lecture slides. You must use a Python or JavaScript library (as discussed in Module-09 Graph Vis) to generate the graphs required in this assignment. 

# Q1 Color nodes based on final split (2 points)

Draw the original Karate club graph (before the split) and color the nodes according to the factions they belong to (John A and Mr. Hi). This should look similar to the graph on slide 92 - all edges should be present, just indicate the nodes in the eventual split by color.

Q: How many nodes (students) eventually go with John and how many with Mr. Hi?


## Answer

If the graph is split evenly, then 17 students will eventually go with Mr Hi and 17 students with Mr Hi. 

![\label{fig:pre-split}](https://github.com/schen8180/data440/blob/main/hw5/Screen%20Shot%202023-11-15%20at%204.08.56%20PM.png?raw=true)


```python
#!/usr/local/bin/python3
# testargs.py

import matplotlib.pyplot as plt
import networkx as nx
import numpy

G = nx.karate_club_graph()
color = ["#1f78b4"] * 34
color[0] = "orange"  # Mr. Hi has 16 edges
color[33] = "blue"   # John has 17 edges

color_map = []
for node in G:
  if node in G.neighbors(0):
    color_map.append('orange')
  else:
    color_map.append('blue')
nx.draw_spring(G, node_color=color_map, with_labels=True)
plt.show() # first graph
```

## Discussion

I used NetworkX to complete my visualization for this question. First, I iterated over each node in the network G, which is the karate club network graph. Afterwards, since Mr. Hi is node zero according to the notebook module provided for this assignment, I checked to see which nodes are connected to Mr. Hi using the .neighbors() function. If they are connected, then I assigned them to have the color orange. In contrast, if they are not connected, then I assumed that they belonged to John A, and I assigned them to have the color blue. This code returned a network where there is an even split of students that go with Mr. Hi and John A.


# Q2 Use the Girvan-Newman algorithm to illustrate the split (4 points)

We know the final result of the Karate Club split, which you've colored in Q1. Use the Girvan-Newman algorithm to check if the split could have been predicted by the social interactions expressed by edges. How well does the mathematical model represent reality? Generously document your answer with all supporting equations, code, graphs, arguments, etc.

Keeping the node colors the same as they were in Q1, run multiple iterations of the Girvan-Newman graph partioning algorithm (see Module-07 Social Networks, slides 90-99) on the Karate Club graph until the graph splits into two connected components. Include an image of the graph after each iteration in your report.

Note: Implement the Girvan-Newman algorithm (See Module-07, slide 91) rather than relying on a built-in function which hide the intermediate steps. Narrate in your report, the workings of the Girvan-Newman algorithm.

Q: How many iterations did it take to split the graph?

## Answer

It took 11 iterations for the graph to split into two connected components.

![\label{fig:splitting}](https://github.com/schen8180/data440/blob/main/hw5/hw5.png?raw=true)


![\label{fig:post-split}](https://github.com/schen8180/data440/blob/main/hw5/Screen%20Shot%202023-11-15%20at%204.31.11%20PM.png?raw=true)

## Discussion

To complete this task, I utilized the nx.edge_betweenness_centrality() function in NetworkX to find the edge betweenness values. This will allow me to find the edge with the maximum value, which will help me identify the nodes that are connected with both Mr. Hi and John A. These nodes play a crucial role in keeping the overall network connected, and if I remove their edges, then the network will break into more than one connected component.

```

# before the while loop to extract graph from each iteration 
ebc = nx.edge_betweenness_centrality(G)
all_edges_betweenness_list = list(ebc.values())
max_betweenness_value = max(zip(ebc.values(), ebc.keys()))[0]
max_betweenness_edge = max(zip(ebc.values(), ebc.keys()))[1] #edge with maximum betweeness value
G.remove_edge(*max_betweenness_edge)

print(len(list(nx.connected_components(G))))

pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True, node_color=color)


# after the while loop
counter = 0
while len(list(nx.connected_components(G))) <= 1: # this means if the there are 1 big component, in this case
# G has has not been split into more than one component so the the loops keeps iterating until the big network breaks into two 
  counter += 1
  ebc = nx.edge_betweenness_centrality(G)
  all_edges_betweenness_list = list(ebc.values())
  max_betweenness_value = max(zip(ebc.values(), ebc.keys()))[0]
  max_betweenness_edge = max(zip(ebc.values(), ebc.keys()))[1] #edge with maximum betweeness value
  G.remove_edge(*max_betweenness_edge) #removing edge with maximum betweeness value

#components = list(nx.connected_components(G)) #checking to see how many connected compoenents there are, 2 is an indeal number. 
print(counter)
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True, node_color=color)



# to check for the connected  components 
for i in nx.connected_components(G): 
    print(i)
    
# {0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 19, 21} 

# {2, 8, 9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33}


# creating the colors 

color_map = []
for node in G:
  if node in [0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 19, 21]:
    color_map.append('orange')
  else:
    color_map.append('blue')
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()


for ind, arg in enumerate(sys.argv):
    print ("[{}]: {} {}".format(ind,arg,sys.argv[ind]))

```


# Q3 Compare the actual to the mathematical split 

Compare the connected components of the Girvan-Newman split graph (Q2) with the connected components of the actual split Karate club graph (Q1).

Q: Did all of the same colored nodes end up in the same group? If not, what is different?

## Answer

## Discussion

# References 

* Zachary's karate club <https://en.wikipedia.org/wiki/Zachary%27s_karate_club>

* spring_layout, <https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html>

* Color Hex Color Codes, <https://www.color-hex.com/>

* kamada_kawai_layout, <https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.kamada_kawai_layout.html>
* Labels And Colors, <https://networkx.org/documentation/stable/auto_examples/drawing/plot_labels_and_colors.html>

* edge_betweenness_centrality <https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html>

* connected_components <https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.connected_components.html>

* Drawing basics <https://networkx.guide/visualization/basics/>