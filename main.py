from urllib import request
import json, os

TOKEN = 'f39cb9f09d3c0b5032bc1883a6d135f8'

api = 'https://api.54heb.com/'
checkTokenUrl = 'checktoken'
getClassListUrl = 'study/studyLink'
clockUrl = 'study/statistics'
clockParams = '?type=new&id='

def sendRequest(url, params=''):
  headers = {
    'token' : TOKEN
  }
  req = request.Request(url=api+url+params, headers=headers)
  res = request.urlopen(req)
  data = json.load(res)
  return data

def main():
  tokenVaildCode = sendRequest(checkTokenUrl)['code']
  if (tokenVaildCode != 0):
    raise Exception("error token code")
  print('Success vaild token')
  classList = sendRequest(getClassListUrl)['data']
  newClassList = classList['new']
  print('Get newest class:', newClassList['name'], newClassList['brief'])

  clockCode = sendRequest(clockUrl, clockParams+str(newClassList['id']))['code']
  if(clockCode != 0):
    raise Exception("unsuccess clock")
  else:
    print('Success clock')

if __name__ == '__main__':
    main()
