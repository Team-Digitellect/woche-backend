from flask import jsonify, request

from Auth.auth import protected,get_identity
from . import api
from .models import Table,Items



@api.route('/table/<string:table_id>', methods=['POST'])
@protected('woche user')
def create_Items(table_id):
    name = request.json['name']
    type = request.json['type']
    user_id = get_identity()
    table = Table.query.filter_by(id=table_id, user_id=user_id).first()
    if not table:
        return jsonify({
            'sucess':False,
            'message': 'Table not Found',
        }), 404
    if 'name' not in request.json or 'type' not in request.json:
        return jsonify({
            'sucess':False,
            'message': 'Invalid Request',
        }), 400

    if Items.query.filter_by(name=name, table=table).first():
        return jsonify({
            'sucess':False,
            'message': 'item with same name already exists in table',
        }), 400
    Item = Items(name=name, type=type, table_id=table.id)
    Item.insert()
    return jsonify({
        'success':True,
        'message': 'Items created successfully',
        'data': Item.format()
    }), 201

@api.route('/table/<string:table_id>', methods=['GET'])
@protected('woche user')
def get_Items_by_table(table_id):
    data=[]
    user_id = get_identity()
    table = Table.query.filter_by(id=table_id, user_id=user_id).first()
    if not table:
        return jsonify({
            'sucess':False,
            'message': 'Table not Found',
        }), 404
    items = Items.query.filter(Items.table_id == table.id).all()
    for item in items:
        t = item.format()
        data.append(t)
    return jsonify({
        'data': data
        }), 201

@api.route('/table/<string:table_id>/item/<string:item_id>', methods=['PUT'])
@protected('woche user')
def update_Item(table_id, item_id):
    name = request.json['name']
    user_id = get_identity()
    table = Table.query.filter_by(id=table_id, user_id=user_id).first()
    if not table:
        return jsonify({
            'sucess':False,
            'message': 'Table not Found',
        }), 404
    if 'name' not in request.json:
        return jsonify({
            'sucess':False,
            'message': 'Invalid Request',
        }), 400

    item = Items.query.filter_by(id=item_id, table_id=table.id).first()
    if not item:
        return jsonify({
            'success':False,
            'message': "Table's item not Found",
        }), 404
    item.name = name
    item.update()
    return jsonify({
        'success':True,
        'message': 'Item name updated successfully'
    }),200

@api.route('/table/<string:table_id>/items/<string:item_id>', methods=['DELETE'])
@protected('woche user')
def delete_items_by_table(table_id,item_id ):
    user_id = get_identity()
    table = Table.query.filter_by(id=table_id, user_id=user_id).first()
    if not table:
        return jsonify({'message': 'Table not found'}), 404
    item = Items.query.filter_by(id=item_id, table_id=table.id).first()
    if not item:
        return jsonify({
            'success':False,
            'message': "Table's item not Found",
        }), 404
    item.delete()
    return jsonify({
        'success':True,
        'message': 'Item Deleted successfully'
    }),200
  