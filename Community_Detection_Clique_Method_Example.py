#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:34:02 2018

@author: anyagromova
"""
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community 

doc_nodes = [i for i in range(1, 12)]
manuf_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

g_edges=[('A', 1), ('A', 'B'), ('A', 2), ('A','C'), 
         ('B', 3), ('B', 'C'), ('B', 2), 
         ('C', 2), ('C', 1), ('C', 3),
         ('D', 3), ('D', 'C'), ('D', 'H'), ('D', 'E'), ('D', 6), ('D', 5), ('D', 'F'), ('D', 'G'), ('D', 4),
         ('E', 'H'), ('E', 5), ('E', 'F'), ('E', 6), ('E', 'G'),
         ('F', 5), ('F', 'I'), ('F', 8), ('F', 9),
         ('G','H'), ('G', 'D'), ('G', 'I'), ('G', 7), ('G', 4),
         ('H', 5), ('H', 7), ('H', 8), ('H', 'I'), ('H', 'J'), ('H', 'K'), ('H', 9), ('H', 10), ('H', 11), ('H', 12),
         ('I', 8), ('I', 7), ('I', 9), 
         ('J', 12), ('J', 11), ('J', 'K'), ('J', 10),
         ('K', 12), ('K', 11), ('K', 10), 
         (1, 2), (2, 3), (2, 10), (4, 5), (5, 6), (7, 4), (7, 8), (7, 9), (8, 9), (10, 2), (10, 12), 
         (10, 11), (11, 12)]

g = nx.Graph()
g.add_nodes_from(doc_nodes)
g.add_nodes_from(manuf_nodes)
g.add_edges_from(g_edges)
nx.draw(g, with_labels = True)
plt.axis('off')
g
g.edges()

###################### K_Clique Overlapping Community Detection
from networkx.algorithms.community import k_clique_communities
k_click_dict = {}

for i in range(2,6):
    key = 'k_click_{}'.format(i)
    k_click_dict[key] = list(community.k_clique_communities(g,i))
    
community_dict = {}

for k,v in k_click_dict.items():
    n_communities = int(k[-1])
    print('n_communities: ', n_communities)
    communities = [] 
    print(v)
    
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            print('Sets being compared: ', i, j)
            print(v[i].intersection(v[j]))
    print('\n')

