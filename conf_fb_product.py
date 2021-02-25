import Utils as ut
import Spark.init_services as its

def create_product_list(db,product_type,item_id,confi_id,confi_dict):
    ut.add_record_to_firebase(db,f'{product_type}/{item_id}',confi_id,confi_dict)
    