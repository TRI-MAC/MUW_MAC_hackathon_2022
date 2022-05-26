import requests as req
import time

 
#r = req.get('http://tg03b-080200042301.local/rest/webrtc.name')
r=req.post('http://tg03b-080200042301.local/rest/recorder.visible-name',data={"body":"Rec1"})
#r2=req.get('http://tg03b-080200042301.local/rest/recorder.visible-name')
print(r.text)