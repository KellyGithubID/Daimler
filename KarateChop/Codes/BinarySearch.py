class BinarySearch:
    def __init__(self, given_array=[], given_target_number=0):
        self.array = given_array
        self.target_number = given_target_number
        self.low_index = 0
        self.high_index = len(self.array) - 1
        self.middle = self.find_middle_index()

    def find_middle_index(self):
        return (self.low_index + self.high_index - 1) // 2 + 1

    def search_index_of_target_number(self):
        if len(self.array) == 0:
            return -1
        return self.search_array()

    def search_array(self):
        while -1 < self.low_index <= self.high_index < len(self.array):
            if self.target_number_found():
                return self.middle
            self.update_middle_index()
        return -1

    def target_number_found(self):
        self.middle = self.find_middle_index()
        return self.array[self.middle] == self.target_number

    def update_middle_index(self):
        if self.array[self.middle] > self.target_number:
            self.high_index = self.middle - 1
        else:
            self.low_index = self.middle + 1
