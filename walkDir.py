import os

def listdir_fullpath(d):
#    return [os.path.join(d, f) for f in os.listdir(d)]
	path_list=[]
	for i in os.listdir(d):
		path_list.append(os.path.join(d,i))
	return path_list


list1=listdir_fullpath("/root")
print list1
