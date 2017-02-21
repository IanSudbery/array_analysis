import os
import re


with open("targets.txt", "w") as targets_file:
    fields = ["SlideName","fraction", "knockdown", "time", "replicate", "FileName"]
    print "\t".join(fields)
    for line in open("fofn"):
        F = line.strip().split("/")
        fraction = F[0]
        try:
            Cy3 = re.match("(?:CYTO|TOTAL)_(.+)\.", F[1]).groups()[0]
        except AttributeError:
            print "Cannot match '(?:CYTO|TOTAL)_(.+)\.' in %s" % F[1]
            raise
        try:
            time = re.search("\.([0-9]+)hrs", F[1]).groups()[0]
        except AttributeError:
            print "Cannot match '\.([0-9]+)hrs' in %s" % F[1]
            print line
            raise
        try:
            replicate = re.search("R([0-9])", F[2]).groups()[0]
        except AttributeError:
            print "Cannot match 'R([0-9])' in %s" % F[2]
            raise
        filename = line.strip()
        SlideName=".".join([fraction[0], Cy3, time, replicate])
        print "\t".join([SlideName,fraction, Cy3, time, replicate, filename])
