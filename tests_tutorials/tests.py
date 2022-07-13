import unittest
from unittest.mock import MagicMock, patch

from main import len_joke, get_joke


class TestJoke(unittest.TestCase):

    # The decorator "patch" creates a special fake object, a MagicMock object, and passes
    # The reference to it into the decorated function (test_len_joke in this case)
    # Using the patch eliminates the dependency of the len_joke function on the get_joke function
    # Helps the test be independent from the return value of the get_joke function
    # Also eliminates dependency on internet connection or remote API server
    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    @patch("main.requests")
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "hello world"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "hello world")

    @patch("main.requests")
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_response.json.return_value = {"value": {"joke": "hello world"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "No jokes")


if __name__ == "__main__":
    unittest.main()
