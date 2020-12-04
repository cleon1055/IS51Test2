
"""
Standard-English:

This program will display the number of total grades, avergage grade, and percentage
of those grades above the average test score of a final. 
The test scores for the final are stored in a file called final.txt, which we will open and use
for the program. 

We first read the grades in the in text file final.txt. 
Then from the final.txt file, we assign the grades to a list of integers.  
Once the text file has been read into memory we close the final.txt file. 

We then create a funtion to add the grades in the text file into a list and calculate the total
number of grades based on the length of the list and display it.
Next we create a function to calculate the average grade based of the grade list and displat it.
Once we have the average, we create another function to calculate the percent of grades higher 
than the class average and display it. 

To finsh, we display the total number of grades, grade average and percent of grades that are 
are higher than the average to the user. 

"""

"""
Pseudocode

main ():


    gradelist = []

    total number of grades = lenth of lines in final.txt
    append.each line in txt file to list1

grade_list():
    Read in final.txt file
    create list = each line from file
    close file
    create a grade_list
    return the grade_list

def cal_average(total):
    result = sum of all grades in gradelist / number of grades in gradelist 
    return result

def Percentages_past_avergage(result):
    percentage = (grades > average)/total number of grades * 100 
    return percentage


Number of grades = number of grades in list one (len.lis1)
Average grade = cal_avergae(total)
Percentage of grades above average= Percentages_past_Average

main()

"""

def main ():


    gradelist = []

    total_grades = len[final.txt]
    gradelist.append(float(number))

def total_grades():
    infile = open(txt_file)
    numbers = [number for number in infile]
    infile.close()
    gradelist = []
    return total_grades 

def cal_average(total_grades): 
    result = sum(gradelist) / total_grades   
    return result

def Percentages_past_average(result):
    percentage = (grades > cal_average)/total * 100 
    return percentage


Number of grades = total_grades():
Average grade = cal_avergae(total): 
Percentage of grades above average = Percentages_past_average

print("Number of grades:", total_grades)
print("Averge Grade:", cal_average)
print("Percentage of grades above average:", Percentages_past_average) 

main()
