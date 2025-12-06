from setup import call_model_chat_completions, MODEL
from langdetect import detect
#function 1: ask mutiple times for each question and take the most common answer
def ask_multiple_times(prompt: str) -> str:
    choices = []
    for _ in range(4):
         response = call_model_chat_completions(prompt, temperature = 0.8)
         if response["ok"]:
            choices.append(response["text"].strip())
    if not choices:
        return ""
    
    count_showup = {}
    for choice in choices:
        if choice in count_showup:
            count_showup[choice] += 1
        else:
            count_showup[choice] = 1
    
    most_com_ans = ""
    max = 0
    for a, count in count_showup.items():
        if count > max:
            max = count
            most_com_ans = a
         
    return most_com_ans

#function 2: if the question is not in English , translate it to English first
def is_english(prompt: str) -> bool:
    try:
        if detect(prompt) =="en":
            return True
        else:
            return False
    except:
        return False
    
def translate_to_english(prompt: str) -> str:
    if is_english(prompt):
        return prompt
    system_prompt = " You are one of the best translator in the world. Translate the quetions into English accurately but keep the original meaning if the question is not written in English."
    response = call_model_chat_completions(prompt,temperature = 0.2,system = system_prompt)
    if response["ok"]:
        return response["text"].strip()
    else:
        return prompt 

#function 3: follow the dev domain, classify the question type
# math , coding, future_prediction, planning, common_sense
def type_check(prompt: str) -> str:
    system_prompt = "You are a great classifier. To better answer the user's question, you must classify the question into one of the following five categories:'math','coding','future_prediction','planning',or 'common_sense'. Reply with the category name only, does not need to explain, keep simple and accurate."
    response = call_model_chat_completions(prompt,system = system_prompt)
    if response["ok"]:
        type = response["text"].strip()
        if type in ["math", "coding", "future_prediction", "planning", "common_sense"]:
            return type
        else:
            return "common_sense"
    else:
        return "common_sense"

#function 4: based on the question type, create an agent_loop to answer the question
# math and coding need translate to English first
# math, future_prediction, planning need to ask multiple times
def agent_loop(prompt: str) -> str:
    type = type_check(prompt)
    if type in ["math", "coding"]:
        prompt = translate_to_english(prompt)
    else:
        prompt = prompt
    if type =="math":
        train = "You are a great math tutor. Separate the math problem into small steps. MUST DO NOT SHOW THE STEPS IN THE OUTPUT. Reply with the final answer with number only, do not include any explanation."
        combine_prompt = f"{train}\n{prompt}"
        result = ask_multiple_times(combine_prompt)
        return result
    elif type =="coding":
        system_prompt = "You are a high level software engineer. Write the code simple and efficient based on the requirements. Reply with the final code only, do not include any explanation."
        response = call_model_chat_completions(prompt, temperature = 0.2,system = system_prompt)
        if response["ok"]:
            return response["text"].strip()
        else:
            return ""
    elif type =="future_prediction":
        train = "You are a perfect assistant in futrue analysis. Accoring to the information given and you known, make the most realiable choice. Reply with the final answer only, do not include any explanation."
        combine_prompt = f"{train}\n{prompt}"
        result = ask_multiple_times(combine_prompt)
        return result
    elif type =="planning":
        train = "You are a great planner who always make a perfect plan. Make a detailed plan based on the requirements. Reply with the final plan only, do not include any explanation."
        combine_prompt = f"{train}\n{prompt}"
        result = ask_multiple_times(combine_prompt)
        return result
    elif type =="common_sense":
        response = call_model_chat_completions(prompt)
        if response["ok"]:
            return response["text"].strip()
        else:
            return ""