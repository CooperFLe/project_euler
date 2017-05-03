import timeit;

start = timeit.default_timer();
nums = [[0 for x in range(50)] for y in range(100)];
final = 0;

f = open('input.txt','r');
for line in f:
    final = final + int(line);
print("Total: " + str(final));
print("First 10: " + str(final)[:10])
stop = timeit.default_timer();

print "Runtime: " + str((stop - start)*1000)[:4] + " ms";
