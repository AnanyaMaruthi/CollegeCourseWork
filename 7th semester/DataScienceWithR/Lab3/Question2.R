# Below we have results of a simple experiment to look at the visitation of various bee species to different plants.The number of bees observed was as follows.
# i)Buff Tail:10 1 37 5 12
# ii)Garden bee:8 3 9 6 4
# iii)Red Tail:18 9 12 4
# iv)Carder bee: 8 27 6 32 23
# v)Honey Bee: 12 13 16 9 10
# Make five simple numeric vectors of these data. Next join the bee vectors together to make a data frame. Each row of the resulting frame relates to specific plant, the plant names are Thistle,Vipers,Golden Rain,Yell


buff_tail <- c(10,1,37,5,12)
garden_bee <- c(8,3,9,6,4)
red_tail <- c(18,9,12,4, 10)
carder_bee <- c(8,27,6,32,23)
honey_bee <- c(12,13,16,9,10)
data_frame <- data.frame(buff_tail, garden_bee, red_tail, carder_bee, honey_bee)
row.names(data_frame) <- c("Thistle", "Vipers", "Golden Rain", "Yell", "PlantX")
data_frame
str(data_frame)
