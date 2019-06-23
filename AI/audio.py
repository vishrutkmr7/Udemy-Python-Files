# pyaudio not installed...
import pyglet, pyaudio, wave, subprocess, speech_recognition as sr
from commands import Commander


# file = pyglet.resource.media('audio/to-the-point.mp3')
# file.play()
#
# pyglet.app.run()

running = True

def say(text):
    subprocess.call('say ' + text, shell=True)

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
cmd = Commander()

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
    if command in ['quit', 'exit', 'bye', 'goodbye', 'stop']:
        global running
        running = False

    # say('You said: ' + command)
    cmd.discover(command)


while running == True:
    initSpeech()
