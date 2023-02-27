import cv2

def convertVideo(fName, category):
  vidcap = cv2.VideoCapture(fName)
  success, image = vidcap.read()
  count = 0
  while success:
    outFName = f"./data/ccd_frames/{category}/{fName.split('/')[-1]}-{count}.jpg"
    cv2.imwrite(outFName, image)
    success, image = vidcap.read()
    count += 1

convertVideo("./data/Uge2ipmaE2c.mp4", "Accident")

