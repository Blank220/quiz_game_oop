import random
import time
import winsound
  
#open the quiz file and read it
with open('quiz.txt', 'r') as file:
   lines = file.readlines()

#Introduction to the Game
print('WELCOME TO QUIZ LEGENDS!'.center(80))
time.sleep(2)
print('Get Ready To Answer The Ultimate Quiz!'.center(80))
time.sleep(1)
print('Loading......'.center(80))
time.sleep(2)

#formatting of the questions/choices
questions = []
i = 0
while i < len(lines):
   if lines[i].startswith('#QUESTIONS'):
      q = lines[i + 1].strip()
      a = lines[i + 3].strip()
      b = lines[i + 4].strip()
      c = lines[i + 5].strip()
      d = lines[i + 6].strip()
      correct = lines[i + 7].strip()[-1]
      questions.append((q,a,b,c,d,correct))
      i += 9
   else:
      i += 1
#choosing random questions
random.shuffle(questions)

#tracking of scores
score = 0

#printing the question and choices
for q in questions:
   print('\n' + q[0])
   print(q[1])
   print(q[2])
   print(q[3])
   print(q[4])

#checks if answer is right
   ans = input('What\'s your answer? (a/b/c/d) or "x" to exit: ').lower()
   if ans == 'x':
         print('Exiting program....Byeeee!')
         time.sleep(2)
         break
   
   while ans not in ['a','b','c','d',"x"]:
      print('Invalid answer,please refer to the choices')
      ans = input('What\'s your answer? (a/b/c/d or "x" to exit):'.lower())

      if ans == 'x':
         print('Exiting program....Byeeee!')
         time.sleep(2)
         break
   if ans == 'x':
      break

   if ans == q[5]:
      print('Checking answer...')
      time.sleep(1)
      print('✅ Correct!')
      winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
      score += 1
   else:
      print('Checking answer...')
      time.sleep(1)
      print(f'❌ Wrong! The correct answer is {q[5]}')
      winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
      
#Final Score
if score == 0:
   print(f'Wala Kang Tinama Kahit Isa, Mag Review Ka Pa! {score} out of {len(questions)}')
elif score == len(questions):
   print(f'Wow, Sanaol Perpek {score} out of {len(questions)}')
else:
   print(f'Finished! You Did A Wonderful Job! \nYou got {score} out of {len(questions)}')
