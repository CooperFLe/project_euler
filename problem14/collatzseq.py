import timeit;
import sys;

start = timeit.default_timer();
def collatz(n):
    steps = 0;
    while(n >1):
        if n%2 == 0:
            steps = steps + 1;
            n = n/2;
        elif n%2 == 1:
            steps = steps + 1;
            n = 3 * n + 1;
    return steps;

longest = 0;
value = 0;
for x in range(1000000):
    length = collatz(x);
    if length > longest:
        longest = length;
        value = x;
print "Longest: " + str(longest);
print "Value: " + str(value);


stop = timeit.default_timer();
print "Runtime: " + str((stop - start))[:4] + " seconds";
