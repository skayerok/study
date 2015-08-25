import urllib.request, urllib.parse
import json
import time

token = 'ololo'

def getlongPollServer():
    """делает запрос метода messages.getLongPollServer к vk API, в ответе возвращает кортеж из messages.getLongPollServer"""
    params = urllib.parse.urlencode({'access_token':token})
    response = json.loads(urllib.request.urlopen('https://api.vk.com/method/messages.getLongPollServer?%s' % params).read().decode('UTF-8'))
    server = response['response']['server']
    key = response['response']['key']
    ts = response['response']['ts']
    return server, key, ts

def getNewMessages(server, key, ts):
    response = urllib.request.urlopen('http://%s?act=a_check&key=%s&ts=%s&wait=25&mode=2' % (server, key, ts)).read().decode('UTF-8')
    return response

def getUserInfo(id):
    response = json.loads(urllib.request.urlopen('https://api.vk.com/method/users.get?user_ids=%s' % id).read().decode('UTF-8'))
    firstName = response['response'][0]['first_name']
    return firstName

"""def getUserInfoByMessageId(messageId):
    params = urllib.parse.urlencode({'message_ids':messageId, 'access_token': token})
    response = json.loads(urllib.request.urlopen('https://api.vk.com/method/messages.getById?%s' % params).read().decode('UTF-8'))
    return response['response'][1]['uid']"""

def sendMessageTelegram(text):
    params = urllib.parse.urlencode({'chat_id':'-14476920','text':text})
    response = urllib.request.urlopen('https://api.telegram.org/bot%s/sendMessage?%s' % ('lololo', params))

def log(*arg):
  log = open ('log.txt', 'a')
  log.seek(0,2)
  log.write(time.ctime() + ':')
  log.write(str(arg) + '\n')

longPollServer = getlongPollServer()
server = longPollServer[0]
key = longPollServer[1]
ts = longPollServer[2]
NewMessages = json.loads(getNewMessages(server, key, ts))
while True:
    if 'failed' not in NewMessages:
        for i in range(len(NewMessages['updates'])):
            if NewMessages['updates'][i][0] == 4 and NewMessages['updates'][i][-3] == 'Дно':
                log(NewMessages)
                uid = NewMessages['updates'][i][-1]['from']
                message = NewMessages['updates'][i][-2]
                sendMessageTelegram(getUserInfo(uid) + ': ' + message)
        NewMessages = json.loads(getNewMessages(server, key, ts))
        ts = NewMessages['ts']
    else:
        longPollServer = getlongPollServer()
        NewMessages = getNewMessages(longPollServer[0], longPollServer[1], longPollServer[2])
        ts = NewMessages['ts']
