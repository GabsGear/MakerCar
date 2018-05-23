
# pylint: disable=E1101
import face_recognition
from datetime import datetime
import cv2
import voice as vc


class Recognition(vc.Voice):

    def chamadaMoodle(self, nome):
        print('Fazendo a chamada no moodle: ' + str(nome))


    def getFromCam(self):
        # Get a reference to webcam #0 (the default one)

        video_capture = cv2.VideoCapture(1)

        gabs_image = face_recognition.load_image_file("/home/gabs/reconhecimento facial/photos/obama.jpg")
        gabs_face_encoding = face_recognition.face_encodings(gabs_image)[0]

        # gabs_image = face_recognition.load_image_file("gabs.jpg")
        # gabs_face_encoding = face_recognition.face_encodings(gabs_image)[0]

        # Create arrays of known face encodings and their names
        known_face_encodings = [
            gabs_face_encoding
        ]
        known_face_names = [
            "Gabs"
        ]

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        process = 0
        confirm = 0
        horario = 'unkdown'
        while process <= 5:
            # Grab a single frame of video
            ret, frame = video_capture.read(0)

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    start=datetime.strptime('16:00','%H:%M')
                    end = datetime.strptime('18:00','%H:%M')

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                        dnow=datetime.now() 
                        if(dnow.time() > start.time() and dnow.time() < end.time()):
                            print('Alguem entrou na sala')
                            horario = 'aula'


                    face_names.append(name)
                    confirm += 1
                    process += 1

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

        if(confirm < 5):
            print('Nao foi possivel reconhecer o aluno')

        else:
            print('\n\n\nAluno reconhecido entrou na sala confirmações ' + str(confirm) + ' de ' + str(process))    
            print('Nome: ' + str(name))
            print('Horario: ' + str(datetime.now()))

            if(horario == 'aula'):
                print('Horario de aula, fazendo a chamada')
                self.chamadaMoodle(str(name))
            
            process_this_frame = not process_this_frame

        return name

    def takeShot(self):
        cap = cv2.VideoCapture(1)

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

        input('Press Enter to take a shot')
        return_value, image = cap.read()
        cv2.imwrite('/home/gabs/reconhecimento facial/photos/photo.png', image)

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def RegisterNewPerson(self):
        self.sayWellcome()
        self.startRecord() #get name
        self.sayPhoto() #avisar que vai tirar uma foto
        self.takeShot() #salva foto no banco de dados
        self.sayFinish() #fim da rotina
        return()
