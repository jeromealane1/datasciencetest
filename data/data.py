#!/usr/bin/env python
from matplotlib import pyplot as plt
import pyspark as spark
from pyspark import SparkContext , SparkConf
import pyspark.sql as sp
from datetime import datetime
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.ml.stat import Correlation


#DIRECTIONS: At the very bottom un-comment the functions that you want to see the answer to. example: qustion_one(df,plt)

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

#get some ideas about the 
#df.printSchema()
#df.describe().show()

#test parsing time data into utc time
#ts = int("1325369589")

#print datetime.utcfromtimestamp(ts.strftime('%Y-%m-%d %H:%M:%S'))

def analyze(df):
    df.describe().show()
#save plot
def question_one(df,plt):
    #group by beer then aggrigate beer_abv
    strongest_beer = df.groupBy('beer_brewerId')
    #print strongest_beer
    strongest_beer_abv = strongest_beer.agg({'beer_ABV':'avg'})
    #convert to pandas
    pandas_abv = strongest_beer_abv.toPandas()        
    #Question 1 sort and plo
    sort_pandas_abv = pandas_abv.sort_values('avg(beer_ABV)').head()
    sort_pandas_abv.plot.bar(x='beer_brewerId',y='avg(beer_ABV)')
    plt.show()

def quetion_two(df,plt):
    #Question 2
    df_star = df.select("review_taste","review_aroma","review_appearance","review_palette","review_overall","review_time")
    df_star.show()
    #highest_raiting = df_star.groupby('review_time').max().show()
    highest_raiting = df_star.groupby('review_time').max()
    #question2 = highest_raiting.max()
    #question2 = highest_raiting.agg({'review_overall':'max'}).sort_values('max(review_overall)').head(100).show()
    #question2 = highest_raiting.agg({'review_overall':'max'}).agg({'review_taste':'max'}).sort(desc("max(review_overall)")).show()
    #convert to pandas
    #pandas_question_two = question2.toPandas()
    pandas_question_two = highest_raiting.toPandas()
    #Question2 sort and plot
    new_df = pandas_question_two.sort_values('max(review_overall)').tail()
    print new_df
    #return new_df
    #pandas_question_two.plot.bar(x='review_time',y='max(review_overall)')
    #plt.savefig('question_two.png')
    #plt.show()

def question_three(df, plt):
    dfcopy = df.select("review_taste","review_aroma","review_appearance","review_palette","review_overall")
    dfcopy.show()
    pandas_question_three = dfcopy.toPandas()

    #Question3 sort and plot    
    print pandas_question_three.corr(method='pearson')
    pandas_question_three_corr_df = pandas_question_three.corr(method='pearson')
    cor_columns = pandas_question_three_corr_df.columns
    plt.matshow(pandas_question_three_corr_df)

    plt.savefig('question_three.png')
    plt.show()

def question_four(df,plt):
    best_beer = df.groupBy('beer_name')
    best_beer_aroma = best_beer.agg({'review_aroma':'max'})
    best_beer.agg({'review_aroma':'max'}).show()
    pandas_best_beer = best_beer_aroma.toPandas()
    sort_best_beer = pandas_best_beer.sort_values('max(review_aroma)').tail()
    sort_best_beer.plot.bar(x='beer_name',y='max(review_aroma)')
    plt.show()

def reviews_per_style(df,plt):
    best_beer = df.groupBy('beer_style')
    best_beer_aroma = best_beer.agg({'review_overall':'count'}).show()

#Un-Comment the question you want to run
#question_one(df,plt)
#quetion_two(df,plt)
#question_three(df,plt)
#reviews_per_style(df,plt)
question_four(df,plt)