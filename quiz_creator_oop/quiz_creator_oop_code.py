import time

class QuizBase:
    def __init__(self):
        self.counter = 0        #marks how many question is saved
    
    def greet(self):
        print('WELCOME TO QUIZ LEGENDS!'.center(80))
        time.sleep(2)
        print('Get Ready To Create The Ultimate Quiz!'.center(80))
        time.sleep(1)
        print('Loading......'.center(80))
        time.sleep(2)

class Quiz(QuizBase):
    def run(self):
        self.greet()

#ask user for a question or give them the choice to exit
        while True:
            question = input('Enter A Question Of Your Choice Or Type "x" To Stop: *')
            if question.lower() == 'x':
                print('Thank You For Using Quiz Legends \nHave A Great Day!')
                break

            print('Now, What Are The Possible Answers? ')
            #ask the user for the choices/possible answers in the question (a-d)
            option_a = input('Option A. ')
            option_b = input('Option B. ')
            option_c = input('Option C. ')
            option_d = input('Option D. ')
            options = ['a', 'b', 'c', 'd']

            #ask the user the correct answer and checks if it is in the choices given
            while True:
                correct_option = input('What option is the correct answer? (a/b/c/d): ').lower()
                if correct_option in options:  
                    print(f'Nice! So The Right Answer is {correct_option}! ')
                    break
                print('Error! Answer Given Is Not On The Choices!')

            #saves the question and answer to a text file
            with open('quiz.txt', 'a') as file:
                file.write('#QUESTIONS\n' + question + '\n')
                file.write('#OPTIONS\n')
                file.write('a) ' + option_a + '\n')
                file.write('b) ' + option_b + '\n')
                file.write('c) ' + option_c + '\n')
                file.write('d) ' + option_d + '\n')
                file.write('#ANSWER ' + correct_option + '\n')
                file.write('Moving on...\n')
            print('Saving Question.....')
            time.sleep(2)
            self.counter += 1
            print(f'.....Question Saved Successfully \n You\'ve added {self.counter} Questions')
            
