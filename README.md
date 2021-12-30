# Knowledge-Graph-with-NLP

## Data Extraction
DOCRED, a dataset constructed from Wikipedia and Wikidata, was used as the dataset for this project. It comprises of 3,053 text files obtained from https://github.com/thunlp/DocRED. The text files were converted from **train_annotated.json** using the script in **extracting_train_data.ipynb**.

## Generating Entity-Relation Pairs 
knowledge_graph.py was written to extract entity-relation pairs (subject-verb-object triples) from each text.

## Visualising Knowledge Graph
