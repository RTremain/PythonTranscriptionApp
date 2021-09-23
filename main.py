import speech_recognition

recognizer = speech_recognition.Recognizer()

f = open("transcription.txt", "w")

while True:
    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            f = open("transcription.txt", "a")
            if text == "quit":
                print("Quitting")
                f.write("---EoF---")
                f.close()
                break
            f.write(text + "\n")
            f.close()
            print(f"Recognized {text}")


    except speech_recognition.UnknownValueError as e:
        print(f"Error: {e}")
        recognizer = speech_recognition.Recognizer()
        continue
