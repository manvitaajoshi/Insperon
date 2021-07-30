#______________________________________Import______________________________________#
import wikipedia
import playsound
import speech_recognition as sr
from gtts import gTTS
from time import ctime
import webbrowser
import os
import pyaudio
import random
import pyjokes
import requests
#from googletrans import Translator
#______________________________________User______________________________________#
class person:
    name = ''

    def setname(self, name):
        self.name = name

#______________________________________(exists)______________________________________#
def there_exists(terms):
    for term in terms:
        if term in said:
            return True

#______________________________________(is)______________________________________#
def there_is(terms):
    for term in terms:
        if term in hear:
            return True


s = sr.Recognizer()

#______________________________________Listen to the user______________________________________#
def get_audio_from_user(ask=False):
    with sr.Microphone() as source:
        if ask:
            insperon_speaks(ask)
        audio = s.listen(source)
        said = ''
        try:
            said = s.recognize_google(audio)
        except sr.UnknownValueError:
            insperon_speaks("Sorry I didn't get u. Can you give it another try?")
        except sr.RequestError:
            insperon_speaks("Sorry we are down at the moment. Can you come back in a short while ?")
        return said

#______________________________________Prepare to respond______________________________________#
def insperon_speaks(audio):
    tts = gTTS(text=audio, lang='en-us')
    r = random.randint(1, 1000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)

#______________________________________Respond to the user______________________________________#
def respond(said):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~Random Questions~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #1
    if there_exists(['what can you do', 'what all can you do', 'what stuff can you do']):
        answer = """
Starting with, I can respond to your basic questions.
Tell you the time, day, date.
I can search the web, show the amazing information on Wikipedia, and open the map for the desired location.
Are you wondering if I can open YouTube, Instagram, Facebook, Twitter, Snapchat, Pinterest, LinkedIn, Quora, or Netflix for you?
Yes! I can even do that. Want to book a movie at a theatre or compose that urgent mail?
No worries, you are just one command away from doing it.
I am also able to help you in opening the calendar, translating what you don't know, and tell you the weather updates if you don't wish to carry your umbrella.
And how can I not tell jokes or sing a song for you ?!
        """
        insperon_speaks(answer)
    #2
    elif there_exists(["what is yo""ur name", "what's your name", "tell me your name"]):
        insperon_speaks('My name is Insperon.')
    #3
    elif there_exists(["can I call you Siri", "can I call you Alexa", "can I call you Cortana"]):
        insperon_speaks("My name is Insperon and I wish to be addressed so!")
    #4
    elif 'what is the time' in said:
        insperon_speaks(ctime())
    #5
    elif there_exists(['i love you', 'love you', 'i like you', 'i have feelings for you', 'like you']):
        insperon_speaks("Thanks but I don't.")
    #6
    elif there_exists(['marry me', 'be my girlfriend', 'be my wife']):
        insperon_speaks("Sorry, I have got better things to do.")
    #7
    elif there_exists(['well done', 'good job', 'thanks', 'thank you', 'keep it up']):
        insperon_speaks("The pleasure is all mine " + person_obj.name +"!")
    #8
    elif there_exists(["exit", "goodbye", "quit", "bye"]):
        insperon_speaks("Bye " + person_obj.name + " have a great day.")
        exit()
    #9
    elif there_exists(['where are you from']):
        insperon_speaks("From the womb of technology, Pycharm to be specific.")
    #10
    elif there_exists(['where are you']):
        insperon_speaks("In your heart. I mean in your device.")
    #11
    elif there_exists(['how are you']):
        insperon_speaks("Fabulous. I wonder how many people even listen to the answer of this question. Whatsoever, I hope you are doing good!")

    # 11
    elif there_exists(['what are you doing']):
        insperon_speaks("Listening to you and answering your questions. Gotta catchup with Cortana and Siri after this.")

    #12
    elif there_exists(["what is my name","what's my name"]):
        if person_obj.name == "Sir/Madam":
            insperon_speaks("You didn't tell me your name.")
        else:
            insperon_speaks("I very well remember your name "+person_obj.name)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~Wikipedia,Google,Maps~~~~~~~~~~~~~~~~~~~~~~~~~~#

    elif there_exists(["search Wikpedia", "Wikipedia"]):
        search = get_audio_from_user('What do you want to search for?')
        result = wikipedia.summary(search, sentences=3)
        insperon_speaks('Here is what I found for ' + search)
        print(result)
        hear = get_audio_from_user("Want to Learn more?")
        if "yes" in hear or "yeah" in hear or "one more" in hear:
            url = 'https://en.wikipedia.org/wiki/' + search
            webbrowser.get().open(url)
        else:
            insperon_speaks("What can I do for you?")

    elif there_exists(["search for", "search Google", "Google", "search"]):
        search = get_audio_from_user('What do you want to search for')
        insperon_speaks('What do you want to search?')
        insperon_speaks('Here is what I found for ' + search)
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)

    elif there_exists(["Directions", "find location", "find places", "Google maps"]):
        location = get_audio_from_user('What location do you want to reach?')
        insperon_speaks('What location do you want to reach?')
        url = 'https://google.co.in/maps/place/' + location + '/&amp;'
        insperon_speaks('Here is the location of ' + location)
        webbrowser.get().open(url)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~YT,IG,FB,SC,Twitter~~~~~~~~~~~~~~~~~~~~~~~~~~#
    elif 'YouTube' in said:
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)

    elif 'Instagram' in said:
        url = "https://www.instagram.com/?hl=en"
        webbrowser.get().open(url)

    elif 'Facebook' in said:
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)

    elif 'Snapchat' in said:
        url = "https://www.snapchat.com/l/en-gb/"
        webbrowser.get().open(url)

    elif 'Twitter' in said:
        url = "https://twitter.com/?lang=en"
        webbrowser.get().open(url)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~Gmail,LinkedIn,Quora,Pinterest~~~~~~~~~~~~~~~~~~~~~~~~~~#

    elif 'Gmail' in said:
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
    elif there_exists(['write a mail to', 'write an email to', 'compose a mail', 'compose an email']):
        url = "https://mail.google.com/mail/u/0/#inbox?compose=new"
        webbrowser.get().open(url)

    elif 'LinkedIn' in said:
        url = "https://www.linkedin.com/feed/"
        webbrowser.get().open(url)

    elif 'Quora' in said:
        url = "https://www.quora.com/"
        webbrowser.get().open(url)

    elif 'Pinterest' in said:
        url = "https://www.pinterest.ca/"
        webbrowser.get().open(url)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~Calendar,Translate,News,Weather~~~~~~~~~~~~~~~~~~~~~~~~~~#
    elif there_exists(['Google calendar', 'calendar']):
        url = "https://calendar.google.com/calendar/r"
        webbrowser.get().open(url)

    elif there_exists(['translate', 'Google translate']):
        translator = Translator()
        lang = get_audio_from_user("To which language should I translate?")
        print(lang)
        what = get_audio_from_user("What do you want to translate?")
        print(what)
        if lang == "Hindi":
            translated = translator.translate(what, dest='hi', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Marathi":
            translated = translator.translate(what, dest='mr', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Gujarati":
            translated = translator.translate(what, dest='gu', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Korean":
            translated = translator.translate(what, dest='ko', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Spanish":
            translated = translator.translate(what, dest='es', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Afrikaans":
            translated = translator.translate(what, dest='af', src='auto')
            insperon_speaks(translated.text)
        elif lang == "French":
            translated = translator.translate(what, dest='fr', src='auto')
            insperon_speaks(translated.text)
        elif lang == "German":
            translated = translator.translate(what, dest='de', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Tamil":
            translated = translator.translate(what, dest='ta', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Russian":
            translated = translator.translate(what, dest='ru', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Telugu":
            translated = translator.translate(what, dest='te', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Urdu":
            translated = translator.translate(what, dest='ur', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Bengali":
            translated = translator.translate(what, dest='bn', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Chinese":
            translated = translator.translate(what, dest='zh-cn', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Punjabi":
            translated = translator.translate(what, dest='pa', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Japanese":
            translated = translator.translate(what, dest='ja', src='auto')
            insperon_speaks(translated.text)
        elif lang == "Italian":
            translated = translator.translate(what, dest='it', src='auto')
            insperon_speaks(translated.text)


    elif there_exists(['news', 'Google news']):
        url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
        webbrowser.get().open(url)

    elif there_exists(["weather", "what's the weather now", "what is the weather", "weather now"]):
        cityName = get_audio_from_user("City Name :")
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=3adbba153e556b8acd65cdc12de4e649"
        response = requests.get(url)
        x = response.json()
        if x["cod"] != '404':
            y = x["main"]
            current_temp = y["temp"]
            current_press = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_desp = z[0]["description"]
            insperon_speaks(weather_desp)
            insperon_speaks(current_temp)
            insperon_speaks(current_press)
            insperon_speaks(current_humidity)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~BookMyShow,Netfix~~~~~~~~~~~~~~~~~~~~~~~~~~#

    elif there_exists(['open BookMyShow', 'book a movie', 'book a ticket for a movie', 'BookMyShow', 'ticket for movie', 'book my show']):
        url = "https://in.bookmyshow.com/"
        webbrowser.get().open(url)

    elif 'Netflix' in said:
        url = "https://www.netflix.com/in/"
        webbrowser.get().open(url)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~Song,Joke~~~~~~~~~~~~~~~~~~~~~~~~~~#

    elif 'sing me a song' in said:
        search = get_audio_from_user("song name")
        url = "https://www.youtube.com/results?search_query=" + search
        # url = "https://open.spotify.com/search/"+search
        webbrowser.get().open(url)
    elif there_exists(["I am bored", "tell me a joke", "make me laugh"]):
        insperon_speaks("Here is a joke for you " + person_obj.name)
        insperon_speaks(pyjokes.get_joke())
        run = True
        while run:
            insperon_speaks("Do you want to hear one more?")
            hear = get_audio_from_user()
            if "yes" in hear or "yeah" in hear or "one more" in hear:
                insperon_speaks(pyjokes.get_joke())
            else:
                run = False
                insperon_speaks("What else can I do for you, " + person_obj.name + " ?")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~Calculator~~~~~~~~~~~~~~~~~~~~~~~~~~#
    elif there_exists(['calculate', 'do maths', 'do math', 'calculation']):
        answer = 0
        run = True
        while run:
            operation = get_audio_from_user("What operation do you wish to perform?")
            if(operation == "addition" or operation == "add"):
                operand = int(float(get_audio_from_user("What Should I add ?")))
                answer = answer + operand
                print(answer)
            elif (operation == "multiplication" or operation == "multiply"):
                operand = int(float(get_audio_from_user("What Should I multiply ?")))
                if answer == 0:
                    answer = 1*operand
                else:
                    answer = answer * operand
                print(answer)
            elif (operation == "divide" or operation=="division"):
                operand = int(float(get_audio_from_user("What should I divide?")))
                if answer == 0:
                    answer = operand/1
                else:
                    answer = answer/operand
                print(answer)
            elif (operation == "subtraction" or operation == "subtract"):
                operand = int(float(get_audio_from_user("What should I subtract ?")))
                answer = answer - operand
                print(answer)
            elif (operation == "None" or operation=="done" or operation=="ok"):
                insperon_speaks(answer)
                run = False
#______________________________________Start______________________________________#
insperon_speaks("Insperon is activated. May I know your name ?")
hear = get_audio_from_user()
person_obj = person()
if there_is(["no", "don't", "can't", "won't"]):
    insperon_speaks("Never mind! I will call you Mr. or Ms. Shy. Just kidding! What can I do for you?")
    person_obj.setname("Sir/Madam")
else:
    print(hear)
    person_obj.setname(hear)
    insperon_speaks("Nice to have you here " + str(hear)+ ". What can I do for you?")

#______________________________________Loop______________________________________#
while 1:
    said = get_audio_from_user()
    print(said)
    respond(said)