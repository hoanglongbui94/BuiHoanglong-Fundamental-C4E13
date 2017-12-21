from mlab import mlab_connect
from models.service import service
from faker import Faker
from random import choice, randint

service_faker = Faker()
# print(service_faker.name())

mlab_connect()


service.drop_collection()
for i in range(30):
    services = service(Name = service_faker.name() , YOB = randint(1987,1998), gender = randint(0,1), height = randint(150,180), occupied = choice(  [True, False] ), phone = "0909121212")
    services.save()
