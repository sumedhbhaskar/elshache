"""
	file writing and reading scripts for encryption app
"""
from demobackend import *

def generateShares(secret,totalshare,min_share):
	obj = elshache(secret,totalshare,min_share)

	share_verifier = obj.randomNumberInverse

	sharelist = obj.shareConstruction()

	with open("Share_List.txt", "+a") as f:

		for i in range(1,totalshare+1):
			f.write("Share {} is: {} \n".format(i,sharelist[i-1]))

		f.write("Share Verifier is: {} ".format(share_verifier))	

	


def generateKey(filename,min_share,share_verifier):
	obj = elshache_re()
	with open("{}".format(filename),"r") as f:
		data = f.readline()
		data = data.split()
	x_list = []
	y_list = []
	for i in range(len(data)):
		if(i%2==0):
			x_list.append(int(data[i]))
		else:
			y_list.append(int(data[i]))  
 
	a0_coef = obj.shareReconstruction(x_list,y_list,min_share)
	a1_coef = obj.shareReconstruction_a1(x_list,y_list,min_share,share_verifier)

	verifyKey(a0_coef,a1_coef)






def verifyKey(a0_key,a1_key):
	if(a0_key == a1_key):	
		with open("SecretKey.txt","+a") as f:
			f.write("Congratulations, your secret is {} (for debug pupose: your key{} and your verifing key {}".format(a0_key,a0_key,a1_key))

	else:
		with open("SecretKey.txt","+a") as f:
			f.write("Oops, your secret key can't be generated. Your verifying key and secret key don't match. For debugging purpose here are your two keys: {} and {}".format(a0_key,a1_key))				
	


