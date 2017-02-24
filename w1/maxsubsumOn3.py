def maxsubsumOn3(vector):
    maxsum = 0
    vectorlen = len(vector)
    for i in range(vectorlen):
        for j in range(i,vectorlen):
            thissum=0
            for k in range (i,j):
                thissum=thissum+vector[k]
                if(thissum>maxsum):
                    maxsum=thissum
    return maxsum

array=[4,-3,15,-2,-1,2,-6,2]
print(maxsubsumOn3(array))
