import cv2
import os

import dfentry as dfe

def take_photo(path, name):
    
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
    
    img_counter = 0
    min_size = (50,50)
    
    while True:
        
         ret, frame = cam.read()
         frame = cv2.flip(frame, 1)
         faces = face_detector.detectMultiScale(frame, 1.05, 5, minSize = min_size)
         for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
         if not ret:
             test_card = cv2.imread('test_card.jpg')
             cv2.imshow('failed to grab frame', test_card)
             #print("failed to grab frame")
         
         else:
             cv2.imshow("Capture_part", frame)
     
         k = cv2.waitKey(1)
         if k%256 == 27:
             # ESC pressed
             print("Escape hit, closing...")
             break
         elif k%256 == 32 and ret:
             # SPACE pressed
             img_name = os.path.join(path, name +  "_frame_{}.png".format(img_counter))
             cv2.imwrite(img_name, frame[y:y+h,x:x+w])
             print("{} written!".format(img_name))
             img_counter += 1
     
    cam.release()        
    cv2.destroyAllWindows()


if __name__ == '__main__': 
        
    path = './'
    csv_file = os.path.join(path, "name_list.csv")     
    ds_folder = os.path.join(path, "Dataset")  
    df = dfe.entry_system(csv_file)   
    print(df)
    
    name = input('Input your name_id: ')
    
    if (name in df['name_id'].values):
        print('Name validation sucess!')
        sub_path = df[df['name_id'] == name]['path'].tolist()[0]
        print(sub_path)
        dest_folder = os.path.join(ds_folder, sub_path)
        os.makedirs(dest_folder, exist_ok=True)
        take_photo(dest_folder,name)
        
    else:
        print('Name validation fail!')
    
