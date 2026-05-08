import random
from pathlib import Path
quiz_folder = Path("quizzes")
quiz_folder.mkdir(exist_ok=True)
capitals={'Maharashtra':'Mumbai','Gujarat':'Gandhinagar','Kerala':'Thiruvananthapuram','Tamil Nadu':'Chennai','Uttar Pradesh':'Lucknow','Madhya Pradesh':'Bhopal','Andhra Pradesh':'Amravati','Goa':'Panaji','West Bengal':'Kolkata','Telangana':'Hyderabad','Uttarakhand':'Dehradun','Assam':'Dispur','Arunachal Pradesh':'Itanagar','Bihar':'Patna','Punjab':'Chandigarh','Chhattisgarh':'Raipur','Jharkhand':'Ranchi','Haryana':'Hissar','Himachal Pradesh':'Shimla','Karnataka':'Bengaluru','Manipur':'Imphal','Mizoram':'Aizawal','Meghalaya':'Shillong','Nagaland':'Kohima','Odisha':'Bhubhaneshwar','Rajasthan':'Jaipur','Sikkim':'Gangtok','Tripura':'Agartala'}
for quiz_num in range(35):
    quiz_file=open(f'capitalsquiz{quiz_num+1}.txt','w',encoding='UTF-8')
    answer_file=open(f'capitalsquiz_answers{quiz_num+1}.txt','w',encoding='UTF-8')
    quiz_file.write('Name:\n\nDate:\n\nPeriod\n\n')
    quiz_file.write((' '*20)+f'State Capitals Quiz (Forms{quiz_num+1})')
    quiz_file.write('\n\n')
    #Shuffle the order of the states
    states=list(capitals.keys())
    random.shuffle(states)
    for num in range(28):
        correct_answer=capitals[states[num]]
        wrong_answers=list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers=random.sample(wrong_answers,3)
        answer_options=wrong_answers+[correct_answer]
        random.shuffle(answer_options)
        quiz_file.write(f'{num+1}. Capital of {states[num]}:\n')
        for i in range(4):
            quiz_file.write(f"{'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        answer_file.write(f"{num+1}.{'ABCD'[answer_options.index(correct_answer)]}\n")

    quiz_file.close()
    answer_file.close()