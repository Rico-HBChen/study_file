'''import requests,os,bs4
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
        print(len(comicelem))
        comicurl=comicelem[0].get('src')
        print('downloading img%s' % (comicurl[0]))
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
'''
#抓取http://xkcd.com上的动画并保存
import os,requests,bs4,time,warnings
warnings.filterwarnings("ignore")
def grapWep():
    #保存目录
    os.makedirs('xkcd',exist_ok=True)
    #目标网站url
    url='https://xkcd.com'
    while not url.endswith('#'):
        print('Downloading page %s' % url)
        #打开网站
        openWep=requests.get(url)
        openWep.raise_for_status()
        #获取动画
        soup=bs4.BeautifulSoup(openWep.text)
        imgElems=soup.select('#comic img')
        #获取动画url
        imgUrl='https:'+imgElems[0].get('src')
        #打开动画
        openImg=requests.get(imgUrl)
        openImg.raise_for_status()
        #获取动画后缀名
        imgSuffix=os.path.splitext(imgUrl)[1]
        #重新编辑动画名
        imgName=os.path.basename(os.path.splitext(imgUrl)[0])+'_'+str(int(time.time()))+imgSuffix
        print('Downloading animation %s' % imgUrl)
        #以动画名作为文件名,并以二进制写模式打开文件
        imgFile=open(os.path.join('xkcd',imgName),'wb')
        for chunk in openImg.iter_content(1000):
            imgFile.write(chunk)
        
        imgFile.close()
        
        #前一幅动画的url
        prevLink=soup.select('a[rel="prev"]')[0]
    
        url='https://xkcd.com'+prevLink.get('href')
 
    print('End')

grapWep()
