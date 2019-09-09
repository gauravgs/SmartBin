import pyrebase
from datetime import datetime
firebaseConfig = {
    'apiKey': "AIzaSyD-nqdhZtiIol5psI1_BkIwMAAa3keOX9I",
    'authDomain': "data-8889a.firebaseapp.com",
    'databaseURL': "https://data-8889a.firebaseio.com",
    'projectId': "data-8889a",
    'storageBucket': "data-8889a.appspot.com",
    'messagingSenderId': "489236791138",
    'appId': "1:489236791138:web:caaf218e465375eb"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
now = datetime. now()
alfa = distance
timestamp = datetime. timestamp(now)
data = {
    "cap": "50", "fil": alfa, "lastupdate": str(int(timestamp))
}
results = db.child("Bin1").set(data)
