with open(r'C:/Users/wee/Documents/ReadInAOC3.txt','r') as f:
    input = f.readlines()


## Store beginning index, length of number and string number in an array i.e. [([2,4],3,'123'),...]means 3 digit number at 2,4 of 123.
## Go through tuples, jump to beginning index, scan in 9 directions for each digit of number, if found not == '.' and not found.isdigit()
## digit is relevant, store number in wantedids !!! AS AN INT i.e num = int(digit1 + digit2 + digit3) !!!
storage = []
#print(input)
for k,lines in enumerate(input):

    for i,c in enumerate(lines):
        
        if i == 0:
            continue
        elif len(storage):
            if i > begin and i <= final:
                
                continue
        
        if not c.isdigit():
            continue

        else:
            hasbeenfound = 1
            strint = c
            j = 1
            while lines[i+j].isdigit():
                strint += lines[i+j]
                j += 1
            length = j
            stortuple = [[k,i],length,strint]
            begin = stortuple[0][1]
            final = begin+length
            storage.append(stortuple)

def CheckNeighbours(x,k):
    #x = [row,col]
    #clockwise from above
    Neighbours = [[x[0]-1,x[1]],[x[0]-1,x[1]+1],[x[0],x[0]+1],[x[0]+1,x[1]+1],[x[0]+1,x[1]],[x[0]+1,x[1]-1],[x[0],x[1]-1],[x[0]-1,x[1]-1]]
    
    return Neighbours

sumbuf = []
for stored in storage:
    #print(stored)
    num = int(stored[2])
    #print(num)
    #print(stored)
    indofint = [[stored[0][0],stored[0][1]+i] for i in range(stored[1])]
    for indice in indofint:
        indneighb = CheckNeighbours(indice,k)
        #True if symbol, false if not
        for inds in indneighb:
            #print(inds)
            try:
                vals = input[inds[0]][inds[1]]
            except IndexError: #Lazy but oh well
                continue

            #print(vals)
            if vals == '.' or vals.isalnum():
                continue
            elif num not in sumbuf:
                    sumbuf.append(num)

#print(sumbuf)
print(sum(sumbuf))



            



