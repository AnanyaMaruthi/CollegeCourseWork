# It finally works! DAMN

#### Configure stuff properly:

> 1. mapred-site.xml [use this](https://stackoverflow.com/questions/50719585/unable-to-run-mapreduce-wordcount)
> 2. Others [use this](https://www.edureka.co/blog/install-hadoop-single-node-hadoop-cluster)

#### Executing stuff:

1. Compile java file using `javac WordCount.java -cp $(/usr/local/hadoop/bin/hadoop classpath)`

2. Move all class files into a folder [classes](classes/)

3. Create a Manifest file [manifest.mf](manifest.mf)

4. Create a jar file `jar -cvmf WordCount.jar manifest.mf classes.` [Refer this](https://docs.oracle.com/javase/tutorial/deployment/jar/build.html)

5. Verify if jar file is built correctly `java -jar WordCount.jar` (P.S. You'll get hadoop errors tho)

6. Create the [input file](textfile.txt)

7. View hadoop file system `hadoop fs -ls /`

8. Create a new directory (if needed) `hadoop fs -mkdir /lab`

9. Move the input file to hadoop filesystem `hadoop fs -copyFromLocal /path/to/input/file /path/in/hadoop/fs`
   For example `hadoop fs ./textfile.txt /lab`

10. Execute Map reduce program `hadoop jar WordCount.jar /lab/textfile.txt /output`

11. Check for the newly created folder `hadoop fs -ls /output`

12. Display output on terminal `hadoop fs -cat /output/part-00000`

# Annnnnd We're done! YAAAY!!

> Remember, alias hadoop='/usr/local/hadoop/bin/hadoop'
