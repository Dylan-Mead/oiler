#The prime factors of $13195$ are $5, 7, 13$ and $29$.
#What is the largest prime factor of the number $600851475143$?

primes <- scan("src/oiler/primes.txt", what = numeric())

start <- Sys.time()
number <- 600851475143
ceiling <- number ^ 0.5


factors <- primes[number %% primes == 0 & primes <= ceiling]


end <- Sys.time()
cat("Run time no divide out:", format(end - start), "\n")

cat(tail(factors, 1), "\n")




start <- Sys.time()

remaining <- 600851475143
largest_factor <- NA_real_


for (p in primes) {
  if (p > sqrt(remaining)) break

  if (remaining %% p == 0) {
    largest_factor <- p
    while (remaining %% p == 0) {
      remaining <- remaining / p
    }
  }
}

# If anything remains, it must be the largest prime factor.
if (remaining > 1) {
  largest_factor <- remaining
}

end <- Sys.time()
cat("Run time with divide out:", format(end - start), "\n")

cat(largest_factor, "\n")
