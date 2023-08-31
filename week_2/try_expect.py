import requests


question = input("Enter your question for the magic 8 ball: ")

magic_8_ball =  f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'



try:
    response = requests.get(magic_8_ball).json()
    answer = response['magic']['answer']
    print(f" the magic 8 balls says: {answer}")
except Exception as e:
    print("I'm not sure what is going on but I can't tell you the answer to your question")
    print(e)
    