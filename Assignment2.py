def remove_items(a, item):
	res = [i for i in a if i != item]
	return res
if __name__=="__main__":
	a = [1,3,1,3,2,5,7,9,2,1]
	item = 1
	print ("The original list is : " + str(a))
	res = remove_items(a , item)
	print ("The list after removing all occurence of item: " + str(res))
