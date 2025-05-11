Code:
likes(ram,mango).
girl(seema).
red(rose).
owns(john,gold).
likes(bill,cindy).
OUTPUT :
?- likes(ram,What).
What=mango
?- likes(Who,cindy).
Who = bill
?- red(What).
What = rose
?-owns(Who,What).
What = gold,
Who = john

switch prolong