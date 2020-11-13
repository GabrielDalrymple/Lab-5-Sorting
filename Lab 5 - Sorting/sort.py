def bubbleSort(myList):
	#run through the list
	for i in range(len(myList)):
		#run through the rest of the list
		for j in range(0, len(myList)-i-1):
			#check if you should bubble
			if myList[j] > myList[j+1]:
				#bubble up number
				myList[j], myList[j+1] = myList[j+1], myList[j]
	return

def insertionSort(myList):
	#run throught the list
	for i in range(1, len(myList)):
		#key value to swap with
		key = myList[i]
		#shift elements to the right
		j = i-1
		while j >= 0 and key < myList[j]:
			#workhorse of shifting
			myList[j+1] = myList[j]
			j -= 1
		myList[j+1] = key
	return

def shellSort(myList):
	#start with a big gap equal to half the list size
	n = len(myList)
	gap = n//2
	#loop until point at outselves
	while gap > 0:
		#run throught rest of the list from the pivot
		for i in range(gap, n):
			temp = myList[i]
			j = i
			#loop while bounding by the index
			while j >= gap and temp < myList[j-gap]:
				myList[j] = myList[j-gap]
				j -= gap
			myList[j] = temp
			#edge cases of gap bounding for final round
		if gap == 2:
			gap = 1
		else:
			gap = int(gap/2.2)
	return

def mergeSort(myList, first, last):
	#repeat until at list size of 1
	if first < last:
		mid = (first + last) // 2
		#sort the left side first
		mergeSort(myList, first, mid)
		#sort the right side
		mergeSort(myList, mid+1, last)
		#merge toegether
		mergeSortMerge(myList, first, mid, last)
	return

def mergeSortMerge(myList, first, mid, last):
	#temp list to help with mergeSort
	tempList = [0] * (last - first + 1)
	index = 0
	#first half of sorted list
	f1 = first
	l1 = mid
	#second half of sorted list
	f2 = mid+1
	l2 = last
	#iterate while both lists haven't reached their ends
	while f1 <= l1 and f2 <= l2:
		if myList[f1] < myList[f2]:
			tempList[index] = myList[f1]
			f1 +=1
		else:
			tempList[index] = myList[f2]
			f2 += 1
		index += 1
	#finish off the first list
	while f1 <= l1:
		tempList[index] = myList[f1]
		f1 += 1
		index += 1
	#finish off the second list
	while f2 <= l2:
		tempList[index] = myList[f2]
		f2 += 1
		index += 1
	#copy list back to original list
	for num in tempList:
		myList[first] = num
		first += 1
	return

def iterativeMergeSort(myList):
	#temp list to copy back and forth from
	tempList = [0]*len(myList)
	#initial partition size per pass
	partition = 2
	#boolean to pass to tempList or original list
	sendToTemp = True
	#remember the last j index
	lastJ = 0
	#get size of list
	size = len(myList)
	#keep looping until we've exceeded the length of the list
	while partition <= size:
		j = 0
		#move through the list jumping by the partition size
		while j < size:
			end = j + partition - 1
			if end < size:
				#find the mid point
				mid = (j + end) // 2
				#either send to the temp list or back to the original list
				if sendToTemp:
					iterativeMerge(myList, tempList, j, mid, end)
				else:
					iterativeMerge(tempList, myList, j , mid, end)
			else:
				mid = j + ((size - j) // 2)
				if sendToTemp:
					iterativeMerge(myList, tempList, j, mid, size - 1)
				else:
					iterativeMerge(tempList, myList, j, mid, size-1)
			#remember last j for cleanup
			lastJ = j
			#step to next partition
			j += partition
		#swap sending to original list or temp list
		if sendToTemp:
			sendToTemp = False
		else:
			sendToTemp = True
		#double partition size to mimic logn
		partition *= 2
	#check to see if we need to do one last swap for non power of 2 numbers
	if partition != size:
		if sendToTemp:
			iterativeMerge(myList, tempList, 0, lastJ - 1, size-1)
			sendToTemp = False
		else:
			iterativeMerge(tempList, myList, 0, lastJ - 1, size - 1)
	#copy back to original list if our last write was to tempList
	if not sendToTemp:
		for i in range(size):
			myList[i] = tempList[i]
	return

def iterativeMerge(fromList, toList, first, mid, last):
	#store size of list
	size = (last - first) + 1
	#left sorted half
	f1 = first
	l1 = mid
	#right sorted half
	f2 = mid + 1
	l2 = last
	index = first
	#run the lists while both haven't reached their ends
	while f1 <= l1 and f2 <= l2:
		#either take from left or right half based on which is lowest value
		if fromList[f1] < fromList[f2]:
			toList[index] = fromList[f1]
			f1 += 1
		else:
			toList[index] = fromList[f2]
			f2 += 1
		#always increase index
		index += 1
	#clean up remaining lists
	while f1 <= l1:
		toList[index] = fromList[f1]
		f1 += 1
		index += 1
	while f2 <= l2:
		toList[index] = fromList[f2]
		f2 += 1
		index += 1
	return

def quickSort(myList, low, high):
	if low < high:
		index = partitionIndex(myList, low, high)
		quickSort(myList, low, index-1)
		quickSort(myList, index+1, high)
	return

def partitionIndex(myList, low, high):
	index = low
	for i in range(low, high):
		if myList[i] < myList[high]:
			myList[i], myList[index] = myList[index], myList[i]
			index += 1
	myList[index], myList[high] = myList[high], myList[index]
	return index