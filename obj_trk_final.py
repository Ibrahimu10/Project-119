import cv2



video=cv2.VideoCapture("video.mp4")

 
tracker=cv2.TrackerCSRT_create()


boolean, frames = video.read()

# Select the bounding box on the image
bbox=cv2.selectROI("Choose What To Track", frames, False)


tracker.init(frames, bbox)



def drawing(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(50,120,150),3)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
while True:
    check,img=video.read()   
    success,bbox=tracker.update(img)
    if success:
        drawing(img,bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("result",img)
            
    key=cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()







