import urllib.request, urllib.parse
import json
import time

token = '61bb9e30860022e57953faa7755eb82c352956f888282a313a06d309909bd1b6ad330989981ee6d310f48'
def getlongPollServer():
    """делает запрос метода messages.getLongPollServer к vk API, в ответе возвращает кортеж из messages.getLongPollServer"""
    params = urllib.parse.urlencode({'access_token':token})
    response = json.loads(urllib.request.urlopen('https://api.vk.com/method/messages.getLongPollServer?%s' % params).read().decode('UTF-8'))
    server = response['response']['server']
    key = response['response']['key']
    ts = response['response']['ts']
    return server, key, ts

def getNewMessages(server, key, ts):
    response = urllib.request.urlopen('http://%s?act=a_check&key=%s&ts=%s&wait=25&mode=0' % (server, key, ts)).read().decode('UTF-8')
    return response

def getUserInfo(id):
    response = json.loads(urllib.request.urlopen('https://api.vk.com/method/users.get?user_ids=%s' % id).read().decode('UTF-8'))
    firstName = response['response'][0]['first_name']
    return firstName

def getUserInfoByMessageId(messageId):
    params = urllib.parse.urlencode({'message_ids':messageId, 'access_token': token})
    response = json.loads(urllib.request.urlopen('https://api.vk.com/method/messages.getById?%s' % params).read().decode('UTF-8'))
    return response['response'][1]['uid']

def sendMessageTelegram(text):
    params = urllib.parse.urlencode({'chat_id':'-14476920','text':text})
    response = urllib.request.urlopen('https://api.telegram.org/bot%s/sendMessage?%s' % ('137230011:AAFMRRRNr3ufNEjEYXTm77378-gUJVmmL6A', params))

NewMessages = json.loads(getNewMessages(getlongPollServer()[0], getlongPollServer()[1], getlongPollServer()[2]))
server = getlongPollServer()[0]
key = getlongPollServer()[1]
ts = getlongPollServer()[2]
while True:
    if 'failed' not in NewMessages:
        ts = NewMessages['ts']
        for i in range(len(NewMessages['updates'])):
            if NewMessages['updates'][i][0] == 4 and NewMessages['updates'][i][-2] == 'Дно':
                print(NewMessages)
                messageId = str(NewMessages['updates'][i][1])
                message = NewMessages['updates'][i][-1]
                sendMessageTelegram(getUserInfo(getUserInfoByMessageId(messageId)) + ': ' + message)
        NewMessages = json.loads(getNewMessages(server, key, ts))
    else:
        NewMessages = getNewMessages(getlongPollServer()[0], getlongPollServer()[1], getlongPollServer()[2])
        ts = NewMessages['ts']
        print(NewMessages, ts)