import timeit;
start = timeit.default_timer();

def main():
    sundays = 0;
    day = 6;
    month = 1;
    year = 1900;
    leap = 1904;

    while year < 2000:
        year = year + 1;
        if month == 13:
            month = 1;
        while month < 13:
            if month == 9 or month == 4 or month == 6 or month == 11:
                if day > 30:
                    month = month + 1;
                    day = day - 30;
                    if day == 1:
                        sundays = sundays + 1
            elif month == 2:
                if year == leap and day > 29:
                    month = month + 1;
                    day = day - 29;
                    leap = leap + 4;
                    if day == 1:
                        sundays = sundays + 1;
                elif year != leap and day > 28:
                    month = month + 1;
                    day = day - 28;
                    if day == 1:
                        sundays = sundays + 1;
            elif day > 31:
                month = month + 1;
                day = day - 31;
                if day == 1:
                    sundays = sundays + 1;
            day = day + 7;
    print "Sundays on first of month: " + str(sundays);
main();
stop = timeit.default_timer();
print "Runtime: " + str((stop - start)*1000)[:5] + " ms";
