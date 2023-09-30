# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")












































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print): 
    with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer='78 65 89 86 55 91 64 89', expected_print='[78, 65, 89, 86, 55, 91, 64, 89]\nThe highest score in the class is: 91\n')
  
  def test_2(self):
    self.run_test(given_answer='150 142 185 120 171 184 149 199', expected_print='[150, 142, 185, 120, 171, 184, 149, 199]\nThe highest score in the class is: 199\n')

  def test_3(self):
    self.run_test(given_answer='24 59 68', expected_print='[24, 59, 68]\nThe highest score in the class is: 68\n')


print("\n\n\n.\n.\n.")
print('Checking that your code prints a sentence that reads:\n\nThe highest score in the class is: X\n\nwhere X is the largest integer that was entered.')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 

