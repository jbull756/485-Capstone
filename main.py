import requests
import urllib.request
import requests
from bs4 import BeautifulSoup
import json
from monkeylearn import MonkeyLearn
import os.path
import time


Econ_Class_Lists=[101, 102, 108, 208, 251, 310, 320, 325, 340, 395, 396, 401, 402, 409, 421, 422, 431,
                  435, 441, 442, 444, 451, 452, 457, 461, 481, 490, 491, 495]
#URL format: https://webapps.lsa.umich.edu/open/syllabushandler.ashx/175000/2110/ECON/101

#Inputs for different departments and classes
Classes_list=Econ_Class_Lists
url="https://webapps.lsa.umich.edu/open/syllabushandler.ashx/"
department_id= "175000" #Econ
Term="2110" #winter 2017
department_name="ECON"

PDF_List=[]
for class_num in Classes_list:

    output_name="syllabusfor_"+str(class_num)+str('.')+"pdf"
    if os.path.exists(output_name)== False:
        class_num=str(class_num)
        combined_url=url+department_id+"/"+Term+"/"+department_name+"/"+class_num

    	#URL call
        response = urllib.request.urlretrieve(combined_url, output_name)
        if response:
            print("File "+output_name+" was downloaded ")

    if os.path.exists(output_name) == True:
        print("File "+output_name+" already exists ")



for class_num in Classes_list:
    file_name = "syllabusfor_" + str(class_num) + str('.') + "pdf"

    with open(file_name, 'rb') as payload:
        response = requests.post("https://api.monkeylearn.com/v2/extractors/ex_8tMs2MDB/extract/",
        files={'file': payload},
        headers={'Authorization': 'Token def5e8a69387cf4226aa7e9fa04fa12083ffa913'})
    time.sleep(5)
    print(json.loads(response.text))







    #Current_Syllabus= open(file_name, 'rb').read()
    #path = "/Users/Trey/Desktop/si485"+file_name
    #subprocess.call(["pdf2htmlEX", path], shell=False)










