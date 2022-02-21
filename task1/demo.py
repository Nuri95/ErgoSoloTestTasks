from merge import merge


def count_lines(file):
    with open(file, 'rt') as f:
        count = 0
        for _ in f.readline():
            count += 1

        return count


file1 = './data/f1.txt'
file2 = './data/f2.txt'
with open(file1, 'r') as f1:
    with open(file2, 'r') as f2:
        count_lines_file1 = count_lines(file1)
        count_lines_file2 = count_lines(file2)
        print(count_lines_file1, count_lines_file2)
        for line in merge(f1, f2, count_lines_file1, count_lines_file2):
            print('result', line)
