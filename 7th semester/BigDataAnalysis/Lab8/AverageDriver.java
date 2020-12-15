package classes;

import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;

public class AverageDriver {

       public static class AverageMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

              public static final int MISSING = 9999;

              public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
                     String line = value.toString();
                     String year = line.substring(15, 19);
                     int temperature;
                     if (line.charAt(87) == '+')
                            temperature = Integer.parseInt(line.substring(88, 92));
                     else
                            temperature = Integer.parseInt(line.substring(87, 92));

                     String quality = line.substring(92, 93);
                     if (temperature != MISSING && quality.matches("[01459]"))
                            context.write(new Text(year), new IntWritable(temperature));
              }
       }

       public static class AverageReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
              public void reduce(Text key, Iterable<IntWritable> values, Context context)
                            throws IOException, InterruptedException {
                     int max_temp = 0;
                     int count = 0;
                     for (IntWritable value : values) {
                            max_temp += value.get();
                            count += 1;
                     }
                     context.write(key, new IntWritable(max_temp / count));
              }
       }

       public static void main(String[] args) throws Exception {
              if (args.length != 2) {
                     System.err.println("Please Enter the input and output parameters");
                     System.exit(-1);
              }

              Job job = new Job();
              job.setJarByClass(AverageDriver.class);
              job.setJobName("Max temperature");

              FileInputFormat.addInputPath(job, new Path(args[0]));
              FileOutputFormat.setOutputPath(job, new Path(args[1]));

              job.setMapperClass(AverageMapper.class);
              job.setReducerClass(AverageReducer.class);

              job.setOutputKeyClass(Text.class);
              job.setOutputValueClass(IntWritable.class);

              System.exit(job.waitForCompletion(true) ? 0 : 1);
       }
}