from flask import Flask, render_template, redirect, url_for
from models.service import Service

from mlab import mlab_connect

app = Flask(__name__)
mlab_connect()

# id_to_find = "5a3b5e32f3718221f4d462a1"
#
# # god = service.objects(id=id_to_find).first() #normal way
#
# Neal = service.objects().with_id(id_to_find) #for id
# if Neal is None:
#     print("Not Found")
#
# else:
#     print(Neal.Name)
#     Neal.update(set__occupied = True) #inc__
#     print(Neal.occupied)
#     Neal.reload()
#     print(Neal.occupied)

    # god.delete()
@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('form.html')

@app.route('/search/<int:gender>')
def search(gender):
    filter_service = Service.objects(gender = gender, occupied = False)
    # for service in all_service:
    # first_service = all_service[0]
    return render_template('search.html', all_service = filter_service)

@app.route('/admin')
def admin():
        # print(Service.objects[0].Name)
        return render_template("admin.html", services = Service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
      Service.objects(id=service_id).delete()
      return redirect(url_for("admin"))
      # render_template("admin.html", services = Service.objects())

@app.route('/blockaudio')
def blockaudio():
    return render_template('blockaudio.html')

@app.route("/BTVN")
def BTVN():
    return render_template("BTVN.html")


if __name__ == '__main__':
  app.run( debug=True)




# filter_service = service.objects(gender = 1, height__gte = 160).first()
# #
# # for service in filter_service:
# #     print(service.Name, service.height)
#
# # filter_service[0].delete
# # If filter_service is not None:
# #     print("Not FOund")
#
# for service in filter_service:
#     if service.occupied == False:
#         service.update(set__occupied = True)
#         print(service.Name, service.height, service.occupied)
#         service.reload()1
#         print(service.Name, service.height, service.occupied)
