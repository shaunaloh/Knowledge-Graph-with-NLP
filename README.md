# Knowledge-Graph-with-NLP

## Data Extraction
[DOCRED](https://github.com/thunlp/DocRED) was used as the dataset for this project. It is a large-scale, document level dataset constructed from Wikipedia and Wikidata, comprising of 3,053 text files. The individual text files were extracted from DOCRED's `train_annotated.json` using the code written in `extracting_train_data.ipynb`.

## Knowledge Graph Implementation
`knowledge_graph.py` was written to execute the following:

### Coreference Resolution
Using python package Coreferee, co-references in each co-reference chain were resolved and replaced to follow a single referent. 
Install Coreferee from the command line by typing: 
```
python -m pip install coreferee
python -m coreferee install en
```
The coreference resolution code works on spaCy models `en_core_web_trf` and `en_core_web_lg`. Install both models ifrom the command line by typing:

``` 
-m spacy download en_coref_lg
-m spacy download en_coref_trf
```

### Generate Entity-Relation Pairs 
Entity-relation pairs (subject-verb-object triples) were extracted from each text. 
- Using spaCy's NLP pipeline, entities and noun chunks were merged to form single entities. This allows compound words or modifiers to be viewed as a single subject/object.
- spaCy's DependencyMatcher was used to match the pattern required of the SVO triple.

### Knowledge Graph Visualisation
NetworkX and Pyvis python packages were used to create an interactive knowledge graph (refer to sample: `nx.html`), to visualise the relationships between entities. An example DOCRED text 'A Charlie Brown Christmas' was used to illustrate how triples were generated and stored in a knowledge graph.

## Bash Script for Multi-File Processing
A bash shell script `run.sh` was written to parallel process all 3,053 DOCRED text files and generate the corresponding triples from each text. To run the pipeline via Git Bash, navigate into the bash script file directory using 'cd <file_path>' and execute: './run.sh'. 
