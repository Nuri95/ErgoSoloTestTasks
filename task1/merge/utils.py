__all__ = (
    'count_lines',
)


def count_lines(file):
    with open(file, 'rt') as f:
        count = 0
        for _ in f:
            count += 1

        return count

