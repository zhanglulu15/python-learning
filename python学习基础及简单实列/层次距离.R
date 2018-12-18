#计算欧几里得距离
library(cluster)
library(NbClust)
library(flexclust)
library(fMultivar)
library(ggplot2)
library(rattle)

#查看flexclust包中的数据集，它包括27种肉、鱼和禽的yun养物质的测量
data("nutrient",package = "flexclust")
head(nutrient,4)

#使用as.matrix()函数可使用标准括号富豪得到距离
d <- dist(nutrient)
as.matrix(d)[1:4,1:4]
#观测值之间的距离越大，异质性越大，观测值和它自己之间的距离是0

#层次聚类分析：在层次聚类中，起初每一个实列或者观测值属于一类，聚类计算每一次把两类聚成新的一类，
#直到所有的类聚成单个类为止
data("nutrient",package = "flexclust")
row.names(nutrient) <- tolower(row.names(nutrient)) #将行名称的大写形式转换为小写
nutrient.scaled <- scale(nutrient)   #由于变量的变化范围很大，需要将其标准化为均值为0，方差为1
d <- dist(nutrient.scaled)  #使用欧几里得距离
fit.average <- hclust(d,method = "average")
plot(fit.average,hang = -1,cex = .8,main = "average linkage clustering")

#选择聚类个数
library(NbClust)
devAskNewPage(ask = TRUE)
nc <- NbClust(nutrient.scaled,distance = "euclidean",min.nc = 2,max.nc = 15,method = "average")
table(nc$Best.nc[1,])
barplot(table(nc$Best.nc[1,]),
        xlab = "Number of Clusters",ylab = "Number of Criteria",
        main = "Number of Clusters Chosen by 26 Criteria")

#获取最终聚类方案
clusters <- cutree(fit.average,k = 5)  #将树状图分成5类
table(clusters)  #查看每一类的情况
aggregate(nutrient,by = list(cluster = clusters),median) #获取每类的中位数(原始度量)
aggregate(as.data.frame(nutrient.scaled),by = list(cluster = clusters),median) #获取每类的中位数（标准度量）

plot(fit.average,hang = -1,cex =.8,
     main = "Average Linkage Clustering/5 Cluster Solution") #绘制结果图
rect.hclust(fit.average,k =5)  #将结果分成5类


  
  
  
  
  
  
  
  
  







