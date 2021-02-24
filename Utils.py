
import firebase_admin
from firebase_admin import credentials, firestore, storage
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import base64

################
    #Firebase connection - Class probably
################

def create_connection_firebase(path):
    cred = credentials.Certificate(path)
    default_app = firebase_admin.initialize_app(cred, {'storageBucket':'axpycs.appspot.com'})
    db = firestore.client()
    return db

def get_records_from_firebase(db,path):
    data = db.collection(path).stream()
    data_dic = {}
    for i in data:
        data_dic[i.id] = i.to_dict()
    print(f'{len(data_dic)} records found')
    return data_dic

def add_record_to_firebase(db,path,key,values):
    db_create = db.collection(path)
    try:
        db.collection(path).document(key).set(values)
        print(f'key {key} has been uploaded with {len(values)} records')
    except:
        print(f'Try again, there is an issue in the key {key}')

def add_image(db,path, user_name):
    bucket = storage.bucket()
    im = bucket.blob(user_name+'.jpg')
    im.upload_from_filename(path)
    im.make_public()
    url_f = str(im.public_url).encode('ascii')
    #base64.b64encode(sample_string_bytes)  | base64_bytes.decode("ascii")
    return base64.b64encode(url_f)

def decode_link(url_f):
    url_f = url_f.encode('ascii')
    url_f = base64.b64decode(url_f)
    return url_f.decode('ascii')


################
    #Open file -
################

def choose_file():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


