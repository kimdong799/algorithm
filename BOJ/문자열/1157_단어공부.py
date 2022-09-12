import sys
from collections import Counter
input_string = sys.stdin.readline().rstrip().upper()

str_counter = Counter(input_string)
max_char_freq = str_counter.most_common(1)[0][1]
max_char = str_counter.most_common(1)[0][0]

if len(input_string) > 1:
    sec_char_freq = str_counter.most_common(2)[1][1]
    print("?" if max_char_freq == sec_char_freq else max_char)
else:
    print(max_char)