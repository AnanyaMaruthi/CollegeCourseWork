A <- matrix(c(1,2,3,4,5,6,7,8), nrow=4, ncol=2)
transpose <- t(A)
B <- matrix(c(1,2,3,4), nrow=2, ncol=2)
C <- matrix(c(5,6,7,8), nrow=2, ncol=2)
inverse <- solve(B)
eigenValue <- eigen(B)
crossproduct <- crossprod(B)
cross <- t(B) %*% (B)

A[1,] 
A[,1]
A[2,]
A[,2]
