OUTPUT_FOLDER=data/SVO_triples/
IFS="/"
for FILE in data/raw_21Dec/* 
do 
  read -ra ADDR <<<"$FILE"
  python knowledge_graph.py --text_file "$FILE" --output_file "${OUTPUT_FOLDER}${ADDR[-1]}"
done 

