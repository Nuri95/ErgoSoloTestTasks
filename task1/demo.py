from merge import merge
from merge.utils import count_lines


file1 = './data/f1.txt'
file2 = './data/f2.txt'

with open(file1, 'r') as f1:
    with open(file2, 'r') as f2:
        count_lines_file1 = count_lines(file1)
        count_lines_file2 = count_lines(file2)

        for line in merge(f1, f2, count_lines_file1, count_lines_file2):
            print(line)
