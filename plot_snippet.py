# MODULES REQUIRED
import matplotlib.pyplot as plt
import os
import pandas



# CSV file from which data is to be read
file_name="Values.CSV"

#location of the file in your PC
location ="C:\\vibhuti\\timater\\rusk"

#Function to plot, this function should be called from main.
def Function_Plot(): 
	for root, dirs, files in os.walk(location):
		for file in files:
			if file.endswith(".CSV"):
				if file == file_name:
					target_file = os.path.join(root, file) #complete path to the values file

					#Read data from each file in top level folder and plot graphs into a dataframe , Usecols includes only desired column
					Data2Plot = pandas.read_csv(target_file,usecols=[0,1,2,3,4,5,6,7,8,9])

					#if you want to modify values like inf to float or precise the values
					Data2Plot['Time (ms)'] = Data2Plot['Time (ms)']/1000
					Data2Plot['Time (ms)'] = Data2Plot['Time (ms)'].astype(int)

					#plotting 
					Data2Plot.plot(x=0,y=[1,2,3,4,5,6,7,8,9],figsize=(15,6),linewidth=1)

					#setting the X Y Axis names
					plt.xlabel('Time (s)',fontsize = 12)
					plt.ylabel('All Tasks',fontsize = 12)

					#Title of the Graph
					plt.title('Graph Title',y=1.1,fontsize = 14)
					plt.legend(loc='best') #curve names tag
					plt.show() #to view
					plt.savefig("Give the path with filename.png to save") #to save in your PC
					plt.close() 