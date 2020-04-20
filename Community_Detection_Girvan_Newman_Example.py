#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:39:48 2018

@author: anyagromova
"""

import networkx as nx
from networkx.algorithms import community

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd



def get_plot(g, df, savefig = True):
    g = nx.from_pandas_edgelist(df)
    manuf = list(df.target.unique())
    physicians = list(df.source.unique())
    plt.figure(figsize =(7,7))
    layout = nx.spring_layout(g, iterations = 50)
    nx.draw_networkx_nodes(g,
                          layout, 
                          nodelist=manuf, 
                          node_size = 400, # list f sizes based on g.degree
                          node_color = 'lightblue')
    
    nx.draw_networkx_nodes(g, layout, nodelist=physicians, node_color = '#808080', node_size=50)
    popular_phys = [phys for phys in physicians if g.degree(phys) > 1]
    nx.draw_networkx_nodes(g, layout, nodelist=popular_phys, node_color = 'orange', with_label = True, node_size = 50, alpha=0.5)
    nx.draw_networkx_edges(g, layout, width=0.5, edge_color="#C0C0C0")
    node_labels = dict(zip(manuf, manuf))
    nx.draw_networkx_labels(g, layout, labels=node_labels)
    plt.axis('off')
    
    plt.title('Example Network')
    if savefig:
        plt.savefig(r'/Users/anyagromova/Desktop/Documents/Capstone 2018 /Images/example_network.png')
        plt.show()
        
phys_nodes = [i for i in range(17)]
gpo_nodes = ['A', 'B', 'C', 'D']
g_edges = [('A', 0), ('A', 1), ('B', 2), ('B', 3), ('B', 4), ('B', 5), ('C', 6), ('C', 7), 
          ('C', 8), ('C', 9), ('C', 10), ('D', 8), ('D', 9), ('D', 10), ('D', 11), 
          ('D', 12), ('A', 3), ('D', 13), ('A', 14), ('A', 15), ('A', 16)]

def make_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

G = make_graph(phys_nodes+gpo_nodes, g_edges)
df = nx.to_pandas_edgelist(G)
communities = community.girvan_newman(G)



def make_community_graph(community_tuple):
    community_label = 0
    community_labels = []
    G = nx.Graph()
    for item in community_tuple:
        
        item = list(item)
        G.add_nodes_from([element for element in zip(item, [{'community':community_label} for i in range (len(item))])])
        tuple_len = len(item)
        edge_list = [(item[i], item[j]) for i  in range(tuple_len-1) for j in range(i+1, tuple_len)]
        G.add_edges_from(edge_list)
        
        community_labels.append(community_label)
        community_label +=1
    
    color_codes = [ v for k,v in nx.get_node_attributes(G, 'community').items()]
    nx.draw(G, with_labels = True, node_color = color_codes)
    plt.show()
    
count = 0
stop_count = 100
get_plot(G, df, savefig = True)
for item in communities:
    print('Communities:', item)
    make_community_graph(item)
    if count == stop_count:
        break
    count +=1
get_plot(G, df, savefig = True)


