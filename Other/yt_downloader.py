from pytube import YouTube
''' one liner script:
YouTube('https://youtu.be/aiRY36TPVo8').streams.first().download('E:/')
'''

def videoder(path,url):
    yt = YouTube(url)
    yt = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    yt.download(path)
    print('Video Downloaded')


if __name__ == '__main__':
    url = input('Input url: ')
    path = input('Input path: ')
    videoder(path,url)


