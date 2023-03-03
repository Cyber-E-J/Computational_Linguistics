"""
file: tdb.py   Ed Stabler
  A simple top-down beam CF recognizer.
  The minor changes from td.py are labeled "for beam"
  Modified for python3 Mats Rooth using 2to3
"""
import heapq

def tdstep(g, xxx_todo_changeme): # compute all possible next steps from (i,cs)
    (i,cs) = xxx_todo_changeme
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
        
def recognize(g,i,k):
    beam = [(-1.,i,['S'])] # probability 1., negated
    heapq.heapify(beam) # make list into a "min-heap"
    while beam != [] and not(min(beam)[1]==[] and min(beam)[2]==[]):
        (prob0,i0,cs0) = heapq.heappop(beam)
        print('popped',(prob0,i0,cs0)) # for trace
        nextsteps = tdstep(g,(i0,cs0))
        print('next steps=',nextsteps)
        if len(nextsteps) > 0:
            prob1 = prob0/float(len(nextsteps))
            if -(prob1) > k:
                for (i1,cs1) in nextsteps:
                    heapq.heappush(beam,(prob1,i1,cs1))
                    print('pushed',(prob1,i1,cs1)) # for trace
                    print('|beam|=',len(beam)) # for trace
    if beam == []:
        return False
    else:
        return True

# Examples:
# recognize(g1,['Sue','laughs'],0.05)
# recognize(g1,['Sue','laughs'],0.5)
# recognize(g1,['Bill','knows','that','Sue','laughs'],0.10)
# recognize(g1,['Bill','knows','that','Sue','laughs'],0.01)
# recognize(g1,['Bill','knows','that','Sue','laughs'],0.0000001)
