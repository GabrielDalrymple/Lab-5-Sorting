import sys
import sort
import random
import timeit
'''
#INITIAL BUG TESTING
myList = [8,7,3,9,1,5,4,2,6,10]
print(myList)
sort.bubbleSort(myList)
sort.insertionSort(myList)
sort.shellSort(myList)
sort.mergeSort(myList, 0, len(myList)-1)
sort.iterativeMergeSort(myList)
sort.quickSort(myList, 0, len(myList)-1)
print(myList)
'''


#ACTUAL DRIVER PART TO TAKE COMMAND LINE INPUTS

#check minimum system args
if len(sys.argv) < 3:
	print("Too few arguments, please try again")

#assign argument values
sortType = sys.argv[1]
listSize = eval(sys.argv[2])
printList = False

#check if print 
if len(sys.argv) == 4 and sys.argv[3] == "PRINT":
	printList = True

#make list
myList = []
for i in range(listSize):
	myList.append(random.randint(0, (listSize * 10) + 1))

#if printing the list, print the unsorted list
if printList:
	print("Unsorted: ", myList)
#run appropriate sorting algorithm
if sortType == "BubbleSort":
	print("BubbleSort")
	sort.bubbleSort(myList)
if sortType == "InsertionSort":
	print("InsertionSort")
	sort.insertionSort(myList)
if sortType == "MergeSort":
	print("MergeSort")
	sort.mergeSort(myList, 0, len(myList)-1)
if sortType == "IterativeMergeSort":
	print("IterativeMergeSort")
	sort.iterativeMergeSort(myList)
if sortType == "QuickSort":
	print("QuickSort")
	sort.quickSort(myList, 0, len(myList)-1)
if sortType == "ShellSort":
	print("ShellSort")
	sort.shellSort(myList)
#if we need to print, then print the sorted list
if printList:
	print("Sorted: ", myList)



'''
#TIMING PORTION OF THE PROGRAM

def allTests():
	sortStyles = ["bubble", "insertion", "merge", "iterMerge", "quick", "shell"]
	listSizes = [10, 100, 1000, 5000, 10000, 25000]
	for style in sortStyles:
		print()
		for size in listSizes:
			timer = timeit.Timer(style + "(" + str(size) + ")", "from __main__ import " + style)
			duration = timer.timeit(1)
			print(style, "with", size, "emelents took:", duration, "seconds to execute")
	return None
def bubble(size):
	list = []
	for k in range(0, size):
		list.append(random.randint(0, (10 * k)+1))
	sort.bubbleSort(list)
def insertion(size):
	list = []
	for k in range(0, size):
		list.append(random.randint(0, (10 * k)+1))
	sort.insertionSort(list)
def merge(size):
	list = []
	for k in range(0, size):
		list.append(random.randint(0, (10 * k)+1))
	sort.mergeSort(list, 0, len(list)-1)
def iterMerge(size):
	list = []
	for k in range(0, size):
		list.append(random.randint(0, (10 * k)+1))
	sort.iterativeMergeSort(list)
def quick(size):
	list = []
	for k in range(0, size):
		list.append(random.randint(0, (10 * k)+1))
	sort.quickSort(list, 0, len(list)-1)
def shell(size):
	list = []
	for k in range(0, size):
		list.append(random.randint(0, (10 * k)+1))
	sort.shellSort(list)

allTests()
'''