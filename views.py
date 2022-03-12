from flask import request, jsonify
from flask.views import MethodView

from app import app
from validator import validate
from models import Ads
from schema import ADD_ADS

class AdsView(MethodView):

    @validate('json', ADD_ADS)
    def put(self, ads_id):
        ads_n = Ads(**request.json)
        ads = Ads.by_id(ads_id)

        ads.title = ads_n.title
        ads.description = ads_n.description
        ads.data_create = ads_n.data_create
        ads.user_id = ads_n.user_id

        ads.update()
        return jsonify(ads.to_dict())

    def delete(self, ads_id):
        ads = Ads.by_id(ads_id)
        ads.delete_ads()
        return jsonify({"message": f"Successfully deleted."})

    def get(self, ads_id):
        ads = Ads.by_id(ads_id)
        return jsonify(ads.to_dict())

    @validate('json', ADD_ADS)
    def post(self):
        ads = Ads(**request.json)
        ads.add()
        return jsonify(ads.to_dict())


@app.route('/health/', methods=['GET', ])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'OK'})

    return {'status': 'OK'}


app.add_url_rule('/ads/<int:ads_id>', view_func=AdsView.as_view('ads_get'), methods=['GET', 'DELETE', 'PUT'])
app.add_url_rule('/ads/', view_func=AdsView.as_view('ads_create'), methods=['POST', ])