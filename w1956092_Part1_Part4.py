#Part 1 and Part 4

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
dic_progression = {}        
student_id = ""           


#----------Defining function for Part 1 credit inputs----------
def credit_value(message):                                                      #using parameters as message
    while True:                                                                 #creating infinite while loop
        try:                                                                    #try except handling for get valid integer input
            credit = int(input(message))
            if credit < 0 or credit > 120 or credit%20 != 0:                    #using if condition checking Pass credit range
                print("Out of range.")                                          #if condition True printing out of range
                continue                                                        #using continue to restart the loop from begining

        except ValueError:
            print("Integer required")                                           #proper message display for invalid input
            continue
        else:                                                                   #using else block if there is no error
            return credit                                                       #returning the credit value



#----------Defining function for Histogram----------
def histogram(string_outcome,outcome_count):             #using parameters as string_outcome and outcome_count
    print(string_outcome,outcome_count,":",end = " " )   #using end = " " to print next step into the same line
    for i in range(outcome_count):                       #using for loop to print stars for the count
        print("*",end = "")                              #using end = "" to print all starts in same line
    

#----------Defining function for Dictionary----------
def dictionary(string_outcome):                          #using parameters as string_outcome
    dic_progression[student_id] = string_outcome+str(list_create).strip("[]")    #storing the student ID, values into dictionary
    


print("PREDICT PROGRESSION OUTCOMES")    #creating the program

while continue_quit == "y":              #using while loop if the condition is "y" only user needs to continue the program and get the credits of students
    student_id = input("\nEnter the student ID: ")    #student ID input

    if student_id in dic_progression:                                                           #input validation for student ID to check whether student ID already exist
        print("The student ID already exist! Please enter another student ID.")
        continue


    Pass_credit = credit_value("\nEnter your total PASS credits: ")           #calling function and assigning to Pass_credit variable
    Defer_credit = credit_value("Enter your total DEFER credits: ")           #calling function and assigning to Defer_credit variable
    Fail_credit = credit_value("Enter your total FAIL credits: ")             #calling function and assigning to Fail_credit variable

    total = Pass_credit+Defer_credit+Fail_credit                              #get the total of Pass_credit, Defer_credit and Fail_credit
    if total != 120:
        print("Total incorrect.")                                             #total not equal to 120 display total incorrect
        continue                                                              #using continue to restart the loop from begining


    list_create = [Pass_credit,Defer_credit,Fail_credit]             #storing the user entered Pass_credit,Defer_credit and Fail_credit into the list
                
#----------Progression outcome----------
        
    if Pass_credit == 120:                                 #condition for the Progress outcome
        print("Progress")
        count_progress += 1                                #counting the Progress outcomes
        dictionary("Progress - ")                          #Calling the dictionary function with arguments               
        
    elif Pass_credit == 100:                               #condition for the Progress (module trailer) outcome
        print("Progress (module trailer)")                 
        count_trailer += 1                                 #counting the Progress (module trailer) outcomes
        dictionary("Progress (module trailer) - ")         #Calling the dictionary function with arguments          
        
    elif Pass_credit <= 80 and Fail_credit <= 60:          #condition for the Do not progress - module retriever outcome
        print("Module retriever")        
        count_retriever += 1                               #counting the Do not progress - module retriever outcomes
        dictionary("Module retriever - ")                  #Calling the dictionary function with arguments                                                           
        
    else:
        print("Exclude")                                   #else it will print the Exclude outcome
        count_exclude += 1                                 #counting the Exclude outcomes
        dictionary("Exclude - ")                           #Calling the dictionary function with arguments

        
    continue_quit = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")         #get an input to continue or quite the programme
    while continue_quit!= "y" and continue_quit!= "q":                                                                                   #using while loop to get correct input
        print("Invalid option")                                                                                                          #printing Invalid option for wrong input
        continue_quit = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")     

print ("\nProgram was Quited.")    #Printing the Quit message if q entered

#----------Calling the function for Histogram----------
print("-"*100)
print("Histogram")
histogram("Progress",count_progress)         #function call with arguments   
histogram("\nTrailer",count_trailer)
histogram("\nRetriever",count_retriever)
histogram("\nExclude",count_exclude)

outcomes =(count_progress + count_trailer + count_retriever + count_exclude)             #counting the total outcomes
print("\n")
print(outcomes,"outcomes in total.")                                                     #display the total outcomes
print("-"*100)

#----------Part 4 Dictionary----------
print("Part 4: ")
for key,value in dic_progression.items():
    print(key,":",value,end=" ")


print()
print("\nThank you for using PROGRESSION PREDICT PROGRAM")      #display thanks message for using this program


          
            
    


        
            
            
            
            
            

    
