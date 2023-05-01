from flask import jsonify, request

from Auth.auth import protected,get_identity
from . import api
from user.models import User
from .models import Table,Items




@api.route('/')
def index():
    return 'This is The Main Blueprint'

@api.route('/table', methods=['GET'])
@protected('woche user')
def get_tables():
    data = []
    user_id = get_identity()
    user = User.query.filter(User.id == user_id).first()
    if user:
        tables = Table.query.filter(Table.user_id == user_id).all()
        for table in tables:
            t = table.format()
            data.append(t)
    else:
        return jsonify({
        'message': 'User not found'
        }), 404
    return jsonify({
        'data': data
        }), 201

@api.route('/table/create',methods=['POST'])
@protected('woche user')
def create_table():
    user_id = get_identity()
    user = User.query.filter(User.id == user_id).first()
    if user:
        table_name = request.json.get('table_name')
        exist_table = Table.query.filter(Table.name == table_name ).first()
        if exist_table:
            return jsonify({
            'message': 'Table Already Exist',
            'data': exist_table.format()
        }), 200  
        table = Table(name=table_name, user_id=user_id)
        table.insert()
    else:
        return jsonify({
        'message': 'User not found'
        }), 404
    return jsonify({
        'message': 'Table created successfully',
        'data': table.format()
        }), 201
  
@api.route('/table/<string:table_id>', methods=['GET'])
@protected('woche user')
def get_table_by_id(table_id):
    data = []
    user_id = get_identity()
    table = Table.query.filter_by(id=table_id, user_id=user_id).first()
    if table:
        items = Items.query.filter(Items.table_id==table.id).all()
        for item in items:
            i = item.format()
            data.append(i)
        return jsonify({
            'success': True,
            'Table': table.format(),
            'items':data
        }), 200
    else:
        return jsonify({
        'message': 'Table not found'
        }), 404

@api.route('/table/<string:table_id>', methods=['DELETE'])
@protected('woche user')
def delete_table(table_id):
    user_id = get_identity()
    table = Table.query.filter_by(id=table_id, user_id=user_id).first()
    if not table:
        return jsonify({'message': 'Table not found'}), 404
    table.delete()
    return jsonify({'message': 'Table deleted successfully'})

@api.route('/table/<string:table_id>', methods=['PATCH'])
@protected('woche user')
def update_table(table_id):
    pass