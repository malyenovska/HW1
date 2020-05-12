fname = input('Enter File: ')
try:
    hand = open(fname)
except:
    print('Error, file was not found')
    quit()

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        w = w.lower()
        di[w] = di.get(w,0) + 1

t = sorted(di.items())
print(t)
