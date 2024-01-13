import speech_recognition as sr
import cv2

def buka_kamera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow('Window Title', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Ini bisa dipake tapi di laptop saya kamera malah jadi not responding

        # print("Berikan saya perintah")
        # pr = sr.Recognizer()
        # mic2 = sr.Microphone()
            
        # with mic2 as source:
        #     audio = pr.listen(source)
                
        #     try:
        #         text = pr.recognize_google(audio, language='id').lower()
        #         print("Perintah : ", text)
                    
        #         if "tutup kamera" in text:
        #             print("tutup kamera sedang dijalankan")
        #             break 
                    
        #     except:
        #             print("suara kamu tidak terdengar")


    cap.release()
    cv2.destroyAllWindows()

def pendeteksi_suara():
    recognition = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Coba kamu ngomong")
        audio = recognition.listen(source)

        try:
            text = recognition.recognize_google(audio, language='id').lower()
            print("Pasti Kamu ngomong : ", text)
            if "buka kamera" in text:
                buka_kamera()
        except sr.UnknownValueError:
            print("Suara kamu kurang jelas")


pendeteksi_suara()
