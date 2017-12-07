from datetime import*
now = datetime.now()


from gmail import GMail, Message

html_content_1 = '''<p><strong>Em ch&agrave;o c&ocirc;,&nbsp;</strong></p>
<p>H&ocirc;m nay em ngủ dậy bị {lydo}. B&aacute;c sĩ bảo em bị đ&aacute;i th&aacute;o đường phải đi ti&ecirc;m chủng 4 ng&agrave;y.</p>
<p>C&ocirc; cho em xin nghỉ để đi ti&ecirc;m nh&eacute; :(</p>
<p><strong>Học sinh của c&ocirc;!!!!</strong></p>'''

html_content_2 = '''<p><strong>Em ch&agrave;o c&ocirc;,&nbsp;</strong></p>
<p>H&ocirc;m nay em ngủ dậy bị {ly do}. B&aacute;c sĩ bảo em bị ti&ecirc;u chảy phải đi ti&ecirc;m chủng 4 ng&agrave;y.</p>
<p>C&ocirc; cho em xin nghỉ để đi ti&ecirc;m nh&eacute; :(</p>
<p><strong>Học sinh của c&ocirc;!!!!</strong></p>'''

html_content_3 = ''' <p><strong>Em ch&agrave;o c&ocirc;,&nbsp;</strong></p>
<p>H&ocirc;m nay em ngủ dậy bị {lydo} phải l&ecirc;n n&uacute;i điều trị mấy h&ocirc;m</p>
<p>C&ocirc; cho em xin nghỉ để đi điều trị nh&eacute; :(</p>
<p><strong>Học sinh của c&ocirc;!!!!</strong></p>'''

html_content = [html_content_1, html_content_2, html_content_3]

lydo = ["ung thư", " dau bung", "daidam"]

from random import choice
template = choice(html_content)
lydo1 =  choice(lydo)
content = template.replace("{ly do}", lydo1)

gmail = GMail("conranconcon@gmail.com","ehh12345")
msg = Message(" Đơn xin nghỉ ốm" ,to= "c4e14.labs.huynq@gmail.com",html = choice(content))

while now.hour == 7:
    n = input("Bạn có muốn gửi thư? Y/N ").lowercase()
    if n == Y:
        gmail.send(msg)
        print("done")
    else: print("ok cảm ơn bạn")
