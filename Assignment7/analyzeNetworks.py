import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from artistNetworks import *

def readEdgeList(filename):
    """This function takes one argument (a filename)
    and reads an edge list from a CSV using Pandas."""
    df = pd.read_csv(filename)
    if len(df.columns) > 2:
        print "Warning: Dataframe contains more than two columns.\n"+\
        "This dataframe will be reduced to its first two columns only."
        df = df[df.columns[0:2]]
        pass
    if len(df.columns) == 2:
        return df
    else:
        print "Error: Dataframe nodes invalid. It takes two nodes to make an edge.\n"+\
        "Check function writeEdgeList in artistNetworks.py."
        return

#Example to test. Unhash to test. 
#Must have run example writeEdgeList("6FBDaR13swtiWwGhX1WQsP", 2, "Blink-182.csv")
#Must have run writeEdgeList_byArtist("Sum 41", 2). 
#readEdgeList("Blink-182.csv")


def degree(edgeList, in_or_out):
    """This function measures the number of edges associated with a node.
    Specify 'in' or 'out' to assess the number of in-degree or out-degree edges."""
    if in_or_out == 'in':
        degree_values = edgeList['Artist2'].value_counts()
    elif in_or_out == 'out':
        degree_values = edgeList['Artist1'].value_counts()
    else:
        print("Error: Please type either the option 'in' or the option 'out.'")
        return
    return degree_values


#Examples to test. Unhash to test. 
#edgeList1 = readEdgeList("Blink-182.csv")
#print degree(edgeList1, "in")
#print degree(edgeList1, "out")

def combineEdgeLists(edgeList1, edgeList2):
    """Merges the edge lists of two networks to form a joint networks
    Removes duplicate edges. Will not work with isolated nodes."""
    Joint_network = edgeList1.append(edgeList2)
    Joint_network.drop_duplicates(inplace=True)
    return Joint_network

#Examples to test. Unhash to test. 
#edgeList1 = readEdgeList("Blink-182.csv")
#edgeList2 = readEdgeList("Sum_41.csv")
#print combineEdgeLists(edgeList1, edgeList2)


def pandasToNetworkX(edgeList):
    """Function to create a directed network graph (DiGraph)
    from a given edge list. Function saves the graph as network.jpg
    and opens it with Shell as a subprocess
    Note: will not open with Linnux."""

    Network_edge_data = edgeList.to_records(index=False)
    g = nx.DiGraph()
    for Artist1, Artist2 in Network_edge_data:
        g.add_edge(Artist1, Artist2)
    nx.draw(g, with_labels=False)
    name = str(Artist1)+'_'+str(Artist2)
    plt.savefig(name+"_network.jpg")
    open_call = "open "+name+"_network.jpg"
    #subprocess.call(open_call, shell=True)
    return g

#Examples to test. Unhash to test. 
#edgeList1 = readEdgeList("Blink-182.csv")
#edgeList2 = readEdgeList("Sum_41.csv")
#Joint_network = combineEdgeLists(edgeList1, edgeList2)
#pandasToNetworkX(edgeList1)
#pandasToNetworkX(edgeList2)
#pandasToNetworkX(Joint_network)



def randomCentralNode(inputDiGraph):
    """Function picks the a random but centric node from network data."""

    Ntw_dictionary = nx.eigenvector_centrality(inputDiGraph)
    Ntw_dictionary_sum = float(sum(Ntw_dictionary.itervalues()))
    for key, value in Ntw_dictionary.items():
        Ntw_dictionary[key]= value / Ntw_dictionary_sum
    random_node = np.random.choice(Ntw_dictionary.keys(), p=Ntw_dictionary.values())
    return random_node


#Examples to test. Unhash to test.
#edgeList1 = readEdgeList("Blink-182.csv")
#inputDiGraph = pandasToNetworkX(edgeList1)
#print randomCentralNode(inputDiGraph)




def Joint_NetworkGraph_byArtist(artistname1, depth1, artistname2, depth2):
    """Takes any two artist names and requested depths and outputs a joint
    directed graph of the shared network."""

    filename_str1 = artistname1.replace(' ', '_')
    filename1 = filename_str1+".csv"
    filename_str2 = artistname2.replace(' ', '_')
    filename2 = filename_str2+".csv"

    writeEdgeList_byArtist(artistname1, depth1)
    writeEdgeList_byArtist(artistname2, depth2)

    edgeList1 = readEdgeList(filename1)
    edgeList2 = readEdgeList(filename2)

    Joint_network = combineEdgeLists(edgeList1, edgeList2)
    pandasToNetworkX(Joint_network)

#Examples to test. Unhash to test.
#NetworkGraph_byArtist("Justin Timberlake", 2, "Usher", 2)






