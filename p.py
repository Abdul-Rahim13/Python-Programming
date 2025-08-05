class Find_pair:
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target
    
    def find_pair(self):
        for i in range(len(self.lst)):
            for j in range(i+1, len(self.lst)):
                if self.lst[i] + self.lst[j] == self.target:
                    print(f"Pair found at indices: {i}, {j}")

list = [1,2,3,4,5,6,7,8,9,10]
tar = 6
FP = Find_pair(list, tar)
FP.find_pair()