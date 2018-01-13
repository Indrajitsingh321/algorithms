#!/usr/bin/env python
import sys
for line in sys.stdin:
	line = line.strip()
	words = line.split(',')
	if words[2]=='"Leicester"' and words[7]=='"LEWISHER ROAD"' and words[13]=="12":
		s=words[2]+"\t"+words[7]+"\t"+words[16]+"\t"+words[17]+"\t"+words[18]+"\t"+words[26]
		print '%s\t%s' % (s, 1)