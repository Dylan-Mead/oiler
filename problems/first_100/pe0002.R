#By considering the terms in the Fibonacci sequence whose values 
#do not exceed four million, 
#find the sum of the even-valued terms.

#It's trivial to show that every third term will be even
#This allows us to skip the odd terms and sum only the even ones.

#some basic matrix arithmatic can be used to derive the recurrence relation for 
#even Fibonacci numbers

#   |0, 1|^3    =	|1, 2|
#   |1, 1|		    |2, 3|

library(zeallot)

a <- 1
b <- 2
sum <- 0

#c(a, b) %<-% c(a + b, a + 2 * b)

while (b < 4000000) {
  sum <- sum + b
  c(a, b) %<-% c(a + 2*b, 2*a + 3*b)
} 

cat(sum, "\n")