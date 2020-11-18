library(visualize)

# null hypothesis -> means are equal
# alternative hypothesis -> means are not equal

machine1 <- c(363,404,518,521,613,587,412,469,468, 496)
machine2 <- c(536,474,556,549,479,422,414,505,505,552)
alpha <- 0.05
machine1_mean <- mean(machine1)
machine1_mean
machine2_mean <- mean(machine2)
machine2_mean
var(machine1)
sd(machine1)
var(machine2)
sd(machine2)
t.test(x = machine1, y = machine2, var.equal = TRUE, conf.level = 1 - alpha)

# p-value = 0.6436 > alpha (=0.05) hence, reject null hypothesis and accept alternative hypothesis
# degrees of freedom = df = n1 + n2 - 2 = 10 + 10 - 2 = 18

visualize.t(stat=c(-0.47061, 0.47061), df=18, section="tails")