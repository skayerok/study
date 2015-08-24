import requests
import urllib.request

r = requests.get('https://www.googleapis.com/youtube/v3/search?fields=items%28id%2Csnippet%29&order=date&type=video&access_token=ya29.1QHHG3k8pOKObKzeqaarLd0p6v0lJ5lNbbpCd2-I_bdFD549QI6eE8es0M2oRxRu8syu&publishedAfter=2015-08-20T08%3A58%3A20Z&channelId=UC-bXlo2JKw9pjM0V0wmGrGA&maxResults=3&part=snippet')
u = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/search?fields=items%28id%2Csnippet%29&order=date&type=video&access_token=ya29.1QHHG3k8pOKObKzeqaarLd0p6v0lJ5lNbbpCd2-I_bdFD549QI6eE8es0M2oRxRu8syu&publishedAfter=2015-08-20T08%3A58%3A20Z&channelId=UC-bXlo2JKw9pjM0V0wmGrGA&maxResults=3&part=snippet')
print(r.json())
print(u)   #url, read, code, readline(s)