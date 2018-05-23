import recognition 
import voice

def main():

    test = recognition.Recognition()
    audio = voice.Voice()
    
    name = test.getFromCam()
    if (name != 'Unknown'):
        audio.sayHello(str(name))

    else:
        audio.sayWellcome()

main()
