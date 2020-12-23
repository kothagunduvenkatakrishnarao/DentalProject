import os
from PIL import Image
import random as r
import json
width  = 200
height = 200
i=1
def croping(imageobject,data,per):
    global i
    (w,h)=imageobject.size
    imageobject=imageobject.resize((int(w*per/100),int(h*per/100)))
    (w,h)=imageobject.size
    for p in data["annotations"]:
        a=p["left"]
        b=p["right"]
        c=p["top"]
        d=p["bottom"]
        a1=a*w
        b1=b*w
        c1=c*h
        d1=d*h
        if b1-a1<=width and d1-c1<=height:
            if a1 + width < w:
                a2=a1+width
            else:
                a2=w-1
            if b1 - width >= 0:
                b2=b1-width
            else:
                b2=0
            if c1 + height < h:
                c2=c1+height
            else:
                c2=h-1
            if d1 - height >= 0:
                d2=d1-height
            else:
                d2=0
            for j in range(2):
                k=r.uniform(b2,a1)
                l=r.uniform(b1,a2)
                m=r.uniform(d2,c1)
                n=r.uniform(d1,c2)
                z=r.choice([0,1])
                x=r.choice([0,1])
                if z==0:
                    if x==0:
                        croppedimage=imageobject.crop((k,m,k+width,m+height))
                        left=(a1-k)/width
                        right=(b1-k)/width
                        top=(c1-m)/height
                        bottom=(d1-m)/height
                    else:
                        croppedimage=imageobject.crop((k,n-height,k+width,n))
                        left=(a1-k)/width
                        right=(b1-k)/width
                        top=(c1-n+height)/height
                        bottom=(d1-n+height)/height
                else:
                    if x==0:
                        croppedimage=imageobject.crop((l-width,m,l,m+height))
                        left=(a1-l+width)/width
                        right=(width-l+b1)/width
                        top=(c1-m)/height
                        bottom=(d1-m)/height
                    else:
                        croppedimage=imageobject.crop((l-width,n-height,l,n))
                        left=(width-l+a1)/width
                        right=(width-l+b1)/width
                        top=(c1-n+height)/height
                        bottom=(d1-n+height)/height
                croppedimage.show()
                croppedimage.save("C:/Users/Lakshmi Prasanna/Desktop/dental_pic/crop"+str(i)+".jpg","JPEG")
                data1={}
                data1["annotations"]=[]
                data1["annotations"].append({
                    "caption" : p["caption"],
                    "id": 1,
                    "left" : left,
                    "right" : right,
                    "top" : top,
                    "bottom" : bottom
                })
                with open('C:/Users/Lakshmi Prasanna/Desktop/dental_pic/crop'+str(i)+".json", 'w') as outfile:
                    json.dump(data1, outfile)
                    i=i+1

if __name__ == "__main__":
    directory="C:/Users/Lakshmi Prasanna/Desktop/Dta"
    path="C:/Users/Lakshmi Prasanna/Desktop/dental_pic"
    if not os.path.exists(path):
        os.makedirdirs(path)
    for folder in os.listdir(directory):
        folder_name = directory + "\\" + folder
        for file_name in os.listdir(folder_name):
            if(file_name.endswith(".jpg")):
                file_path = folder_name + "\\" + file_name
                json_path = file_path[:-3]+"json"
                print(file_path,json_path)
                with open(json_path) as json_file:
                    data = json.load(json_file)
                im = Image.open(file_path)
                croping(im,data,100)
                croping(im,data,r.randint(75,80))
                croping(im,data,r.randint(66,75))
                croping(im,data,r.randint(45,65))