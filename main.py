from flask import Flask, request, jsonify

app = Flask(__name)

contacts = []

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route('/contacts/create', methods=['POST'])
def create_contact():
    data = request.json
    if 'name' in data and 'mobile' in data:
        contact = {
            'name': data['name'],
            'mobile': data['mobile']
        }
        contacts.append(contact)
        response = {
            'status': 'success',
            'message': 'Contact created successfully'
        }
        return jsonify(response), 201
    else:
        response = {
            'status': 'error',
            'message': 'Invalid data'
        }
        return jsonify(response), 400

@app.route('/contacts', methods=['GET'])
def get_contacts():
    response = {
        'status': 'success',
        'data': contacts
    }
    return jsonify(response)

@app.route('/contacts/edit', methods=['POST'])
def edit_contact():
    data = request.json
    if 'name' in data and 'mobile' in data:
        for contact in contacts:
            if contact['name'] == data['name']:
                contact['mobile'] = data['mobile']
                response = {
                    'status': 'success',
                    'message': 'Contact edited successfully'
                }
                return jsonify(response), 200
        response = {
            'status': 'error',
            'message': 'Contact not found'
        }
        return jsonify(response), 404
    else:
        response = {
            'status': 'error',
            'message': 'Invalid data'
        }
        return jsonify(response), 400

@app.route('/contacts/delete', methods=['POST'])
def delete_contact():
    data = request.json
    if 'name' in data:
        for contact in contacts:
            if contact['name'] == data['name']:
                contacts.remove(contact)
                response = {
                    'status': 'success',
                    'message': 'Contact deleted successfully'
                }
                return jsonify(response), 200
        response = {
            'status': 'error',
            'message': 'Contact not found'
        }
        return jsonify(response), 404
    else:
        response = {
            'status': 'error',
            'message': 'Invalid data'
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(debug=True)
