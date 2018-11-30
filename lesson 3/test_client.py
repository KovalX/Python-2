import unittest
import time
from errors import ResponseCodeError, ResponseCodeLenError, MandatoryKeyError, UsernameTooLongError
from client import create_presence, translate_message


class CreatePresence(unittest.TestCase):
    # check if type of function argument is str
    def test_create_presence_type(self):
        with self.assertRaises(TypeError):
            create_presence(4578)

    # check if length of function argument is less 24
    def test_create_presence_len(self):
        with self.assertRaises(UsernameTooLongError):
            create_presence("qwertyuiiuooouytoasdfgkklnmghkl")

    def test_create_presence(self):
        self.assertEqual(create_presence('ADMIN'),
                         {'action': 'presence', 'time': time.asctime(), 'user': {'account_name': 'ADMIN'}})


class TranslateMes(unittest.TestCase):
    # check if code is right
    def test_translate_mes_in_correct_resp(self):
        with self.assertRaises(ResponseCodeError):
            translate_message({'response': 700})

    # check if function argument is dictionary
    def test_translate_mes_in_type(self):
        with self.assertRaises(TypeError):
            translate_message(['response', 200])

    # check if key "response" is in response
    def test_translate_mes_key(self):
        with self.assertRaises(MandatoryKeyError):
            translate_message({"": 200})

    # check length of code
    def test_translate_mes_in_correct_len_resp(self):
        with self.assertRaises(ResponseCodeLenError):
            translate_message({'response': 7200})

    def test_translate_message(self):
        response = {'response': 200}
        self.assertEqual(translate_message(response), {'response': 200})


if __name__ == '__main__':
    unittest.main()
