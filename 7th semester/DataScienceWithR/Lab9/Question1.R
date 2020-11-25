number <- c(1:15)
temperature <- c(50,53,54,55,56,59,62,65,67,71,72,74,75,76,79)
yield <- c(122,118,128,121,125,136,144,142,149,161,167,168,162,171,175)
df<-data.frame(temperature, yield)
rownames(df) <- number
df
lr <- lm(yield ~ temperature, data=df)
print(summary(lr))
names(lr)
lr$coefficients
pred <- fitted(lr)
pred
plot(df$temperature, df$yield, col="red")
abline(lr, col="blue")
