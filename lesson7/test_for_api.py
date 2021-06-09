import requests
import unittest

class BookTests(unittest.TestCase):

    def setUp(self):
        print("set up\n")
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"

    def tearDown(self):
        print("\nTearDown\n")

    def test_create_book(self):
        book_data = {"title": "some", "author": "A"}
        resp = requests.post("{}/books/".format(self.base_url), data=book_data)
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        book_id = body.pop("id")
        self.assertDictEqual(book_data, body)

        for key in book_data:
            self.assertEqual(book_data[key], body[key])



if __name__ == "__main__":
    unittest.main()
