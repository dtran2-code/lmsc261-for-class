'''
Question 1.

for i in range(4):
    print("Hello")

Guess: It will print "Hello" 4 times

Result: 

Hello
Hello
Hello
Hello

A for loop is used to repeat the print function for exactly 4 times, since 4 is specified in class "range"
'''







'''
Question 2.

count = 0
while count < 3:
    count = count + 1
print(count)

Guess: It would print 3

Result:

3

A variable is set to a value of 0 as an integer. The while loop is used to add 1 to 0 with the + operator
until "count" reaches a value of 3. Since 3 isn't smaller than 3, the adding stops at 3, and the
program returns "3"
'''





'''
Question 3:

score = 85
if score > 70:
    print("Pass")
elif score > 80:
    print("Great")
else:
    print("Fail")

Guess: The program will print "Great"

Result:

Pass

Since the score's value of 85 does meet the first condition of being over 70, the code prints that
first, and doesn't bother checking the other conditions since the first one is already True. The fix
to this is just to switch the first 2 conditionals:

score = 85
if score > 80:
    print("Great")
elif score > 70:
    print("Pass")
else:
    print("Fail")

'''








'''
Question 4.

x = 5
while x > 0:
    print(x)
    x += 1

Guess: It's going to spit out 5, then 6, 7 ,8... to infinity

Result: It does just that, it's not practical to type it in. The condition is always True, since x is already
bigger than 0, being set with a value of 5. The code would just print x, then print x + 1 as the new x.
'''







'''
Question 5.

for i in range(2):
    for j in range(2):
        print(i, j)

Guess: It would print out

0 0
0 1
1 0
1 1

Result:

0 0
0 1
1 0
1 1

Starting with the nested for loop in regards to j, we know that j in (i, j) will be:

0 0
0 1

And since that fulfills the nested for loop in regards to j, that registers as 1 iteration that counts towards
the outer for loop, for i. To fulfill the outer loop till it satisfies range(2), for j in range(2) would have to
occur again, for it to be another iteration:

0 0 
0 1 
1 0 ---- here, it marks the j loop restarting, and the first iteration of the i loop completing, so it shows 1
         but since the j loop is now 0, it has to iterate one more time
1 1

'''
