from pymongo import MongoClient
from matplotlib import pyplot


client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")


db = client.get_default_database()


customer = db["customers"]


events = customer.count({'ref':'events'})
ads = customer.count({'ref':'ads'})
wom = customer.count({'ref':'wom'})

ref = ['Events', 'Advertisement', 'Word of Mouth']
count_all = [events, ads, wom]


for i in range(len(ref)):
    for j in range(len(count_all)):
        if i == j:
            print('{0} has {1} references'.format(ref[i], count_all[j]))

color = ["gold",'lightcoral','#564652']
pyplot.pie(count_all, labels= ref, colors= color, shadow= True)
pyplot.axis('equal')
pyplot.show()
