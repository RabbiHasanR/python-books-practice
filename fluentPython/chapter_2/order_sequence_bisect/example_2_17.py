import bisect
import sys

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

row_fmt = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)
        offset = position * '  |'
        print(row_fmt.format(needle, position, offset))

#if __name__ == 'main':
if sys.argv[-1] == 'left':
    bisect_fn = bisect.bisect_left
else:
    bisect_fn = bisect.bisect
    
print('Demo:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in haystack))
demo(bisect_fn)
    

