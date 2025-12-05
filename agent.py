from setup import call_model_chat_completions, MODEL
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