# TricountPython
My take on a tricount in python
(work in progress, have a few idea for improvemnts)
The code reads transaction data from a text file, calculates the amount owed or to be received by each individual, and then resolves any outstanding debts between them.

The input file should be formatted with each line representing a single transaction in the following format: 

**WhatWasPaid ByWho Sum ToWhom1 ToWhom2 ToWhom... ToWhomN**

Here's how the code works :
+ The code asks to give the path to the file containing the transactions
+ The dictionaries **percu** , **balance** and **solde** are used to keep track of the an individual **total received**, **spent** and **current balance** respectively.
+ The code goes over each line in the input file, splitting the line into individual components and updating the **percu** and **balance** dictionaries accordingly.
+ The code then calculates the difference between the total amount received and the total amount spent for each individual, storing the results in **solde**
+ The code enters a loop to resolve any debts between individuals, beginning by the one who is owed the most and the one who owes the most.
+ Calculates the amount to be transferred and updating **balance** and **solde**.
+ Output the final balances and transfers to be made.
