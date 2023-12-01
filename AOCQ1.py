
with open(r'C:/Users/wee/Documents/ReadInAOC1.txt','r') as f:
    input = f.readlines()
    f.close()
## Part 1
allbuf = []

## TEST
# input = ['two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen',
# 'abconetwone']



NUM2num = {"zero": 0, "one": 1, "two":2, "three":3,"four":4,"five":5,"six":6,
           "seven":7,"eight":8,"nine":9}

for inputs in input:
    elements = []
    for k, elem in enumerate(inputs):
        if elem.isdigit():
            elements.append((k, int(elem)))

    for key in NUM2num.keys():
        index = inputs.find(key)
        while index != -1:
            elements.append((index, NUM2num[key]))
            index = inputs.find(key, index + 1)

    elements.sort()

    rowbuf = [num for _, num in elements] 
    allbuf.append(rowbuf)

for i,bufs in enumerate(allbuf):
    
    bufs = [bufs[0],bufs[-1]]
    
    if isinstance(bufs[0],str)
        bufs[0] = NUM2num[bufs[0]]
    if isinstance(bufs[1],str):
        
        bufs[1] = NUM2num[bufs[1]]

    allbuf[i] = int(''.join(map(str,bufs)))
 
    
final = sum(allbuf)
