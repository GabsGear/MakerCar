import recognition 
import voice

def main():

    test = recognition.Recognition()
    vc = voice.Voice()
    name = test.getFromCam()
    if (name != 'Unknown'):
        vc.sayHello(str(name))

    else:
          test.RegisterNewPerson()
main()
