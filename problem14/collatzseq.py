import timeit;
import sys;

longest = 0;
value = 0;

start = timeit.default_timer();
buf = [0]*1000000;
def collatz(n):
    steps = 0;
    while(n >1):
        if n < 1000000 and buf[n] != 0:
            return steps + buf[n];
        if n%2 == 0:
            steps = steps + 1;
            n = n/2;
        elif n%2 == 1:
            steps = steps + 1;
            n = 3 * n + 1;
    return steps;

for x in range(1000000):
    length = collatz(x);
    buf[x] = length;
    if length > longest:
        longest = length;
        value = x;
print "Longest: " + str(longest);
print "Value: " + str(value);


stop = timeit.default_timer();
print "Runtime: " + str((stop - start))[:4] + " seconds";
