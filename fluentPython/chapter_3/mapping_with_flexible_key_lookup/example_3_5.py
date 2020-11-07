"""Build an index mapping word -> list of occurrences"""

import sys
import re
from collections import defaultdict
word_re = re.compile('\w+')

index = defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            locaton = (line_no, column_no)
            index[word].append(locaton)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])