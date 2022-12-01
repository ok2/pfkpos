import imaplib
from typing import Dict, Any, List, Tuple

class FetchMails:
    def __init__(self, config: Dict[str, Any]):
        self.server = imaplib.IMAP4_SSL(config['mail']['server'])
        self.server.login(config['mail']['username'], config['mail']['password'])
        self.server.select('Important')

    def mails(self, *args: str) -> List[int]:
        res, data = self.server.search(None, *args)
        if res != 'OK': raise RuntimeError(f'Failed to search mails: {res}-{data}')
        return list([int(x) for x in data[0].split()])

    def fetch(self, msg: int) -> bytes:
        res, data = self.server.fetch(str(msg), '(RFC822)')
        if res != 'OK': raise RuntimeError(f'Failed to search mails: {res}-{data}')
        if type(data) is list and type(data[0]) is tuple and type(data[0][1]) is bytes:
            return data[0][1]
        raise RuntimeError("Wrong email data")

    def close(self):
        self.server.close()
        self.server.logout()
