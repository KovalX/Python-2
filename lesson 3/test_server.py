import unittest
from server import presence_response
from JIM.utils import dict_to_bytes, bytes_to_dict


class PresenceResponse(unittest.TestCase):
    def test_presence_response_full(self):
        self.assertEqual(presence_response(
            {'action': 'presence', 'time':  'Thu Nov 29 22:02:48 2018', 'user': {'account_name': 'Guest'}}),
            {'response': 200})

    # check if key "action" is in function argument
    def test_presence_response_action(self):
        self.assertEqual(presence_response(
            {'time':  'Thu Nov 29 22:02:48 2018', 'user': {'account_name': 'Guest'}}),
            {'response': 400, 'error': 'Неверный запрос'})

    # check if key "action" has a correct value
    def test_presence_response_action_correct(self):
        self.assertEqual(presence_response(
            {'action': 'existence', 'time': 'Thu Nov 29 22:02:48 2018', 'user': {'account_name': 'Guest'}}),
            {'response': 400, 'error': 'Неверный запрос'})

    # check if key "time" is in function argument
    def test_presence_response_time(self):
        self.assertEqual(presence_response(
            {'action': 'action', 'user': {'account_name': 'Guest'}}),
            {'response': 400, 'error': 'Неверный запрос'})


class DictToBytes(unittest.TestCase):
    # check if type of function argument is dict
    def test_dict_to_bytes_type(self):
        with self.assertRaises(TypeError):
            dict_to_bytes(["response", 200])

    def test_dict_to_bytes(self):
        self.assertEqual(dict_to_bytes({'response': 200}), b'{"response": 200}')


class BytesToDict(unittest.TestCase):
    # check if type of function argument is bytes
    def test_bytes_to_dict_type(self):
        with self.assertRaises(TypeError):
            bytes_to_dict({'response': 200})

    def test_bytes_to_dict(self):
        self.assertEqual(bytes_to_dict(b'{"response": 200}'), {"response": 200})


if __name__ == '__main__':
    unittest.main()
