from flask import Response
from flask import jsonify
from db.connection import Connect
from db.model import Projeler


class ProjelerApi():
    def __init__(self, yil, grup):
        self.conn = Connect()
        self.session = self.conn.session()
        self.yil = yil
        self.grup = grup

    def __del__(self):
        self.session.close()

    def message(self):
        try:
            dict = []

            data = self.session.query(Projeler.id, Projeler.yil, Projeler.grup, Projeler.baslik, Projeler.aciklama, Projeler.sonuc, Projeler.birim, Projeler.durum, Projeler.zamandamgasi)
            if (self.grup is not None):
                data = data.filter(Projeler.yil==self.yil, Projeler.grup==self.grup)
            else:
                data = data.filter(Projeler.yil==self.yil)

            data = data.order_by(Projeler.durum, Projeler.grup)

            for row in data:
                dict.append({'id':row.id, 'yil':row.yil,'grup':row.grup, 'baslik':row.baslik, 'aciklama':row.aciklama, 'sonuc':row.sonuc, 'birim':row.birim, 'durum':row.durum, 'zamandamgasi':row.zamandamgasi})

            _json = jsonify({"projeler":dict})

            if (len(dict) == 0):
                return Response("NO DATA found!")
            else:
                return _json

        except Exception as e:
            return Response("sa query error! ",e)


# if __name__ == "__main__":
#     e = ProjelerApi()
#     e.message()

    # print("Base created successfully..")