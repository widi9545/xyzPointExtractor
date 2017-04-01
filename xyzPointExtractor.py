import random
import argparse
import time

pointList = []

class glacierPoints:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.seq_data = ""

def readPoints(file):
	id = 0
	counter = 0
	
	line = file.readline()
	
	newPoint = glacierPoints(id, line)
	pointList.append(newPoint)
	pointData = line[:-1]
	newPoint.seq_data = pointData

	while line != '':

		newPoint = glacierPoints(id, line)
		pointList.append(newPoint)
		pointData = ""
		line = file.readline()

		while line != '' and line[0].isdigit() == True:
			pointData += line[:-1]
			break
		newPoint.seq_data = pointData
		id += 1
		
def swap(A, x, y):
	A[x], A[y] = A[y], A[x]
	return A

def randomizedPartition(A, p,r):
	i = random.randrange(p,r)
	swap(A, r, i)
	return partition(A,p,r)

def randomizedQuicksort(A,p,r):
	if p < r:
		q = randomizedPartition(A,p,r)
		randomizedQuicksort(A,p,q-1)
		randomizedQuicksort(A,q+1,r)

def partition(A,p,r):
	 x = A[r][0]
	 i = p - 1
	 for j in range(p, r):
	 	if A[j][0] <= x:
	 		i = i + 1
	 		swap(A, i, j)
	 swap(A, i+1, r)
	 return i + 1

def xyzPointExtractor(xyzPointList):
	tempList = []

	counter = 0
	index = 0
	xPoint = 0
	yPoint = 0
	zPoint = 0

	for x in range(0, len(pointList)-1):
		for y in pointList[x].seq_data:
			tempList.append(y)
			counter += 1

			if y == ' ' and index == 0:
				xPoint= float("".join(tempList[index:counter]))
				index = counter
				
			elif y == ' ' and index != 0:
				yPoint = float("".join(tempList[index:counter]))
				zPoint = float(pointList[x].seq_data[counter:])
				pointListBuilder = [xPoint, yPoint, zPoint]
				xyzPointList.append(pointListBuilder)

				counter = 0 
				index = 0
				tempList = []

				break

	return xyzPointList

def outputToFile(xyzPointList):
	newFile = open('xyzSortedPoints', 'w')
	for x in xyzPointList:
		for y in range(0, 3):
			newFile.write(str(x[y])), newFile.write(" ")
		newFile.write("\n")
	newFile.close()
	return 1

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-F', '-f', '--file', type=file, help="point", required=True)
	args = parser.parse_args()
	xyzPointList = []
	readPoints(args.file)
	xyzPointExtractor(xyzPointList)
	randomizedQuicksort(xyzPointList, 0, len(xyzPointList)-1)
	outputToFile(xyzPointList)
	print xyzPointList





	


			
	

	



if __name__=="__main__":
	main()