import unittest

from unittest import TestCase

from unittest.mock import patch, call

import Bitcoin

class TestBitcoin(TestCase):
    
    
    @patch('Bitcoin.call_bitcoin_api')
    def test_call_bitcoin_api(self, mock_call_bitcoin_api):
        
        value = Bitcoin.call_bitcoin_api('https://api.coindesk.com/v1/bpi/currentprice.json', 1)
        print(value)
        
    @patch('builtins.input', side_effect=['1'])
    @patch('Bitcoin.call_bitcoin_api')
    def test_main(self, mock_call_bitcoin_api, mock_input):
        mock_call_bitcoin_api.return_value = 100
        Bitcoin.main()
        mock_call_bitcoin_api.assert_called_once_with('https://api.coindesk.com/v1/bpi/currentprice.json', 1)
        

if __name__ == '__main__':
    unittest.main()