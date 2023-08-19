import os
import random
import speech_recognition
import pyaudio
import webbrowser
from datetime import datetime
import time
import requests

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
##  Команды для выполнения задач

commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'play_music': ['включить музыку'], 
        'open_browser': ['открой поиск видео','найди видео', 'найди видео'],
        'open_ya': ['найди в интернете','поищи в инетернете', 'найди мне'],
        'time_now': ['сколько время'],
        'shutdown': ['выключить компьютер'],
        'help': ['расскажи что можешь', 'помощь', 'что умеешь'],
        'telegram_open':['открыть телегу', 'телега'] 
        }
}

def time_now():
    current_datetime = datetime.now()
    return current_datetime




def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
        return query
    except speech_recognition.UnknownValueError:
        return ' Не понял говорите'




def greeting():
   
    
    return 'Привет друг! Я помогу тебе управлять компьютером голосом'


def create_task():
   
    print('Что добавим в список дел?')
    query = listen_command()
    with open('todo-list.txt', 'a') as file:
        file.write(f' {query}\n')     
    return f'Задача {query} добавлена в todo-list!'


def play_music():
  
    
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    
    return f'Танцуем под {random_file.split("/")[-1]} 🔊🔊🔊'

def telegram_open():
    webbrowser.open('https://web.telegram.org')
    return "Готово"


def open_browser():
    print("Так так так... Какое видео ищем?")
    query = listen_command()
    webbrowser.open(f'https://www.youtube.com/results?search_query={query}' , new=1)
    return "Готово"

def open_ya():
    print("Что тебе найти?")
    query = listen_command()
    webbrowser.open_new_tab('https://yandex.ru/search/?lr=10735&text='+ query)
    return "Готово"


def shutdown():
    print("Через сколько минут?")
    query = listen_command()
    time.sleep(60*int(query))
    print(f"Сохраняй всё самое важное, выключу компьютер через 5 секунд")
    time.sleep(5)
    os.system("shutdown -s")
    return f"Выключаю"

def help():
    print("1. Записать нужную тебе задачу")
    print("2. Включить песню")
    print("3. Найти видео на ютубе")
    print("4. Поиск в яндексе")
    print("5. Подсказать сколько время")
    print("6. Выключить компьютер")
    return "Пока всё, скоро научусь чему- нибудь ещё..."

def main():
    print("Првиет\n Данная программа поможет управлять вашим помпьютером при помощи голоса\n Скажите помощь, чтобы отобразились все команды.")

    query = ''
    while query != "закрой программу":
        query = listen_command()
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())
    else:
        print("До скорой встречи!")    

if __name__ == '__main__':
    main()