# CSE467-FINAL-PROJECT
## 1.Introduction
### The purpose of this project is to enhance the model's accuracy in math, coding, future_prediction, planning, and answering common questions by designing an agent.
### This agent uses four functions in this agent:
### 1.ask_multiple_times: ask mutiple times for each essential question and take the most common answer (in this agent is 4)
### 2.translate_to_english: if the question is not in English , translate it to english
### 3.type_check: follow the dev_data domain, classify the question type (math, coding, future_prediction, planning, common_sense)
### 4.agent_loop: based based on the question type, create a loop to answer the question

## 2. Files
### 1. .gitignore - Ignores files
### 2. agent.py - Core agent logic containing all functions
### 3. cse_476_final_project_answers.json - Final answer file for submission
### 4. cse_476_final_project_test_data.json - Test dataset 
### 5. cse476_final_project_dev_data.json - Dev dataset
### 6. final_project_tutorial.ipynb - Project tutorial notebook
### 7. generate_answer_template.py - Generates answer JSON file for output.
### 8. LICENSE - Project license
### 9. README.md - Project documentation including running steps
### 10. setup.py - Setup the project
### 11. evaluator.py - Evaluation tool
### 12. requirments.txt - Dependencies list


## 3. How to run it:
### 1.Use “pip install langdetect”
### 2.Use “python setup.py”
### 3.Use ”python generate_answer_template.py”
### 4.The output file is “cse_476_final_project_answers.json”
