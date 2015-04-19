# sort_fruits.py
# Written for Python 3.4.3
# Revision date: 3/15/15

# By: A. Programmer

#---------------------------------------------------------------------------------------
# This program will sort the unsorted_fruits.txt file and write sorted_fruits.txt file back
#
# CAUTION: Make sure that the unsorted_fruits.txt file is in the same directory
#                    that this program is run from.
#---------------------------------------------------------------------------------------

# Lets open the file in the Python way and load the data into fruit
infile=open("unsorted_fruits.txt", "r")
outfile=open("sorted_fruits.txt", "w")

# READ in the lines of the textfile into a LIST while eliminating the linefeeds
fruit=infile.read().splitlines()

# Get rid of the pesky blanks in the LIST and show the unsorted, cleaned list
while '' in fruit:
    fruit.remove('')
print("Unsorted text file with linefeeds and blanks removed:")
print(fruit)
print('\n')

# SORT the fruits and show the list agin sorted this time
fruit.sort()
print("Sorted text to be written:")
print(fruit)
print('\n')

# This is the header for the FOR LOOP which will write and print each line
print("Show the records that are being written:")

#FOR LOOP to write out the sorted fruits file
for item in fruit:
    outfile.write("%s\n" % item)
    print("%s" % item)
infile.close()
outfile.close()
