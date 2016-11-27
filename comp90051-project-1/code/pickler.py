"""
Utility File Pickling Script

Authors:
Aleck MacNally
Kai Hirsinger

Since:
15th August 2015

Purpose:
Pickling the endless stream of CSV/TSV files
generated by Perren.

Usage:
python utility.py -f [file] -o [output] -d [delimiter]
Where file is the input file, output is the output
pickled file, and d is the delimiter (comma or tab).
"""

import argparse
import cPickle

def parseAdjacencyList(filename, delimiter):
    node_dict = dict()
    with open(filename) as file:
        for line in file:
            node_list = line.strip().split(delimiter)
            #Sometimes diagnostic info is stored as text fields
            try:
                head = int(node_list[0].strip())
            except ValueError:
                head = str(node_list[0].strip())
            #Store singleton lists as integers
            #Why did you do this? I'm changing it back
            if len(node_list[1:]) == 1:
                node_dict[head] = [int(node_list[1].strip())]
            else:
                node_dict[head] = [int(x.strip()) for x in node_list[1:]]
    return node_dict

def main(args):
    #Crunch the numbers
    if args.delimiter == "comma":
        print("Parsing {}".format(args.file))
        node_dict = parseAdjacencyList(args.file, delimiter=",")
    elif args.delimiter == "tab":
        print("Parsing {}".format(args.file))
        node_dict = parseAdjacencyList(args.file, delimiter="\t")
    elif args.delimiter == "space":
        print("Parsing {}".format(args.file))
        node_dict = parseAdjacencyList(args.file, delimiter=" ")
    else:
        print("Error: Need to specify a delimiter")
    print("Pickling...")
    cPickle.dump(node_dict, open(args.output, 'wb'))
    print("Finished! Dumped to {}".format(args.output))

if __name__ == "__main__":
    #Parse all the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",   "--file",
                        help="File to pickle")
    parser.add_argument("-o", "--output",
                        help="Output pickle file")
    parser.add_argument("-d", "--delimiter",
                        help="Field delimiter")
    args = parser.parse_args()
    #Run all the things
    main(args)