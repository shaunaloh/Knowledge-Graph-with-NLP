# Knowledge-Graph-with-NLP

## Data Extraction
DOCRED, a dataset constructed from Wikipedia and Wikidata, was used as the dataset for this project. It comprises of 3,053 text files obtained from https://github.com/thunlp/DocRED. The text files were converted from **train_annotated.json** using the code written in **extracting_train_data.ipynb**.

## Knowledge Graph Implementation
**knowledge_graph.py** was written to execute the following:

### Coreference Resolution
Co-references in each co-reference chain were resolved and replaced to follow a single referent. 

### Generating Entity-Relation Pairs 
Entity-relation pairs (subject-verb-object triples) were extracted from each text. 
- entities and noun chunks were merged to form single entities. This allows compound words or modifiers to be viewed as a single subject/object.
- spaCy's DependencyMatcher was used to match the pattern required of the SVO triple.

### Visualising Knowledge Graph
NetworkX and Pyvis python packages were used to create an interative knowledge graph (refer to sample: '**nx.html**'), to visualise the relationships between entities. A example DOCRED text 'A Charlie Brown Christmas' was used to illustrate how triples were generated and stored in a knowledge graph.

### Bash Script for Multi-File Processing
A bash shell script '**run.sh**' was written to parallel process all 3,053 DOCRED text files and generate the corresponding triples from each text.
