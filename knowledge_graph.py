import argparse
import os.path
from IPython.core.display import HTML

import coreferee
import networkx as nx
from nltk import sent_tokenize
import pandas as pd
from pyvis.network import Network
import spacy
from spacy.matcher import DependencyMatcher
from spacy.pipeline import merge_entities


def coref_resolution(text):
    """
    This function runs through each text and replaces all coreferences within each text.

    Arguments:
    text (str): input text

    Returns:
    coref_doc (str): output text with all coreferences replaced.
    """
    
    nlp = spacy.load('en_core_web_trf')
    nlp.add_pipe('merge_entities')
    nlp.add_pipe('coreferee')

    doc=nlp(text)
    coref_doc=[]
    for token in doc:
        tok = doc._.coref_chains.resolve(token) or token       
        tok_text = ' and '.join([t.text for t in tok]) if(isinstance(tok, list)) else tok.text
        coref_doc.append(tok_text)
        coref_doc=[" ".join(str(item) for item in coref_doc)]
    return (" ".join(coref_doc))


def get_triples(sent):
    """
    This function takes in a subject-verb-object (SVO) pattern and returns all matches
    in the form of SVO triples within the input sentence. A dataframe is then created 
    to store all entity-pairs and their corresponding relations.

    Arguments:
    sent (str): input sentence

    Returns:
    kg_df (dataframe): dataframe of all triples found within the input sentence
    """
    
    sent=coref_resolution(text)
    nlp = spacy.load("en_core_web_trf")
    nlp.add_pipe('coreferee')
    nlp.add_pipe("merge_noun_chunks")
    
    doc=nlp(sent)
    matcher = DependencyMatcher(nlp.vocab)
    pattern = [
    {"RIGHT_ID": "predicate", "RIGHT_ATTRS": {"POS": "VERB"}},
    {"LEFT_ID": "predicate", "REL_OP": ">", "RIGHT_ID": "subject", 
     "RIGHT_ATTRS": {"DEP": "nsubj"}},
    {"LEFT_ID": "predicate", "REL_OP": ">", "RIGHT_ID": "object", 
     "RIGHT_ATTRS": {"DEP": "dobj"}},
    ]
    matcher.add("SVO", [pattern])  
    matches = matcher(doc)
   
    match_ids=[]; token_ids=[];
       
    for i in range(len(matches)):
        match_ids.append(matches[i][0])
        token_ids.append(matches[i][1])

    triple_dict = {"source":[], "relation":[], "target":[]}
    
    for i in range(len(token_ids)):  
        triple_dict["source"].append(doc[token_ids[i][1]].text)
        triple_dict["relation"].append(doc[token_ids[i][0]].text)
        triple_dict["target"].append(doc[token_ids[i][2]].text)
 
    kg_df = pd.DataFrame(triple_dict)
    kg_df.drop_duplicates(inplace=True)
    return kg_df   


def dashboard(kg_df):
    """
    This function takes in a dataframe of SVO triples and visualises a knowledge graph
    in HTML, showing all nodes (subject-object pairs) and edges (relations).

    Arguments:
    kg_df (dataframe): dataframe of triples generated from text file

    Returns:
    net (network): a network graph visualisation of all connecting nodes and edges
    """

    source_list = kg_df["source"].values.tolist()
    relation_list = kg_df["relation"].values.tolist()
    target_list = kg_df["target"].values.tolist()

    net = Network()
    G = nx.from_pandas_edgelist(kg_df, 'source', 'target', edge_attr=True, create_using=nx.MultiDiGraph)
    net.show_buttons(filter_=['nodes', 'edges'])

    for node in G.nodes():
        net.add_node(node)

    for edge in G.edges():
        net.add_edge(edge[0], edge[1], label=relation_list[target_list.index(str(edge[1]))])

    return net.show('nx.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text_file", required=True, type=str)
    parser.add_argument("--output_file", required=True, type=str)
    args = parser.parse_args()

    #if file exists, then skip
    if not os.path.exists(args.output_file.encode("utf-8").decode("utf-8")):
        with open(args.text_file.encode("utf-8").decode("utf-8"), "r") as f:
            text = f.read()
        kg_df = get_triples(text)
        kg_df.to_csv(args.output_file.encode("utf-8").decode("utf-8"), index=False)
    else:
        print("skipping", args.output_file.encode("utf-8").decode("utf-8"))