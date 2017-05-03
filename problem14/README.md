An unfortunately slow solution to [Problem 14](https://projecteuler.net/problem=14) of Project Euler. This is a pure brute force attempt using Python.

Python was chosen because I was recently called about a job offering where Python developers are wanted. Figured it was a good chance to brush up on my Python that I haven't work on in about two years.

# Update
Improved runtime by storing previously found values. This way, if the program finds itself at n after already calculating the steps required to get n to 1, we will take the previously found steps required to get n to 1 and add that to our current step count removing the need to recalculate the step count.

This improvement brought the average runtime down from about 25 seconds to about 2 seconds.
