ls1 = [(5, 'one'), (3, 'rew'), (3, 'lo'), (1, 'trow'), (1, 'lop'), (1, 'ga')]


sorted_ls1 = sorted(ls1, key=lambda x: (-x[0], x[1]))
print(ls1)
print(sorted_ls1)
