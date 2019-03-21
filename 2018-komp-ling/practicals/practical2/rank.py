import re
from collections import Counter
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--top', '-t', default=None, help='number of words which will be showed')
    parser.add_argument(dest='file', help='input file')
    args = parser.parse_args()
    args.top = int(args.top)
    count = Counter([])
    with open(args.file) as file:
        for line in file:
            count.update(re.findall(r'[\w]+\b', line.lower()))
    top_counter = 0
    for word in sorted(count, key=count.get, reverse=True):
        if args.top is not None and args.top <= top_counter:
            break
        print('{}\t{}'.format(word, count[word]))
        top_counter += 1
