# This is the easy quiz question about variables and strings:
easy_quiz = '''A ___1___ is something that holds a ___2___ that may change. It is important in programming because it makes coding easier 
to write so we are not repeating ___2___s.  A ___3___ is a list of characters in order.  We can assign a ___2___ to a ___1___ by using the  = ___4___ .  
When we combine more than one ___3___ together using the + ___4___, we ___5___ them.'''

# Here is the medium quiz about functions:
medium_quiz = '''def is a kind of ___1___.  A ___1___ takes an input and ___2___s an output.  The inputs for the ___1___ are in parenthesis and are called ___3___.
When you use your ___1___ to produce an output, you are ___4___ the ___1___.  To do this you must  end the ___1___ with a ___2___ statement.  
To see the result of your function, you must use the ___5___ ___1___.'''


# Here is the hard quiz question which is about loops:
hard_quiz ='''When we use functions to make comparisons they return a ___1___ value of either True or False.  To run blocks of code multiple times we use a ___2___. 
 A ___2___ which runs code until a condition is met uses the  ___3___ expression.  We use a ___4___  to stop a ___3___ ___2___ when certain conditions are met.  An ___5___ ___2___ occurs when the test condition 
 never reports false and the program keeps running.'''

#Here is the final quiz that asks questions about lists:
hardest_quiz = '''A ___1___ is sequences of anything.  We can have a ___1___ of numbers, characters or even a ___1___ of ___1___s.  It is called ___2___ when more than one ___3___
 refers to the same object - then a change to that object changes the value of each ___3___.  We use the ___4___ operation to add an element to the end of a ___1___ 
 and mutate the ___1___. To iterate through the elements of a ___1___, it is often easier to use a ___5___ loop rather than a while loop.'''

# Here is a list of the answers for each level of the quiz:
easy_quiz_answers = ['variable', 'value', 'string', 'opperand', 'concatenate']
medium_quiz_answers = ['function', 'return', 'parameters', 'calling', 'print']
hard_quiz_answers = ['Boolean', 'loop', 'while', 'break', 'infinite']
hardest_quiz_answers = ['list', 'aliasing', 'variable', 'append', 'for' ]

# This is the list of blanks that are in each quiz which will be replaced by the user's input.
insert_answer = ['___1___', '___2___', '___3___', '___4___', '___5___']
 

closing = ("Thank you for playing this quiz.  I hope you had fun.")

# This function takes the level set by the user and returns the correct quiz.
def choose_quiz_level (user_level):  
    if user_level == 'easy':
        return easy_quiz 
    if user_level == 'medium':
        return medium_quiz 
    if user_level == 'hard':
        return hard_quiz 
    if user_level == 'hardest':
        return hardest_quiz
    if user_level == 'quit':
        return closing 

# this function tkes the the quiz level set by the user input and returns the correct set of answers.
def select_answers (user_level):
    if choose_quiz_level (user_level) == easy_quiz:
        return easy_quiz_answers
    if choose_quiz_level(user_level) == medium_quiz:
        return medium_quiz_answers
    if choose_quiz_level (user_level) == hard_quiz:
        return hard_quiz_answers
    if choose_quiz_level (user_level) == hardest_quiz:
        return hardest_quiz_answers



# This is the quiz function that takes the quiz text and answers based on the quiz level selected by the user, and obtains the user input for each blank.  
#If the user answer is correct, it adds it to the quiz text and prompts for the next blank.  
#If the user provides the wrong answer, they are told it is incorrect and asked to again enter the answer.
#Once a quiz level is completed, the user is promoted to choose a new quiz level and play again, or to quit.

def play_quiz():   
    user_level = raw_input ("Please choose level: easy, medium, hard, hardest or quit if you no longer wish to play: ")
    quiz_text = choose_quiz_level (user_level)
    answers = select_answers (user_level)
    
    while user_level != 'quit':
        print quiz_text
        index = 0
        while index < len (insert_answer):
            user_input = raw_input("What is the correct answer for " + insert_answer[index] + "? ")      
            if user_input != answers[index]:
                user_input = raw_input ("That is not correct.  Please try again" + insert_answer[index] + " ")                
            if user_input == answers[index]:
                print "That is the correct answer."
                quiz_text=quiz_text.replace(insert_answer[index], user_input)
                print quiz_text
                index = index + 1
        user_level = raw_input ("You have successfully completed this quiz.  You can play another quiz by choosing another level.  Please choose: easy, medium, hard, hardest, or quit if you no longer wish to play:")  
        quiz_text = choose_quiz_level (user_level)
        answers = select_answers (user_level)
    return closing
        

print play_quiz() 