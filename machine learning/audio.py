# pyaudio not installed...
import pyglet, pyaudio, wave, speech_recognition as sr


# file = pyglet.resource.media('audio/to-the-point.mp3')
# file.play()
#
# pyglet.app.run()

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()

def initSpeech():
    print("Listening...")

    play_audio("/audio/forcestrong.wav")

    with sr.Microphone() as source:
        print("Say Something..")
        audio = r.listen(source)

    play_audio("/audio/beatlesmail.wav")
    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't get ya!")

    print("Your command:", command)


initSpeech()
