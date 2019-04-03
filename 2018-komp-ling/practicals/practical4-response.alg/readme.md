There are two folders.

"udpipe" contains syntagrus udpipe model (from here https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2898), script for transforming file (gets file name and returns conllu format sentenses from it to stdout).

"max_spanning_tree" contains script and its tests. It gets from stdin number of lines and graph matrix with numbers devided by space. Like that:

4 <br />
0 4 0 0 <br />
0 0 0 7 <br />
0 0 0 7 <br />
3 0 6 0

And returns maximum spanning tree to stdout.
