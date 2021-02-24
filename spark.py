##import findspark as fs
##fs.init()


from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession
conf = SparkConf().setMaster('local').setAppName('Testing Module')
sc = SparkContext(conf = conf)
sc = SparkContext.getOrCreate()
spark = SparkSession.builder.appName('Testing Module').getOrCreate()

df = spark.read.json('health_tracker_data_2020_2.json')
df.select('name').collect()
df.createOrReplaceTempView('table')

spark.conf.set("spark.sql.shuffle.partitions",10)

result =  spark.sql(
    """
        SELECT
            name,
            count(*) as count,
            avg(heartrate) as heart,
            avg(time) as time
        FROM
            table
        GROUP BY 1     
    """
).toPandas()


spark_home = os.environ.get('SPARK_HOME', None)

for i in spark_home:
    print(i)

import os
print(os.environ['SPARK_HOME'])


import json
import pandas as pd
file = open('achievements.json','r',encoding='UTF-8')
data = json.load(file)
df = pd.DataFrame()

for i in data:
    c_name = i['name'] ##Achievement name
    c_description = i['stringRefs']['description'] ## Description
    c_type = i['stringRefs']['title'] # Type :D
    try:
        c_simple_text_des = i['strings']['description']['EN'] # Simple text description
        c_simple_text_title = i['strings']['title']['EN'] # Simple text title
    except:
        c_simple_text_des = None
        c_simple_text_title = None
    df = df.append({
        'Name': c_name,
        'Description': c_description,
        'Des - Title': c_type,
        'Simple Description' : c_simple_text_des,
        'Simple title': c_simple_text_title
    },ignore_index=True)
w = pd.ExcelWriter('result.xlsx')
df.to_excel(w,'Result')
w.save()



text = 'abcdcbda'
Hola = 'hola pasdasd'
Hola[::-1]


