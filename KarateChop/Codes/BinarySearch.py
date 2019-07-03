class BinarySearch:
    def __init__(self, given_array=[], given_target_number=0):
        self.array = given_array
        self.target_number = given_target_number

    def search_index_of_target_number(self):
        if len(self.array) == 0:
            return -1
