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
            dict = {}
            dictYil = {}
            dictGrup = []

            _yillar = self.session.query(Projeler.yil).filter(Projeler.yil==self.yil).order_by(Projeler.yil.desc()).group_by(Projeler.yil).all()
            for _yil in _yillar:
                _gruplar = self.session.query(Projeler.grup).filter(Projeler.yil==_yil.yil, Projeler.grup == self.grup).order_by(Projeler.grup.desc()).group_by(Projeler.grup).all()
                for _grup in _gruplar:
                    result = self.session.query(Projeler.id, Projeler.yil, Projeler.grup, Projeler.baslik, Projeler.aciklama, Projeler.sonuc, Projeler.birim, Projeler.durum).filter(Projeler.grup==_grup.grup).order_by(Projeler.durum)
                    for row in result:
                        dictGrup.append({'id':row.id, 'yil':row.yil,'grup':row.grup, 'baslik':row.baslik, 'aciklama':row.aciklama, 'sonuc':row.sonuc, 'birim':row.birim, 'durum':row.durum})

                    dictYil.update({_grup.grup: dictGrup}) #objede update, arrayde append fonksyion kullan...
                    dictGrup = []

                dict.update({_yil.yil:dictYil})
                dictYil = []

            _json = jsonify({"projeler":dict})

            if (len(dict) == 0):
                return Response("No record found!")
            else:
                return _json

        except Exception as e:
            return Response("sa query error! ",e)


# if __name__ == "__main__":
#     e = ProjelerApi()
#     e.message()

    # print("Base created successfully..")