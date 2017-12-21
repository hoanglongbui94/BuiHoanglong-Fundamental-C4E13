
from mongoengine import Document, StringField, IntField, BooleanField

class service(Document):
    Name = StringField()
    YOB = IntField()
    gender = IntField() #0: Female. 1 : Male
    height = IntField()
    phone = StringField()
    occupied = BooleanField()
# ngan = service(Name = " Nguyen Thi Kim Ngan", YOB = "1993", gender = " 1", height = "163", phone = "0903001119", occupied = False)
# ngan.save()
