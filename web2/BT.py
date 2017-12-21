from mlab import mlab_connect
from models.service import service


mlab_connect()
id_to_find = "5a3b5e32f3718221f4d462a1"
service = Service.objects.get(id =id_to_find)
print(service.name)

Service.objects(id = id_to_find).delete()
