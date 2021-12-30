# Knowledge-Graph-with-NLP

## Data Extraction
DOCRED, a dataset constructed from Wikipedia and Wikidata, was used as the dataset for this project. It comprises of 3,053 text files obtained from https://github.com/thunlp/DocRED. The text files were converted from **train_annotated.json** using the code written in **extracting_train_data.ipynb**.

## Knowledge Graph Implementation
**knowledge_graph.py** was written to execute the following:

### Coreference Resolution
Co-references in each co-reference chain were resolved and replaced to follow a single referent.

## Generating Entity-Relation Pairs 
Entity-relation pairs (subject-verb-object triples) were extracted from each text. spaCy's DependencyMatcher was used to match the pattern required of the SVO triple. 

## Visualising Knowledge Graph
