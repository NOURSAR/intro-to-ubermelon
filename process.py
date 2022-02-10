log_file = open("um-server-01.txt") #open a file containing the data we need


def sales_reports(log_file): #defining the function with the parameter(file in this case)
    for line in log_file: # for loop to reed from the first line in the file
        line = line.rstrip() #defining what is the line in the file
        #rstrip removes the characters at the end of the line such as the space 
        day = line[0:3] # in the line to read the first 4 characters (day)
        if day == "Mon": #if condition: if the day equals "Mon" then 
            print(line) #if condition is met print the line


sales_reports(log_file) #calling the function
