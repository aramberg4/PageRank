#
#  Program Name: pageRank.py
#  
#  Created by Austin Ramberg on 4/22/17.
#  Copyright © 2017 Austin Ramberg. All rights reserved.
#
#  Purpose: This program is a very basic Python implementation of the PageRank 
#  algorithm derived by Lawrence Page and Sergey Brin


from numpy import matrix
from numpy import linalg
from math import sqrt
from numpy import array
from numpy import loadtxt

def main():
	# Load matrix from csv
	M = loadMatrix("matrix.csv")
	#M = matrix( [[0,1,1,0],[0,0,1,0],[0,0,0,1],[1,1,0,0]])
	#M = matrix( [[0,1,1,0,0],[0,0,1,0,1],[0,0,0,1,0],[1,1,0,0,1],[1,0,0,0,0,]])

	# Find the number of nodes
	nodes = int(sqrt(M.size))

	# Sum each row of the matrix to compute the number of outlinks for each node
	outlinks = M.sum(axis=1).flatten("C")
	outlinks = array(outlinks.tolist())# Store in array
	print "outlinks: " + str(outlinks)

	# The inlinks of each node (1 = link, 0 = no link)
	columns = M.transpose()

	# Initialize all pagerank values to 1
	qs = [1] * nodes

	# Number of iterations of the recursive function (typically 15)
	iterations = input("How many iterations would you like to run? ")

	# Damping factor
	d = 0.85

	# Iterate recursively
	for j in range (0,iterations):
		print "iteration: " + str(j+1)
		# Call to computePageRank
		qs = computePageRank(qs, nodes, outlinks, columns, d)
		print

def loadMatrix(fileName):
	# Load matrix from csv file
	M = loadtxt(fileName,delimiter=",")
	# Display Matrix
	print "Below is the matrix representation of the realtionship between webpages: "
	print M
	return M

def computePageRank(qs, nodes, outlinks, columns, d):
	# placeholder
	new_qs = [1] * nodes

	for i in range(0, nodes): # For each node do the following:
		# Get inlinks of node
		column = array(columns[i].tolist())
		# Store the number of outlinks each inlink node has in list
		crossList = column * outlinks
		sum = 0
		for x in range(0, len(crossList)):
			if crossList[x] > 0:
				# Divide previous pagerank of inlink node by the crosslist value of 
				# that node and add to sum
				sum += (float(qs[x])/float(crossList[x]))
		# Compute new pagerank score for node using damping factor and sum
		new_qs[i] = (1 - d) + d*(sum)
	print new_qs
	return new_qs

if __name__=="__main__":
   main()

