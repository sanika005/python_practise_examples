from count_freq_each_char_in_string import test1

obj = test1()

inputted_string = "GEEKSFORGEEKS"
expected_output = {'G': 2, 'E': 4, 'K': 2, 'S': 2, 'F': 1, 'O': 1, 'R': 1}


def test_no_of_occ(inputted_string):
    actual_output = obj.count_occr_of_each_char(inputted_string)
    assert(actual_output,expected_output)