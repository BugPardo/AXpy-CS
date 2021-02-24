from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession
import webbrowser

def create_session(appname):
    conf = SparkConf().setMaster('local').setAppName(appname)
    sc = SparkContext(conf=conf)
    sc = SparkContext.getOrCreate()
    spark = SparkSession.builder.appName(appname).getOrCreate()
    webbrowser.open(sc.uiWebUrl)
    return sc, spark

def read_type_file(spark,path):
    spark.conf.set("spark.sql.shuffle.partitions", 10)
    if str.lower(path.split('.')[-1]) == 'json':
        df = spark.read.json(path)
    elif str.lower(path.split('.')[-1]) == 'csv':
        df = spark.read.csv(path= path,header=True,sep=',',encoding='UTF-8')
    try:
        print(f'File {path} has been loaded, it has {df.collect()}')
    except:
        print('Error in file, please check')
    return df

def create_temporary_view(df,name,spark):
    df.createOrReplaceTempView(name)
    try:
        spark.sql(
        f'''
            SELECT  * FROM {name}
        '''
        ).show()
        print(f'Data loaded in temporary view, name:{name}')
    except:
        print('Error in df, please check')

