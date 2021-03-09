import Utils as ut
import Spark.init_services as sp

sc, spark = sp.create_session('testing')


file = ut.choose_file()
db = ut.create_connection_firebase(file)
db.collection('SellServiceN1')

ut.add_record_to_firebase(db,'HOLIWIS/UserDetails/Userlist','TESTING',{'Acomdeishon': 'Shingona', 'Comida': 'Tacos','Color':'Morado'})


db.collection('Customers/Key1/USDS').document('Key1').set({'Dias de vacaciones utilizados': 1, 'Fecha': ('2021-01-18 00:00:00')})

#   {'Dias de vacaciones utilizados': 1, 'Fecha': ('2021-01-18 00:00:00')}
data = db.collection('AXPYdb/1Rclo6rXIJagoFvIGUwC/UserData').stream()
data_dic = {}
for i in data:
    data_dic[i.id] = i.to_dict()
print(f'{len(data_dic)} records found')

a = ut.get_records_from_firebase(db,'SellServiceN1/UserDetails/Userlist')
import pandas as pd
df = pd.read_excel('Vacaciones utilizadas.xlsx',engine='openpyxl')
a = df.to_dict('r')