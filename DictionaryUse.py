stats = {}
for i in items:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

# bonus
for i in sorted(stats, key=stats.get):
    print("%d×'%s'" % (stats[i], i))
