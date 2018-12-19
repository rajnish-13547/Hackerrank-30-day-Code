class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here

    def computeDifference(self):
        a1 = min(self.__elements)
        a2 = max(self.__elements)
        self.maximumDifference = a2-a1

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
