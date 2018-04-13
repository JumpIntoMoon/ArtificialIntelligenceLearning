import random
#打招呼
greetings = ['hola', 'hello', 'hi','Hi','hey!','hey','你好','你好！']

nameQuestions = ['你是谁？', '你叫什么名字？']
nameResponses = ['我是Aka，你好呀！',"我的名字叫Aka~~"]

ageQuestions = ['你几岁了？', '你多大啦？']
ageResponses = ['我11岁哦！',"我11岁啦~~"]

byebye =['bye','byebye','再见']

while True:
	userInput = input(">>> ")
	if userInput.lower() in greetings:
		print(random.choice(greetings))
	elif userInput in nameQuestions:
		print(random.choice(nameResponses))
	elif userInput in ageQuestions:
		print(random.choice(ageResponses))
	elif userInput.lower() in byebye:
		print(random.choice(byebye))
		break
	else:
		print("I did not understand what you said, please try something else.")