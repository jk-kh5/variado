#coding: utf-8
#title_en: Tmohentai
#comment: https://tmohentai.com/
import downloader
from utils import Downloader, Soup, lazy, Session, clean_title

@Downloader.register
class Downloader_tmohentai(Downloader):
    type = 'tmohentai'
    URLS = ['tmohentai.com']
    icon = 'base64:AAABAAEAGBgAAAEAIAAoCQAAFgAAACgAAAAYAAAAMAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADMzzAUvN75mSFDDxT1Bvu0mKrvuJiu87i81vO4vNbzuLzW87i41vO4vNbzuLzW87i81vO4vNb3uLzW87i41ve4vNbzuMDbByDE3v2sgIL8IAAAAAAAAAAAAAAAAKjW1GC00vLQsNMb/a3DV/9XV7f+lqN7/VFnH/yUtv/8rMsH/MTjC/zE3wv8wN8L/MDfC/zE3wv8wN8L/MDfC/zA3wv8wN8L/MTnH/zI5yf8uN767Lja2HAAAAABJSbYHLTW6tDM7zf8uNb//JS26/4yQ2///////7+/z/5SX1P8zOr3/ISm6/yQruv8iKrr/Iiu6/yIquv8kLLv/KC68/y00vf8vNrz/Lza9/y82v/8zO83/LzW8vS4uuQswOL1gMTnH/zE3wP8vNrz/LDO8/yQsuf+tsOX///////7////Cw+L/XWPF/2Rpx/97gM7/gIXP/3d6zP9iZ8b/R0zA/y00u/8jKrr/KjG8/y82vf8wN7//MjjI/zA0vGswNr3BMjnI/y42vf8vNr3/Lza9/x0kuP9CScL/7u75//7/////////+fj4//39+v////7////+/////f/8/Pn/6evx/8HC4v98gM3/Nzy8/yQruv8uNb3/MjnH/y42vMsvNb3pMDfC/y82vf8sNLz/Iyu5/1FXw/+xst//+Pj7//////////7///////7///////////////////////////////////////3/0dPm/2Nnxv8kK7r/LjbC/y81vO4vNb3uMDfC/yoyvP8nLrr/gYTR/+3u9f////////7///////////7///////////////7///////////////7///////7///////////////Pz9v94fMv/Jiy+/y00u+8vNL3tLTXB/ygvuv+andn///////////////////7///////////////////////////////7///////////7///7///7///////7///7///7////4+Pf/ZWrM/yMpuu4uM73tJSy+/5OX2P/u7ff/oaPh//T0+/////7/y8zt/36C1f/Awuv//////6Om4v+pq+P//////7m76f9/hNb/2Nny/8rM7v9wdNH/bXPP/6Wo4v//////1tjv/zU6vO4iKLntYGTO///9/f/R0vD/QUfB/+rq+P//////m5zd/wcPsP+MkNr/7u/5/y41vP83Pr7/8/P6/36C1f8SGrT/dHnR/1RayP+doN//sbTm/11iy/+Dhtf//////3Z8zO4sMbvtxsjv///////Nzu//TVLF/+vr+P//////oKPf/xYetf+eoN7/trnn/yAnuP8kK7r/v8Dq/5KV2/8jKrn/KjG7/4yP2f////7///////Dw+v9NU8b/yMjw/7284+5fZsrt/Pz////////Nzu7/TVPF/+vr+P//////oKLf/xghtf+cn9//cHTR/0lPxP9FS8L/e3/V/5SY3P8hKrn/ICi4/6qs4/////////////7///+RlNr/foLa/9TV6e6Yndvt//7////////Nzu7/TVLF/+vr+P//////oKPf/yAouP+BhNX/OkHA/56i4P+Ul9z/P0bB/3+B1P8qMbr/JS25/5mb3v////////7///////+6vOj/ZGnR/8TG5+68vent//7////////Nzu7/TVPF/+vr+P//////oKPf/yctuf9KUMX/Mzi+/9zd8//S0/H/MDa9/0pPxP8yOb//SU7D/3F20f////////7////////Lze7/YWbQ/56g2+7Awujt//7////////W1/H/T1TF//b2/P////7/qKnh/yMruf8jKrn/V1zJ//z9/v/5+P3/TlTG/yQsuv8sM7z/j5Pa/1ZcyP/Gx+z///////////+ytOb/YWbP/3F1zu6kp+DtzM/w/6yv5P+Nkdr/Njy+/6Ok4P+zteb/b3PQ/xkhtv8UHLX/kJLb//////////7/hIjX/xMbtP8XHrX/r7Pl/7m66P9KUMX/oKPg/6ut4/9WW8n/gofZ/0RHwO5tc8/tpKfm/3R50v96f9T/foLV/3p+1P96ftT/fIDU/32C1f98gNT/2trz//////////7/09Xw/3l+1P93e9P/zMzu///////DxO3/dXnS/29z0P+zteb/e4DY/yIquu4zOb3u2tv3//////////////7///7///////////////////////////////7///////////7///////////////7///////////7///7///////+1t+b/LDPA/yszu+8gKLfpa3DU//z8/v////////7///7///////////////////////////////7///////////////////////7///7///7//////////////7u86f8yOb7/KjHA/zA1vO4uNLu+Jy/E/4SH1//7+/7///////////////////////////////7///////////////////////////////////////7////+/v//n6Pg/zA2vf8nL7v/MjjH/zA2u8gvN7xcLzbG/yUsvP9scc//29zz//7///////7///////7///////////7///7//////////////////////////////8/Q7/9qb9D/JS26/ygwu/8wN77/MjjI/zE4vWUzM8wFLze7rTE5zP8jK7z/O0LA/4mL2P/P0e//+fn9//////////7//////////////////////+jq+P+6vOj/cXbS/zM5vv8iKrn/LTW8/zA3wP8zO83/Lja7tSFAvwgAAAAAMzKzFDE2vasyOcb/LDLG/yMrvv8zOsL/V1zN/3p+2P+QlOH/mJzi/5KW4P+Bhdv/ZWrS/0RKyP8qMcD/JCu+/ywzwf8xOMP/MjnI/zI5x/8vNr2yLDe8FwEAAAAAAAAAAAAAAAEAgAIyN75cLza/vC80vugrMbztJC267SAnue0gJrntISe57SAnue0gJrjtJCm57SYvu+0tMbztLzS97S81vu0vNb3pMDS+vy83vWFAQL4EAAEAAAAAAAA='
    display_name = 'Tmohentai'
    MAX_CORE = 4
    ACCEPT_COOKIES = [r'(.*\.)?(tmohentai\.com)']
    referer = 'https://tmohentai.com/'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

    def init(self):
        self.type_id = self.url[self.url.rfind('/') + 1:]
        self.session = Session()
        html = downloader.read_html('https://tmohentai.com/reader/' + self.type_id + '/cascade', session=self.session)
        self.soup = Soup(html)

    @classmethod
    def fix_url(cls, url):
        return url.replace('http://', 'https://')

    @lazy
    def id(self):
        art = self.soup.find('ul', class_='dropdown-menu')
        id = art.findAll('li')
        art = id[2].find('a')
        if not art:
            art = id[1].find('a').text.strip()
            if art == 'No artists' or art == '':
                art = id[4].find('a').text.strip()
                if art == 'No magazines' or art == '':
                    art = 'N-A'
        else:
            art = id[1].find('a').text.strip() + ', ' + art.text.strip()
        id = art + ']' + self.soup.find('h1', class_='reader-title').text.strip() + '(' + self.type_id
        return clean_title(id)

    @property
    def name(self):
        return self.id

    def read(self):
        #self.title = self.name
        self.urls, self.filenames = get_imgs_www(self.soup)
        self.title = self.name

def get_imgs_www(soup):
    imgs = []
    filenames = {}
    for img in soup.find('div', class_='container').findAll('img'):
        data = img['data-original']
        imgs.append(data)
        filenames[data] = data[data.rfind('/')+1:]
    return imgs,filenames
