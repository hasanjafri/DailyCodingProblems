def remove_overlapping_intervals(lst):
    flist = []
    for num in lst:
        minValue = num[0]
        maxValue = num[1]
        for ranges in flist:
            if ranges[0] < minValue and ranges[1] > maxValue:
                