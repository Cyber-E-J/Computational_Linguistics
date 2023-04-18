""" file: td.py
    a simple top-down backtrack CF recognizer
    python3 converted from Stabler's python2 code with 2to3
"""

def showGrammar(g): # pretty print grammar
    for (lhs,rhs) in g:
        print(lhs, '->', end=' ')
        for cat in rhs:
            print(cat, end=' ')
        print()

def showDerivations(ds): # pretty print the 'backtrack stack'
    for (n,(i,cs)) in enumerate(reversed(ds)):
        print(n,'(', end=' ')
        for w in i: # print each w in input
            print(w, end=' ')
        print(',', end=' ')
        for c in cs: # print each predicted c in cs
            print(c, end=' ')
        print(')')
    print('---------')

def tdstep(g, y): # compute all possible next steps from (i,cs)
    (i,cs) = y
    if len(cs)>0:
        cs1=cs[1:] # copy of predicted categories except cs[0]
        nextsteps=[]
        for (lhs,rhs) in g:
            if lhs == cs[0]:
                print('expand',lhs,'->',rhs) # for trace
                nextsteps.append((i,rhs+cs1))
        if len(i)>0 and i[0] == cs[0]:
            print('scan',i[0]) # for trace
            nextsteps.append((i[1:],cs1))
        return nextsteps
    else:
        return []

def recognize(g,i):
    ds = [(i,['S'])]
    while ds != [] and ds[-1] != ([],[]):
        showDerivations(ds) # for trace
        d = ds.pop()
        ds.extend(tdstep(g,d))
    if ds==[]:
        return False
    else:
        showDerivations(ds) # for trace
        return True


