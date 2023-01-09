import speech_recognition as sr
import qsmouth as cm

def takeCommand():
    sp= sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening')
        # seconds of non-speaking audio before
        # a phrase is considered complete
        sp.pause_threshold = 0.7
        audio = sp.listen(source)
        #audio =
        try:
            print("Recognizing")

            Query = sp.recognize_google(audio, language='en')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            cm.speak('say that again sir')
            return "None"
        return Query
