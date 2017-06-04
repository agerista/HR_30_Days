# Hacker Rank 30 Days of Code Challenge

[Hacker Rank 30 Day Challenge](https://www.hackerrank.com/domains/tutorials/30-days-of-code)

30 Days of Code is an opportunity to learn how to code or brush up on your 
fundamentals. Each day at 9am, you will unlock a new challenge and a corresponding 
video tutorial to help you learn. The tutorial is Java-based, but you can choose 
other popular languages to submit your solution. Topics include if-else statements, recursion, data structures and more.

### Day 0: Hello, World

Task:

Save a line of input from stdin to a variable, print "Hello, World." on a single line. 
Print the value of your variable on a second line. [Try it!](https://www.hackerrank.com/domains/tutorials/30-days-of-code)

### Day 1: Data Types

Task:

* Declare  variables: one of type int, one of type double, and one of type String.

* Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.

* Use the  operator to perform the following operations: 

    * Print the sum of  plus your int variable on a new line.

    * Print the sum of  plus your double variable to a scale of one decimal place 
    on a new line.

    * Concatenate  with the string you read as input and print the result on a 
    new line. [Try it!](https://www.hackerrank.com/challenges/30-data-types)

### Day 2: Operators

Task:

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. [Try it!](https://www.hackerrank.com/challenges/30-operators)

### Day 3: Intro to Conditional Statements

Task:

Given an integer, n, perform the following conditional actions:

* If  is odd, print Weird
* If  is even and in the inclusive range of 2 to 5, print Not Weird.
* If  is even and in the inclusive range of 6 to 20, print Weird.
* If  is even and greater than 20, print Not Weird. [Try it!](https://www.hackerrank.com/challenges/30-conditional-statements)

### Day 4: Class vs. Instance

Task:

Write a Person class with an instance variable, age, and a constructor that 
takes an integer, initialAge, as a parameter. The constructor must assign 
initialAge to age after confirming the argument passed as initialAge is not 
negative; if a negative argument is passed as initialAge, the constructor should 
set age to 0 and print Age is not valid, setting age to 0. In addition, you must 
write the following instance methods:

1. yearPasses() should increase the age instance variable by 1.

2. amIOld() should perform the following conditional actions:

    * If age < 13, print You are young.

    * If age >= 13 and age < 18, print You are a teenager.

    * Otherwise, print You are old. [Try it!](https://www.hackerrank.com/challenges/30-class-vs-instance)

### Day 5: Loops

Task:

Given an integer, n, print its first 10 multiples. Each multiple n x i 
(where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.
[Try it!](https://www.hackerrank.com/challenges/30-loops)

### Day 6: Let's Review

Task:

Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed 
and odd-indexed characters as 2 space-separated strings on a single line. 0 is 
considered to be an even index. [Try it!](https://www.hackerrank.com/challenges/30-review-loop)

### Day 7: Arrays

Task:

Given an array, A, of N integers, print A's elements in reverse order as a single 
line of space-separated numbers. [Try it!](https://www.hackerrank.com/challenges/30-arrays)

### Day 8: Phone a Friend

Task:

Given n names and phone numbers, assemble a phone book that maps friends’ names to 
their respective phone numbers. You will then be given an unknown number of names 
to query your phone book for. For each name queried, print the associated entry from 
your phone book on a new line in the form name=phoneNumber; if an entry for name 
is not found, print Not found instead. [Try it!](https://www.hackerrank.com/challenges/30-phone-a-friend)

### Day 9: Recursion

Task:

Write a factorial function that takes a positive integer, N as a parameter and 
prints the result of N! (N factorial). [Try it!](https://www.hackerrank.com/challenges/30-recursion)

### Day 10: Binary Numbers

Task:

Given a base-10 integer, n, convert it to binary (base-2). Then find and print 
the base-10 integer denoting the maximum number of consecutive 1's in n's binary 
representation. [Try it!](https://www.hackerrank.com/challenges/30-binary-numbers)

### Day 11: 2D Arrays

Task:

Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this 
pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

### Day 12: Inheritance

Task:

You are given two classes, Person and Student, where Person is the base class and 
Student is the derived class. Completed code for Person and a declaration for Student 
are provided for you in the editor. Observe that Student inherits all the properties 
of Person. Complete the Student class. [Try it!](https://www.hackerrank.com/challenges/30-inheritance)

### Day 13: Abstract Classes

Task:

Given a Book class and a Solution class, write a MyBook class that does the following:

* Inherits from Book

* Has a parameterized constructor taking these  parameters:
    
    1. string title
    2. string author
    3. int price

* Implements the Book class' abstract display() method so it prints these  lines:
    1. Title:, a space, and then the current instance's title.
    2. Author:, a space, and then the current instance's author.
    3. Price:, a space, and then the current instance's price.

### Day 14: Scope

Task:

Complete the Difference class by writing the following:

* A class constructor that takes an array of integers as a parameter and saves it 
to the elements instance variable.

* A computeDifference method that finds the maximum absolute difference between 
any 2 numbers in N and stores it in the maximumDifference instance variable.
