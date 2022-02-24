# Perform the following steps to run the Map Reduce Operations using Hadoop Map Reduce Streaming:

- First Map Reduce Operation: Generate Uni-grams, Bi-grams and Tri-grams and Count Frequency of each N-gram

`mapred streaming --files mapper.py,reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input <HDFS_INPUT_DIRECTORY> -output <1_MAPREDUCE_OUTPUT_HDFS>`

- Second Map Reduce Operation: Map each N-gram to either 1, 2 or 3 and then calculate the probabilities of each N-gram:

`mapred streaming --files mapper2.py,reducer2.py -mapper "python mapper2.py" -reducer "python reducer2.py" -input <1_MAPREDUCE_OUTPUT_HDFS> -output <2_MAPREDUCE_OUTPUT_HDFS>`

- Third Map Reduce (Extra Credit: Find trigram with highest probability containing the string "united states")

`mapred streaming --files mapper3.py,reducer3.py -mapper "python mapper3.py" -reducer "python reducer3.py" -input <2_MAPREDUCE_OUTPUT_HDFS> -output <3_MAPREDUCE_OUTPUT_HDFS>`