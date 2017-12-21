from mlab import mlab_connect
from models.service import service


mlab_connect()
all_service = service.objects()


# first_service = all_service[1]
# print(first_service.Name)

for service in all_service:
    print(service.Name)
