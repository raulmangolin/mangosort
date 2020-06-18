import unittest

from mangosort import mangosort


class SortTest(unittest.TestCase):
    def setUp(self):
        self.unsorted_list = [{"key1": "a", "key2": "2", "key3": "A"}, {"key1": "d", "key2": "2", "key3": "A"},
                              {"key1": "b", "key2": "1", "key3": "B"}, {"key1": "a", "key2": "2", "key3": "B"},
                              {"key1": "b", "key2": "1", "key3": "A"}, {"key1": "b", "key2": "2", "key3": "B"},
                              {"key1": "d", "key2": "1", "key3": "B"}, {"key1": "a", "key2": "1", "key3": "B"},
                              {"key1": "c", "key2": "2", "key3": "B"}, {"key1": "c", "key2": "2", "key3": "A"},
                              {"key1": "c", "key2": "1", "key3": "B"}, {"key1": "c", "key2": "1", "key3": "A"},
                              {"key1": "b", "key2": "2", "key3": "A"}, {"key1": "a", "key2": "1", "key3": "A"},
                              {"key1": "d", "key2": "2", "key3": "B"}, {"key1": "d", "key2": "1", "key3": "A"}]

        self.sorted_list_multiple = [{'key3': 'B', 'key2': '1', 'key1': 'd'}, {'key3': 'A', 'key2': '1', 'key1': 'd'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'd'}, {'key3': 'A', 'key2': '2', 'key1': 'd'},
                                     {'key3': 'B', 'key2': '1', 'key1': 'c'}, {'key3': 'A', 'key2': '1', 'key1': 'c'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'c'}, {'key3': 'A', 'key2': '2', 'key1': 'c'},
                                     {'key3': 'B', 'key2': '1', 'key1': 'b'}, {'key3': 'A', 'key2': '1', 'key1': 'b'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'b'}, {'key3': 'A', 'key2': '2', 'key1': 'b'},
                                     {'key3': 'B', 'key2': '1', 'key1': 'a'}, {'key3': 'A', 'key2': '1', 'key1': 'a'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'a'}, {'key3': 'A', 'key2': '2', 'key1': 'a'}]

        self.sorted_list_multiple2 = [{'key3': 'B', 'key2': '1', 'key1': 'd'}, {'key3': 'A', 'key2': '1', 'key1': 'd'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'd'}, {'key3': 'A', 'key2': '2', 'key1': 'd'},
                                     {'key3': 'B', 'key2': '1', 'key1': 'c'}, {'key3': 'A', 'key2': '1', 'key1': 'c'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'c'}, {'key3': 'A', 'key2': '2', 'key1': 'c'},
                                     {'key3': 'B', 'key2': '1', 'key1': 'b'}, {'key3': 'A', 'key2': '1', 'key1': 'b'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'b'}, {'key3': 'A', 'key2': '2', 'key1': 'b'},
                                     {'key3': 'B', 'key2': '1', 'key1': 'a'}, {'key3': 'A', 'key2': '1', 'key1': 'a'},
                                     {'key3': 'B', 'key2': '2', 'key1': 'a'}, {'key3': 'A', 'key2': '2', 'key1': 'a'}]

        self.sorted_list_desc = [{'key3': 'B', 'key2': '2', 'key1': 'd'}, {'key3': 'A', 'key2': '2', 'key1': 'd'},
                                 {'key3': 'B', 'key2': '1', 'key1': 'd'}, {'key3': 'A', 'key2': '1', 'key1': 'd'},
                                 {'key3': 'B', 'key2': '2', 'key1': 'c'}, {'key3': 'A', 'key2': '2', 'key1': 'c'},
                                 {'key3': 'B', 'key2': '1', 'key1': 'c'}, {'key3': 'A', 'key2': '1', 'key1': 'c'},
                                 {'key3': 'B', 'key2': '2', 'key1': 'b'}, {'key3': 'A', 'key2': '2', 'key1': 'b'},
                                 {'key3': 'B', 'key2': '1', 'key1': 'b'}, {'key3': 'A', 'key2': '1', 'key1': 'b'},
                                 {'key3': 'B', 'key2': '2', 'key1': 'a'}, {'key3': 'A', 'key2': '2', 'key1': 'a'},
                                 {'key3': 'B', 'key2': '1', 'key1': 'a'}, {'key3': 'A', 'key2': '1', 'key1': 'a'}]

        self.sorted_list_asc = [{'key3': 'A', 'key2': '1', 'key1': 'a'}, {'key3': 'B', 'key2': '1', 'key1': 'a'},
                                {'key3': 'A', 'key2': '2', 'key1': 'a'}, {'key3': 'B', 'key2': '2', 'key1': 'a'},
                                {'key3': 'A', 'key2': '1', 'key1': 'b'}, {'key3': 'B', 'key2': '1', 'key1': 'b'},
                                {'key3': 'A', 'key2': '2', 'key1': 'b'}, {'key3': 'B', 'key2': '2', 'key1': 'b'},
                                {'key3': 'A', 'key2': '1', 'key1': 'c'}, {'key3': 'B', 'key2': '1', 'key1': 'c'},
                                {'key3': 'A', 'key2': '2', 'key1': 'c'}, {'key3': 'B', 'key2': '2', 'key1': 'c'},
                                {'key3': 'A', 'key2': '1', 'key1': 'd'}, {'key3': 'B', 'key2': '1', 'key1': 'd'},
                                {'key3': 'A', 'key2': '2', 'key1': 'd'}, {'key3': 'B', 'key2': '2', 'key1': 'd'}]

    def test_multiple(self):
        my_sorted_list = mangosort.sort_by_key(self.unsorted_list, [{"key1": True}, {"key2": False}, {"key3": 1}])
        self.assertEquals(my_sorted_list, self.sorted_list_multiple)

    def test_multiple_string(self):
        my_sorted_list = mangosort.sort_by_key(self.unsorted_list, [{"key1": 'DESC'}, {"key2": 'asc'}, {"key3": True}])
        self.assertEquals(my_sorted_list, self.sorted_list_multiple2)

    def test_asc(self):
        my_sorted_list = mangosort.sort_by_key_asc(self.unsorted_list, ["key1", "key2", "key3"])
        self.assertEquals(my_sorted_list, self.sorted_list_asc)

    def test_desc(self):
        my_sorted_list = mangosort.sort_by_key_desc(self.unsorted_list, ["key1", "key2", "key3"])
        self.assertEquals(my_sorted_list, self.sorted_list_desc)


if __name__ == "__main__":
    unittest.main()
