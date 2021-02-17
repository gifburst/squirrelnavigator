import unittest
import sys
sys.path.insert(0, '../')
import akasia


class TestMain(unittest.TestCase):

    def test_get_request(self):
        request_get = akasia.get_request('https://google.com')
        self.assertEqual(str(request_get[1]), '<Response [200]>')


if __name__ == "__main__":
    print('Version: ' + akasia.VERSION + '\n')
    unittest.main()
