from setup import call_model_chat_completions, MODEL
#function 1: ask mutiple times for each question and take the most common answer
def ask_multiple_times(prompt: str) -> str:
    choices = []
    for _ in range(3):
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
def translate_to_english(prompt: str) -> str:
    system_prompt = " You are one of the best translator in the world. Translate the quetions into English accurately but keep the original meaning if the question is not written in English."
    response = call_model_chat_completions(prompt,temperature = 0.3,system = system_prompt)
    if response["ok"]:
        return response["text"].strip()
    else:
        return prompt 

#function 3: follow the dev domain, classify the question type
# math , coding, furture_prediction, planning, common_sense
def type_check(prompt: str) -> str:
    system_prompt = "You are a great classifier. To better answer the user's question, you must classify the question into one of the following five categories:'math','coding','future_prediction','planning',or 'common_sense'. Reply with the category name only, does not need to explain, keep simple and accurate."
    response = call_model_chat_completions(prompt,system = system_prompt)
    if response["ok"]:
        type = response["text"].strip()
        if type in ["math", "coding", "furture_prediction", "planning", "common_sense"]:
            return type
        else:
            return "others"
    else:
        return "others"