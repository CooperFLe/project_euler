import timeit;
import sys;
#21124
start = timeit.default_timer();
ones = [0]*10;
ones[0] = 0;
ones[1] = len("one");
ones[2] = len("two");
ones[3] = len("three");
ones[4] = len("four");
ones[5] = len("five");
ones[6] = len("six");
ones[7] = len("seven");
ones[8] = len("eight");
ones[9] = len("nine");
tens = [0]*10;
tens[2] = len("twenty");
tens[3] = len("thirty");
tens[4] = len("forty");
tens[5] = len("fifty");
tens[6] = len("sixty");
tens[7] = len("seventy");
tens[8] = len("eighty");
tens[9] = len("ninety");

def letters(n):
    # 11 - 19 special case
    if n < 10:
        return ones[n];
    elif n < 20:
        # 10 - 19
        if n == 10:
            return 3;
        if n == 11:
            return len("eleven");
        if n == 12:
            return len("twelve");
        if n == 13:
            return len("thirteen");
        if n == 14:
            return len("fourteen");
        if n == 15:
            return len("fifteen");
        if n == 16:
            return len("sixteen");
        if n == 17:
            return len("seventeen");
        if n == 18:
            return len("eighteen");
        if n == 19:
            return len("nineteen");

    elif n < 100:
        # 20 - 99
        return tens[n/10] + ones[n%10];
    elif n < 1000:
        if n % 100 == 0:
            # Even hundred
            return ones[n/100] + len("hundred");
        # All else
        return 3 + ones[n/100] + letters(n%100) + len("hundred");
    # For 1000
    return len("onethousand");

ans = 0;
for x in range(1,1001):
    ans = ans + letters(x);
print "Answer: " + str(ans);


stop = timeit.default_timer();
print "Runtime: " + str((stop - start))[:6] + " seconds";
