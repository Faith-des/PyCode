import speech_recognition as sr
import wikipedia

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Ask question')
    audio = r.listen (sourse)

try:
    question = r.recognize_google(audio, language="ru-RU")
    print(question)
    answer = wikipedia.summary(question, 2)
    print(answer)
    with open ('conversation.txt','w', encoding='utf8') as f:
        f.write(answer)
except sr.UnknownValueError:
    print("Code did not understand your question")
except sr.RequestError as e:
    print('Error:{0}'.format(e))