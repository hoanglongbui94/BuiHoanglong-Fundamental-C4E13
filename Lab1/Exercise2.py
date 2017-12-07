from pymongo import MongoClient


client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")


db = client.get_default_database()


blog = db["posts"]

new_post = {
'title': "Hòn đá cô đơn",
'author' : "Jason Hoang",
'content': ''' Co hon da co don xa xam
Dung o do co sao mot minh
Phai chang da cung that tinh
Hoa niem dau voi ta?
Co chi gio bay ngang qua (day)
Khe nhe vuot mat tam hon minh
"Nay cau trai that tinh!
Buon lam chi hoi em?"
Co giot nuoc roi tren mi (ai)
Khe nhe tham xot xa trong long
Hinh nhu nuoc cung biet rang:
"Nang da xa cach ta ..."
Oi giot nuoc dau thuong kia oi !
Cho voi khoc khien ta them buon,
Vi ta cung da biet rang:
Nang da xa cach ta.... '''}

blog.insert_one(new_post)
