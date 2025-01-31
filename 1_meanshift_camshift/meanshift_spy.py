import cv2
import numpy as np


#burada yapacagimiz sey kamermizla bir yuz algilayip onun takibini yapmak



#kameramizi aciyoruz
cap = cv2.VideoCapture(0)



#ve ardindan bir tane frame yakaliyoruz, neden bir tane? cunku;
#normalde bunu while dongusu icinde yapiyorduk ama simdi takip islemini gerceklestirecegimiz icin bizim amacimiz
#onde yuzu tespit etmek bunu bir kere yapicaz sonrasinda takibe while dongusu icerisinde gecice cunku;
#eger while dongusu icerisinde biz bu yuzu tespit etseydik bu takip degil de zaten tespit algoritmasi olurdu.
#bu nedenle bir tane frame okuycaz.

ret, frame = cap.read()

if ret == False:
    print("Uyarı")
    

#simdi ise yuz detection islemine gecelim, bunu da onceki projelerde kullandigimiz haarcascade ile yapicaz.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
face_rects = face_cascade.detectMultiScale(frame)

(face_x, face_y, w, h) = tuple(face_rects[0])
track_window = (face_x, face_y, w, h) # meanshift algoritması girdisi

#takip algoritmasi burada detectMultiscale de tespit ettigi yuzun face_rects deki kordinatlarina gore track window u baslaticak.


#simdi ise region of interest yapicaz, region of interest dedigimiz sey ise;
#tespit edilen kutucugun icerisi, yani yuz

roi = frame[face_y:face_y + h, face_x : face_x + w] # roi = face

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)



#simdi ise hsv_roi nin histogramini hesaplamamiz gerekiyor onu yapalim.

roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180]) # takip için histogram gerekli
cv2.normalize(roi_hist , roi_hist ,0 ,255, cv2.NORM_MINMAX)



# takip icin gerekli durdurma kriterleri
# count = hesaplanacak maksimum oge sayısı
# eps = degisiklik
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5, 1)   #5 yineleme ya da 1 tane epsilon



#burada takibe basliyoruz.
while True:
    
    ret, frame = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # histogramı bir goruntude bulmak için kullnıyoruz
        # piksel karşılaştırma
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],1)

        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
        x,y,w,h = track_window
        
        img2 = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),5)
        
        cv2.imshow("Takip", img2)
        
        if cv2.waitKey(1) & 0xFF == ord("q"): break
            
cap.release()
cv2.destroyAllWindows()




























































