with open(r'C:/Users/wee/Documents/ReadInAOC2.txt','r') as f:
    input = f.readlines()

#Python Part 1
maxes = { 'Rmax': 12,
         'Gmax':13,
         'Bmax': 14
}

## If any val in any round of a game is > respective max. sum += gameID. Return sum
##THIS FUNCTION IS POINTLESS FUCK##
def findid(s):
    for i,elem in enumerate(s):
        while not elem.isdigit():
            continue
        if s[i+1].isdigit():
            id = int(elem + s[i+1])
            break
        else:
            id = int(elem)
    return id
#keeping this function here so it can look at the single line below it
# that does its job way better to shame it.       
finalsum = 0 
ids = [j+1 for j,_ in enumerate(input)]
badids = []
for k,games in enumerate(input):
    games = games.removeprefix(f'Game {ids[k]}: ')
    currentid = ids[k]
    games = games.split(';')
    for rounds in games:
        rounds = rounds.split(',')
       # print(rounds)
        for pres in rounds:
            if pres.find('green') != -1:
                for p,char in enumerate(pres):
                    if not char.isdigit():
                        continue
                    if pres[p+1].isdigit():
                        gnum = int(char + pres[p+1])
                        break
                    else:
                        gnum = int(char)
                        break
                #print(gnum)
                if gnum > maxes['Gmax'] and currentid not in badids:
                    print(f'Green Wrong: {rounds}, Game ID {currentid}')
                    badids.append(currentid)
                    finalsum += currentid
                
            elif pres.find('blue') != -1:
                for p,char in enumerate(pres):
                    if not char.isdigit():
                        continue
                    if pres[p+1].isdigit():
                        bnum = int(char + pres[p+1])
                        break
                    else:
                        bnum = int(char)
                        break
                #print(bnum)
                if bnum > maxes['Bmax'] and currentid not in badids:
                    print(f'Blue Wrong: {rounds}, Game ID {currentid}')
                    badids.append(currentid)
                    finalsum += currentid
            elif pres.find('red') != -1:
                for p,char in enumerate(pres):
                    if not char.isdigit():
                        continue
                    if pres[p+1].isdigit():
                        rnum = int(char + pres[p+1])
                        break
                    else:
                        rnum = int(char)
                        break
                #print(rnum)
                if rnum > maxes['Rmax'] and currentid not in badids:
                    print(f'Red Wrong: {rounds}, Game ID {currentid}')
                    badids.append(currentid)
                    finalsum += currentid
goodids = [gid for gid in ids if gid not in badids]
print(goodids)
print(sum(goodids))
