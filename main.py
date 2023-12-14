import re

bagofcubes = {'red':'12','green':'13','blue':'14'}
possiblegames = []
# Open file, read each line
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        #Split line by Game #: and ;
        splitgames = re.split(':|;', line)
        print(f'Split line: {splitgames}')
        #Check the bag of cubes, see if it's OK
        impossible = False
        for i in range(1, len(splitgames)):
            if impossible:
                break
            splitcolors = re.split(',', splitgames[i])
            print(f'Split color {splitcolors}')
            for numbercolor in splitcolors:
                numcolorlist = numbercolor.split()
                print(f'Split number:color {numcolorlist}')
                #Check if it's less
                print(f'bagofcubes {bagofcubes[numcolorlist[1]]}')
                if int(numcolorlist[0]) > int(bagofcubes[numcolorlist[1]]):
                   impossible = True
                   print(f'numcolorlist: {numcolorlist}')
                   break
        print(f'impossible: {impossible}')
        if not impossible:
            getgamenumber = splitgames[0].split()
            possiblegames.append(getgamenumber[1])

print(f'All possible games: {possiblegames}')
#Sum them up
print(f'Sum total: {sum(map(int,possiblegames))}')


