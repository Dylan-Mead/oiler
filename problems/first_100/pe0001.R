# Initialize the sum variable

#total_sum <- 0
# Loop through numbers from 0 to 999
#for (i in 0:999) {
#  if (i %% 3 == 0 || i %% 5 == 0) {
#    total_sum <- total_sum + i
# }
#}

#total_sum <- 0
#i <- 0:999
#total_sum <- sum(i[i %% 3 == 0 | i %% 5 == 0])
#cat(total_sum, "\n")

i <- 0:999
cat(sum(i[i %% 3 == 0 | i %% 5 == 0]), "\n")
