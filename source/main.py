import recognition 
import voice

def main():

    test = recognition.Recognition()
    vc = voice.Voice()
    mic = voice.Record()
    # name = test.getFromCam()
    # if (name != 'Unknown'):
    #     vc.sayHello(str(name))

    # else:
    #     vc.sayWellcome()

    #mic.startRecord()
    mic.Recognition()
main()
