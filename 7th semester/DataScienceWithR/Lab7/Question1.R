# install.packages("visualize")
library(visualize)
zvalue = (152 - 150) / (2 / sqrt(100))
zvalue
qnorm(0.95) # critical value at 95% at upper tail
qnorm(0.05) # critical value at 5% at lower tail
visualize.norm(stat = zvalue, mu = 0, sd = 1, section = "upper")
# visualize.norm(stat = c(10, -10), mu = 0, sd = 1, section = "tails")

# install.packages("BSDA")
library(BSDA)
z.test(x = D$Machine.1, alternative = "greater", sigma.x = 2, mu = 150)
