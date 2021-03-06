import sys
import os
import Utils as ut
import Spark.init_services as its


sets_name =['pandas','numpy','openpyxl','pyspark']

def check_python_version():
    if sys.version[:3] != '3.9':
        os.system(' pip install --upgrade pip')

def install_missing_packed(sets_name):
    for i in sets_name:
        print(i)
        os.system(f'cmd pip install {i}') ### idea works, logic not :( - looking for another way to extract the data and install the missing libraries.


###########
# firebase installing - setting up the full script - configurating the data.
#######
def create_product_list(db,product_type,item_id,confi_id,confi_dict):
    ut.add_record_to_firebase(db,f'{product_type}/{item_id}',confi_id,confi_dict)


