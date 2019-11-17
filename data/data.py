#!/usr/bin/env python
from matplotlib import pyplot as plt
import pyspark as spark
from pyspark import SparkContext , SparkConf
import pyspark.sql as sp
import numpy as np
from datetime import datetime
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import *

#set your context i used local host
sc = SparkContext("local", "First App")
sqlContext = SQLContext(sc)

#test context
#print sc
#print sqlContext

#set dataframe
df = sqlContext.read.load('BeerDataScienceProject.csv', 
                          format='com.databricks.spark.csv', 
                          header='true', 
                          inferSchema='true')
#run some tests on dataframe                          
#print df
#print df.count()
df.printSchema()
# Quesiton 1
#group by beer then aggrigate beer_abv
strongest_beer = df.groupBy('beer_brewerId')
print strongest_beer
strongest_beer_abv = strongest_beer.agg({'beer_ABV':'avg'})
#test aggregate
#strongest_beer.agg({'beer_ABV':'avg'}).show()

#print abv to test
print strongest_beer_abv

#Question 2
highest_raiting = df.groupby('review_time')
#question2 = highest_raiting.max()
question2 = highest_raiting.agg({'review_overall':'avg'})

#convert to pandas in order to graph
pandas = df.toPandas()
pandas_abv = strongest_beer_abv.toPandas()
pandas_question_two = question2.toPandas()







#plt.plot()
    #print np.random.seed(444)
#print "test"
#print pyplot



#print spark.read.schema

#test =sp.read.csv(
#    "data.csv", header=True, mode="DROPMALFORMED", schema=schema
#)
#print test
#plt.plot(radius, area)
#pandas['test']
#sort pandas data 

sortPandas=pandas.sort_values('beer_brewerId').tail()
print sortPandas ,"this is sort pandas"

#pandas.plot()
sort_pandas_abv = pandas_abv.sort_values('avg(beer_ABV)').head()
print sort_pandas_abv

#sort_pandas_abv.plot.bar(x='beer_brewerId',y='avg(beer_ABV)')
sort_pandas_question_two= pandas_question_two.sort_values('avg(review_overall)').head()
pandas_question_two.plot.bar(x='review_time',y='avg(review_overall)')

#plt.savefig('question_one.png')
plt.show()

#test parsing time data into utc time
#ts = int("1325369589")

#print datetime.utcfromtimestamp(ts.strftime('%Y-%m-%d %H:%M:%S'))

#save plot

