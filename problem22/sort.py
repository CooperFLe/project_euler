import timeit;
start = timeit.default_timer();

def makeList(f):
    inFile = open(f,'r');
    for line in inFile:
        names = line;
    names = names.strip().split(",");
    names.sort();
    for x in range(len(names)):
        names[x] = str(str(names[x])[1:-1]).strip();
    return names;

def process(names):
    i = 1;
    total = 0;
    for name in names:
        nameSum = 0;
        for x in range(len(name)):
            nameSum = nameSum + ord(name[x])-64;
        nameSum = nameSum * i;
        total = total + nameSum;
        i = i + 1;
    return total;


def main():
    names = makeList('names.txt');
    print "Total: " + str(process(names));

main();
stop = timeit.default_timer();
print "Runtime: " + str((stop - start))[:6] + " seconds";
