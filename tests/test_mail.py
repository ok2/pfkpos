from .context import pfkpos
import unittest, tomllib

class MailTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        with open('config.toml', 'rb') as fd:
            self.config = tomllib.load(fd)

    def test_connect(self):
        server = pfkpos.mails.FetchMails(self.config)
        mails = server.mails('FROM', 'nettbutikk@sg.no')
        msg = server.fetch(mails[0])
        with open('data/test1', 'wb') as fd:
            fd.write(msg)
        try:
            self.assertEqual(server, 1)
        finally: server.close()

if __name__ == '__main__':
    unittest.main()
