def m(l1, l2):
    m = zip(l1, l2)
    return dict(m)


ml1 = ['Vasia', 'Peta', 'Ivan']
ml2 = [35, 40, 45]
result = m(ml1, ml2)
print(result)
