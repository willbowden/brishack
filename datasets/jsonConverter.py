import json
import xmltodict

NUMFILES = 9997

def convertAllFiles():
  count = 0
  for i in range(NUMFILES+1):
    fname = f"./dataset/Annotations/00{str(i).zfill(4)}.xml"
    with open(fname, "r") as infile:
      dataDict = xmltodict.parse(infile.read())
      dataDict = dataDict["annotation"]
      if "object" in dataDict:
        if isinstance(dataDict["object"], dict):
          dataDict["object"] = [dataDict["object"]]
        final = {
          "index": count,
          "imageName": i,
          "objects": [
            {"type": x["name"],
            "xmin": float(x["bndbox"]["xmin"]),
            "ymin": float(x["bndbox"]["ymin"]),
            "xmax": float(x["bndbox"]["xmax"]),
            "ymax": float(x["bndbox"]["ymax"])
            }
            for x in dataDict["object"]]
          }
        with open(f"./dataset/json/{count}.json", "w") as outfile:
          json.dump(final, outfile)
        print(count)
        count += 1
        

  

if __name__ == '__main__':
  convertAllFiles()