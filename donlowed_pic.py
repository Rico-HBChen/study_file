import requests,os,bs4
url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    #下载网页
    print('downloading page%s' % url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)

    #获得图片地址并下载
    comicelem=soup.select('#comic img')
    if comicelem==[0]:
        print('could not find comic image.')
    else:
        comicurl=comicelem[0].get('src')
        print('downloading img%s' % (comicurl))
        res=requests.get(comicurl)
        res.raise_for_status()

    #保存图片到文件夹
        imagefile=open(os.path.join('.','xkcd',os.path.basename(comicurl)),'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close

    #找到前一张图片地址
        prevlink=soup.select('a[rel="prev"]')[0]
        url='http://xkcd.com'+prevlink.get('href')

print('down')
    
