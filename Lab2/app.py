from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf8')



#2. Analyze ROI ( Region of Interest)
#2.1 Create beautifulsoup
soup = BeautifulSoup(html_content, "html.parser")

section = soup.find('section', 'section chart-grid')
ul = section.find('ul')
li_list = ul.find_all('li')

new_list = []

for li in li_list:
#
#

    h4 = li.h4 #find(a)
    a_list = h4.find_all("a")

    # Find singles
    artists= []
    for a in a_list:
        a.string = a.string
        artists.append(a.string)

    # find song
    name = li.h3.a
    song_name = name.string

    Answer = { "name": song_name,"artists": ", ".join(artists)}

    new_list.append(Answer)


pyexcel.save_as(records = new_list, dest_file_name= "itune1.xlsx")

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': len(Answer), # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
for songs in Answer:
    dl.download(songs)
