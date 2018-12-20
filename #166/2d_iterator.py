class tdIterator:
    def __init__(self, arrayList):
        self.arrayList = arrayList

    def next(self):
        try:
            if isinstance(self.arrayList[0], list):
                if len(self.arrayList[0]) > 0:
                    num = self.arrayList[0][0]
                    self.arrayList[0].remove(num)
                    if len(self.arrayList[0]) == 0:
                        self.arrayList.remove(self.arrayList[0])
                    return num
                else:
                    self.arrayList.remove(self.arrayList[0])
                    return self.next()
        except IndexError:
            raise

    
    def has_next(self):
        try:
            if isinstance(self.arrayList[0], list):
                if len(self.arrayList[0]) > 0:
                    return True
                else:
                    return False
        except IndexError:
            raise

if __name__ == "__main__":
    td_iterator = tdIterator([[1, 2], [3], [], [4, 5, 6]])
    import pdb; pdb.set_trace()
    for y in range(7):
        print(td_iterator.next())
    
    