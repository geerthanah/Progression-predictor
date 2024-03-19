
#Part 1, Part 2 and Part 3

#----------Initializing the variables----------

credit = 0              
Pass_credit = 0         
Defer_credit = 0        
Fail_credit = 0         
continue_quit = "y"     
total = 0               
count_progress = 0      
count_trailer = 0       
count_retriever = 0     
count_exclude = 0       
outcomes = 0            
list_create = []           
list_progress = []      
list_trailer = []       
list_retriever = []      
list_exclude = []       
new = ""                
work = "y"              
option = ""
file = 0
file_r = 0


#----------Defining function for Part 1 credit inputs----------
def credit_value(message):                                                      #using parameters as message
    while True:                                                                 #creating infinite while loop
        try:                                                                    #try except handling for get valid integer input
            credit = int(input(message))                                        
            if credit < 0 or credit > 120 or credit%20 != 0:                    #using if condition checking credit range
                print("Out of range.")                                          #if condition True printing out of range
                continue                                                        #using continue to restart the loop from begining

        except ValueError:
            print("Integer required")                                           #proper message display for invalid input
            continue
        else:                                                                   #using else block if there is no error
            return credit                                                       #returning the credit value
        

#----------Defining function for Part 1 - D. Histogram----------
def histogram(string_outcome,outcome_count):             #using parameters as string_outcome and outcome_count
    print(string_outcome,outcome_count,":",end = " " )   #using end = " " to print next step into the same line
    for i in range(outcome_count):                       #using for loop to print stars for the count
        print("*",end = "")                              #using end = "" to print all starts in same line


#----------Defining function for Part 2 List(extension)----------    
def list_extension(outcome_name,list_name,outcome_count):    #using parameters as outcome_name,list_name and outcome_count
    if outcome_count!=0:                                     #using if condition to execute the next step. Next step only works if the outcome_count not equal to 0
        for c in range(outcome_count):                       #using for loop. variable c for index within the list.
            new = str(list_name[c]).strip("[]")              #converting the index values to string and using strip function to strip []. strip fuction not works for list
            print(outcome_name,"-",new)


#----------Defining fuction for Part 3 Text File(Extension)----------
def file_extension(outcome_name,list_name,outcome_count):      #using parameters as outcome_name,list_name and outcome_count
    if outcome_count!=0:                                       #using if condition to execute the next step. Next step only works if the outcome_count not equal to 0
        for x in range(outcome_count):                         #using for loop. variable x for index within the list.
            file = open('progression_file.txt', 'a')           #a stands for append mode. go to the end of the file and append the content
            new = str(list_name[x]).strip("[]")                #converting the index values to string and using strip function to strip []. strip fuction not works for list
            file.write(outcome_name+" - "+new+"\n")            #writing ti the file
            file.close()                                       #closing the file


        

#----------Creating the program----------

print("PREDICT PROGRESSION OUTCOMES")                       

while True:                                                 #creating infinite while loop
    continue_quit = "y"                                     #Assigning "y" for continue_quit 

    print("\nMenu")                                         #creating a menu for student,staff or exit the program
    print("Option '1' - Student going to predict progression outcome")
    print("Option '2' - Staff member going to predict progression outcomes")
    print("Option '3' - Exit Program")
    option = input("Enter your option number: ")                                      #ask to input the option
    
    if option !="1" and option !="2" and option !="3":
        print("Invalid option")                                                       #proper message display for invalid input
        continue

#-------------------------For student-----------------------------------
    if option=="1":                                                                 #if option 1 students can predict their outcome                                                  
        while work == "y":                                                          #using while loop to grt the credits from students
            
            Pass_credit = credit_value("\nEnter your total PASS credits: ")         #calling function and assigning to Pass_credit variable
            Defer_credit = credit_value("Enter your total DEFER credits: ")         #calling function and assigning to Defer_credit variable
            Fail_credit = credit_value("Enter your total FAIL credits: ")           #calling function and assigning to Fail_credit variable

            total = Pass_credit+Defer_credit+Fail_credit                            #get the total of Pass_credit, Defer_credit and Fail_credit
            if total != 120:
                print("Total incorrect.")                                           #total not equal to 120 display total incorrect
                continue                                                            #using continue to restart the loop from begining


#----------Progression outcome---------------
                
            if Pass_credit == 120:                                 #condition for the Progress outcome
                print("Progress")                                  #print the outcome
                break                                              #break the while work == "y" loop
        
            elif Pass_credit == 100:                               #condition for the Progress (module trailer) outcome
                print("Progress (module trailer)")                 #print the outcome
                break                                              #break the while work == "y" loop
        
            elif Pass_credit <= 80 and Fail_credit <= 60:          #condition for the Do not progress - module retriever outcome
                print("Module retriever")        #print the outcome
                break                                              #break the while work == "y" loop
        
            else:
                print("Exclude")                                   #else it will print the Exclude outcome
                break                                              #break the while work == "y" loop



#------------------------For staff member----------------------------------
    elif option=="2":                                                                  #if option 2 staff member can predict their outcome
        while continue_quit == "y":                                                    #using while loop if the condition is "y" only user needs to continue the program and get the credits
            
            Pass_credit = credit_value("\nEnter your total PASS credits: ")            #calling function and assigning to Pass_credit variable
            Defer_credit = credit_value("Enter your total DEFER credits: ")            #calling function and assigning to Defer_credit variable
            Fail_credit = credit_value("Enter your total FAIL credits: ")              #calling function and assigning to Fail_credit variable

            total = Pass_credit+Defer_credit+Fail_credit
            if total != 120:
                print("Total incorrect.")                                              #total not equal to 120 display total incorrect
                continue

            
            list_create = [Pass_credit,Defer_credit,Fail_credit]             #storing the user entered Pass_credit,Defer_credit and Fail_credit into the list
                        
#----------Progression outcome----------
                
            if Pass_credit == 120:                                 #condition for the Progress outcome
                print("Progress")                                  #print the outcome
                count_progress += 1                                #counting the Progress outcomes
                list_progress.append(list_create)                  #appending the list_create list into the list_progress list
                
            elif Pass_credit == 100:                               #condition for the Progress (module trailer) outcome
                print("Progress (module trailer)")                 
                count_trailer += 1                                 #counting the Progress (module trailer) outcomes
                list_trailer.append(list_create)                   #appending the list_create list into the list_trailer list
                
            elif Pass_credit <= 80 and Fail_credit <= 60:          #condition for the Do not progress - module retriever outcome
                print("Module retriever")        
                count_retriever += 1                               #counting the Do not progress - module retriever outcomes
                list_retriever.append(list_create)                 #appending the list_create list into the list_retriever list
                
            else:
                print("Exclude")                                   #else it will print the Exclude outcome
                count_exclude += 1                                 #counting the Exclude outcomes
                list_exclude.append(list_create)                   #appending the list_create list into the list_exclude list

                
            continue_quit = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")         #get an input to continue or quite the programme
            while continue_quit!= "y" and continue_quit!= "q":                                                                                   #using while loop to get correct input
                print("Invalid option")                                                                                                          #proper message display for invalid input
                continue_quit = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")     

        print ("\nProgram was Quited.\n")    #Printing the Quit message if q entered

#----------Call the function for Histogram----------
        print("-"*100)
        print("Histogram")
        histogram("Progress",count_progress)         #function call with arguments
        histogram("\nTrailer",count_trailer)
        histogram("\nRetriever",count_retriever)
        histogram("\nExclude",count_exclude)

        outcomes =(count_progress + count_trailer + count_retriever + count_exclude)    #counting the total outcomes
        print("\n")
        print(outcomes,"outcomes in total.")                                            #display the total outcomes
        print("-"*100)


#----------Part 2 - Call the function for List(extension)----------
        print("\nPart 2: ")
        list_extension("Progress",list_progress,count_progress)                    #function call with arguments
        list_extension("Progress (module trailer)",list_trailer,count_trailer)
        list_extension("Module retriever",list_retriever,count_retriever)
        list_extension("Exclude",list_exclude,count_exclude)


#----------Part 3 - Text File(extension)----------
        file = open('progression_file.txt', 'w')   #opening the file in write mode and overwrite to it
        file.write("Part 3: \n")                   #write into the file
        file.close()                               #close the file

#----------Call the function for Part 3----------
        file_extension("Progress",list_progress,count_progress)                  #function call with arguments
        file_extension("Progress (module trailer)",list_trailer,count_trailer)
        file_extension("Module retriever",list_retriever,count_retriever)
        file_extension("Exclude",list_exclude,count_exclude)



#----------Part 3 - Access the stored data and print----------
        print("-"*100)

        try:
            file_r = open('progression_file.txt', 'r')               #open the file in read mode
            for line in file_r:                                      #uding for loop to print the stored data
                print(line,end="")

            file_r.close()                                           #close the file

        except FileNotFoundError:
            print("File not found please check the file")

        

    elif option =="3":                                                #option 3 for exit
        print("Thank you for using PROGRESSION PREDICT PROGRAM")      #display thanks message for using this program
        break                                                         #get out from while True loop

        

            
    


        
            
            
            
            
            

    
