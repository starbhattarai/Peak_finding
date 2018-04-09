class Peak:
	def __init__(self, array):
		self.array = array

	def peakfun(self,array):
		start = 0
		end = len(array)-1
		peak = None
		while(peak==None):
			mid = int((start + end)/2)
			if(mid == end):
				peak = array[mid]
			elif (array[mid -1] > array[mid]):
				end = mid -1
			elif (array[mid]<array[mid+1]):
				start = mid +1
			else :
				peak = array[mid]
		return peak	
		
def main():
	array = []
	print("Please enter the value for array")
	a = 0
	a = input()
	array = [int(item) for item in a.split(",")]
	x=Peak(array)
	peakm = x.peakfun(array)
	print(peakm)

if __name__ == "__main__":
	main()
