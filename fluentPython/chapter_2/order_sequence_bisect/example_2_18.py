import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    print(i)
    return grades[i]

results = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(results)