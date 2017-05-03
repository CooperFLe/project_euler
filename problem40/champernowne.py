import timeit;
start = timeit.default_timer();

def main():
    i = 1;
    string = "";
    while len(string) < 1000000:
        string = string + str(i);
        i = i + 1;
    string = string[:1000000];
    total = int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999]);
    return total;
print "Total: " + str(main());
stop = timeit.default_timer();
print "Runtime: " + str((stop - start))[:6] + " seconds";
