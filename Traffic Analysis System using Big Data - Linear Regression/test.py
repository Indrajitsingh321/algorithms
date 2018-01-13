
import os
#os.system("start-all.sh")
location=raw_input("Enter the location: ")
sub_location=raw_input("Enter the sub_location: ")
time=raw_input("Enter the time: ")
ss="map.py"
f = open(ss,'w')
b="#!/usr/bin/env python"+"\n"+"import sys"+"\n"+"for line in sys.stdin:"+"\n\t"+"line = line.strip()"+"\n\t"+"words = line.split(',')"+"\n\t"+"if words[2]=="+"\'\""+location+"\"\'"+" and words[7]=="+"\'\""+sub_location+"\"\'"+" and words[13]=="+"\""+time+"\""+":"+"\n\t\t"+"s=words[2]+"+"\"\\t\""+"+words[7]+"+"\"\\t\""+"+words[16]+"+"\"\\t\""+"+words[17]+"+"\"\\t\""+"+words[18]+"+"\"\\t\""+"+words[26]"+"\n\t\t"+"print \'%s\\t%s\' % (s, 1)"
f.write(b)  
f.close() 

print("MR Started")
os.system("hadoop jar hadoop-streaming-2.7.1.jar -input /d -output /qwee -mapper /home/indrajit/Desktop/major/map.py -file /home/indrajit/Desktop/major/map.py -reducer /home/indrajit/Desktop/major/reducer.py -file /home/indrajit/Desktop/major/reducer.py")
print("MR Completed")
os.system("hadoop fs -copyToLocal /qwee/part-00000 /home/indrajit/Desktop/major/Gui/")
os.system("hadoop dfs -rmr /qwee")
str="new"+time+".txt"
os.system("cp /home/indrajit/Desktop/major/Gui/part-00000 /home/indrajit/Desktop/major/Gui/"+str)
os.system("python major.py")














