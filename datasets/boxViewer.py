import cv2
import json
import random

def viewBounds(fileNo):
  fname = f"./dataset/json/{fileNo}.json"
  with open(fname, "r") as infile:
    jsonData = json.load(infile)

  img = cv2.imread(f"./dataset/JPEGImages/{str(jsonData['imageName']).zfill(6)}.jpeg")
  cv2.imshow("Original Image", img)
  cv2.waitKey(0)
  cv2.destroyWindow("Original Image")
  drawnImage = img.copy()
  for box in jsonData["objects"]:
    x1 = round(box["xmin"], 0)
    y1 = round(box["ymin"], 0)
    x2 = round(box["xmax"], 0)
    y2 = round(box["ymax"], 0)
    pt1 = (int(x1), int(y1))
    pt2 = (int(x2), int(y1))
    pt3 = (int(x2), int(y2))
    pt4 = (int(x1), int(y2))
    cv2.line(drawnImage, pt1, pt2, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
    cv2.line(drawnImage, pt2, pt3, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
    cv2.line(drawnImage, pt4, pt3, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
    cv2.line(drawnImage, pt1, pt4, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
    cv2.putText(drawnImage, box["type"].upper(), pt1, fontFace=16, fontScale=0.7, thickness=2, color=(255, 0, 0))
  
  cv2.imshow("Annotated Image", drawnImage)
  cv2.waitKey(0)
  

if __name__ == '__main__':
  num = random.randint(0, 9584)
  viewBounds(num)