# Given
# mean of sample, xmean = 11.0g / 100ml
# std deviation of sample, sigma = 2.1g / 100 ml
# mean of population = 10.2g / 100ml
# H0 mean = 150
# Ha Mean <> 150

library(visualize)
zvalue = (11 - 10.2) / (2.1 / sqrt(55))
zvalue
pnorm(zvalue)
dnorm(zvalue)
pnorm(2.825218) - pnorm(-2.825218)
qnorm(0.05) # z value at 95% CI
# qnorm(0.01)
visualize.norm(stat = zvalue, mu =  0, sd = 1, section = "upper")
visualize.norm(stat = c(2.825218, -2.815218), mu = 0, sd = 1, section = "tails")
