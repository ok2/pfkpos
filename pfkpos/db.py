from typing import Dict, Any
from datetime import timedelta
from couchbase.auth import PasswordAuthenticator # type: ignore
from couchbase.cluster import Cluster # type: ignore
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions, QueryOptions) # type: ignore

class DB:
    def __init__(self, config: Dict[str, Any]):
        username = config['db']['username']
        password = config['db']['password']
        server = config['db']['url']
        self.auth = PasswordAuthenticator(username, password)
        self.cluster = Cluster(server, ClusterOptions(self.auth))
        self.cluster.wait_until_ready(timedelta(seconds=5))
        
        self.pfkpos = self.cluster.bucket("RFKPOS")
        self.inventory = self.pfkpos.scope("Inventory")
        self.system = self.inventory.collection("System")
        self.transactions = self.inventory.collection("Transactions")

    def next_transaction_id(self):
        tid = self.system.increment('nextTransactionID').get('content')
        return f't{tid:020}'

