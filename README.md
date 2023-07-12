# Community-Detection-in-SNS

* Task
  1. 각 블로그 pair들을 구하고, 해당 blog pair의 공통되는 followee들과 그 숫자 구하기
     
  2. Similarity가 가장 높은 top 3 blog pair들을 구하고 해당 Similarity도 구하기
     
  3. blog와 blog가 속해 있는 community가 나온 dataset을 이용하여 각 community에 속한 blog 총 수 구하기
     
  4. (1)에 했던 문제를 medium dataset을 이용해서 mapper와 reducer 수를 다르게하여 total time 비교해보기
</br>

* Implementation
  
  a. Run mapper, reducer file
   ```sh
   hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D mapred.job.name='job' \
	-D mapred.text.key.comparator.options = n \
	-file ./hw1/mapper1.py -mapper mapper1.py \
  -file ./hw1/reducer1.py -reducer reducer1.py \
	-input ./hw1/medium_relation \
	-output ./hw1/output1
   ```
   
  b. Move input file
  ```sh
  hdfs dfs -copyFromLocal hw1/medium_relation ./hw1
  ```

  c. check output file
  ```sh
  hdfs dfs -cat hw1/output1/part-00000 | head -10
  ```

  d. Remove output file
  ```sh
  hdfs dfs -rm -r ./hw1/output1
  ```
