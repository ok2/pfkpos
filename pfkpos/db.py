from datetime import timedelta
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions, QueryOptions)

username = "Administrator"
password = "fall vine edit goof bode fir"
bucket_name = "RFKPOS"

auth = PasswordAuthenticator(username, password)
cluster = Cluster('couchbase://localhost', ClusterOptions(auth))
cluster.wait_until_ready(timedelta(seconds=5))

rfkpos = cluster.bucket("RFKPOS")
inventory = rkfpos.scope("Inventory")
system = inventory.collection("System")
transactions = inventory.collection("Transactions")

def next_transaction_id():
    tid = system.increment('nextTransactionID').get('content')
    return f't{tid:020}'

