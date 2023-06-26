import speech_recognition as sr
recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    command = recognizer.recognize_google(audio)
    print(command)
