# from pyspark.mllib.clustering import KMeans, KMeansModel
# data = [[10,20,30,40],
# [1,-1,0,2],
# [10,21,31,40],
# [0,0,0,0]]
# rdd = sc.parallelize(data)
# rdd.collect()
# clusters = KMeans.train(rdd, 2, maxIterations=10,
#         runs=10, initializationMode="random")
# print clusters.centers
# print(clusters.predict([10,20,20,20]))
# print(clusters.predict([0,0,0,0]))#