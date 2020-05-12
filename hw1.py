fname = input('Enter File: ')
try:
    hand = open(fname)
except:
    print('Error, file was not found')
    quit()

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        w = w.lower()
        #retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w, di[w])

t = sorted(di.items())
print(t)
