# The r script for processing NEON data of cell count in water July 25, 2023.
# xxu@sdsu.edu

#plot(c(1,2,3,4,5),c(1,4,9,16,25))

setwd("C:/cygwin64/home/jyqia/neno")
#library("")
#cell <- read.table("Annual.txt", header=TRUE)
#plot(cell$Cell_Count~cell$Lat)

cell <- read.table("bird_annual_summary.txt", header=TRUE)
#plot(cell$Cell_Count~cell$Lat)
plot(cell$Total_Bird~cell$Diameter)

#plot(cell$Cell_Count~cell$Lat, type="p", xlab="Latitude", ylab="Microbial cell count (1000 / ml)", cex = 1.5, lwd = 2, las=3, cex.lab=1.5,cex.axis=1.5,font.lab=2)
#summary(lm(cell$Cell_Count~cell$Lat))
#plot(cell$Cell_Count~cell$Dissolved_O2)
#plot(cell$Cell_Count~cell$Dissolved_O2, type="p", xlab="Dissolved Oxygen", ylab="Microbial cell count (1000 / ml)", cex = 1.5, lwd = 2, las=3, cex.lab=1.5,cex.axis=1.5,font.lab=2)
#summary(lm(cell$Cell_Count~cell$Dissolved_O2))

#plot(cell$Cell_Count~cell$Water_Temp, type="p", xlab="Water temperature (Degree C)", ylab="Microbial cell count (1000 / ml)", cex = 1.5, lwd = 2, las=3, cex.lab=1.5,cex.axis=1.5,font.lab=2)
#summary(lm(cell$Cell_Count~cell$Water_Temp))

