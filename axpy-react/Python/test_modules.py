import Utils as ut
import Spark.init_services as its

### Create DB connection with firebase
def main():
    path_session_file = ut.choose_file()
    db = ut.create_connection_firebase(path_session_file)
    item_id = 'ETLServices'
    ##ut.add_record_to_firebase(db,f'WebService/EmailSettings/{item_id}','Settings',{'a':'as'})



a  = 26

a >= 10 and a%5-1
