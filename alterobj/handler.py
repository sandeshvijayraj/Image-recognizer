#!/usr/bin/enc python3
import subprocess
import os
from flask import Flask,request,redirect,render_template
import requests
import json
from flask_cors import CORS
import test as t

selectedlis=["apple","orange","banana","broccoli","carrot","sandwich","pizza"]

mylist=[]
retlink="hell"

app=Flask(__name__)
CORS(app)

@app.route("/getrun",methods=['POST','GET'])
def doing():
	import myfirst as obj
	global mylist,retlink
	mylist=[]
	print("doing")
	print(mylist)
	images=request.files.getlist("abc")
	for img in images:
		print("in loop")
		fil_name=img.filename
		print("here"+fil_name)
		img.save(os.getcwd()+"/"+fil_name)
		print("moved")
	items=obj.objdtc()
	imgs=t.listimg()
	for abc in imgs:
		os.remove(abc)
	os.remove(".png")
	for x in items:
		temli=x.split(" : ")
		if (temli[0] not in mylist) and (temli[0] in selectedlis) and(float(temli[1])>=55.00):
			mylist.append(temli[0])
	print(mylist)
	retlink='%20'.join(mylist)
	print("https://www.food2fork.com/api/search?key=cedb20aa01fb90aaa09d6ce33ac707e7&q="+retlink)
	#jobj=json.loads(x)
	return redirect("http://192.168.43.180/result.html")

@app.route("/getlink",methods=['POST','GET'])
def getlink():
	global retlink
	return "https://www.food2fork.com/api/search?key=cedb20aa01fb90aaa09d6ce33ac707e7&q="+retlink
app.run(host='0.0.0.0')