from flask import Flask, jsonify, request, render_template
from flask_api import status

app = Flask(__name__)


# List of widgets
widgets = [
    {
        "widget_id": 1,
        "widget_name": "Test Widget",
        "description": "Description"
    }
]


# Display the home page
# https://dev.rackspace.example.com/
@app.route('/')
def home():
    return render_template('index.html')


"""
Execution Result:
-----------------
curl -i -X GET  http://127.0.0.1:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 213
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Mon, 03 Dec 2018 14:08:25 GMT

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Accion: Python SDET Hirevue</title>
    </head>

    <body>
        <h1>Solution for Q5 (REST API)</h1>
    </body>
</html>
"""


# GET: Get all widgets
# https://dev.rackspace.example.com/widgets
"""
GET: Get all widgets
    Response:
    Code: 200 if successful, 400 if not
    Type: JSON
        Example:
        [
            {
                "widget_id" : 1,
                "widget_name": "Test Widget",
                "description": "Description"
            }
        ]
"""


@app.route('/widgets', methods=['GET'])
def get_all_widgets():

    if widgets:
        # Return the widgets in JSON format
        content = jsonify({'widgets': widgets})
        return content, status.HTTP_200_OK
    else:
        # Return 400
        content = jsonify({"GET_FAILED": "No widgets found"})
        return content, status.HTTP_400_BAD_REQUEST


"""
Execution Result:
curl -i -X GET  http://127.0.0.1:5000/widgets
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 130
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Mon, 03 Dec 2018 14:10:58 GMT

{
  "widgets": [
    {
      "description": "Description",
      "widget_id": 1,
      "widget_name": "Test Widget"
    }
  ]
}
"""


# POST: Create a new widget
# https://dev.rackspace.example.com/widgets
"""
POST: Create a new widget
    Request:
        Type: JSON
        Header: X-Auth-Token
            Example:
            {
                "widget_name": "Test Widget",
                "description": "Description"
            }
    Response:
        Code: 201 if successful, 400 if not
        Type: JSON
            Example:
            {"widget_id": 1}
"""


@app.route('/widgets', methods=['POST'])
def create_new_widget():

    # Read the 'widget_id', 'widget_name' & 'description'
    request_data = request.get_json()

    # If 'widget_id' not provided, generate one by incrementing the last widgets's ID
    try:
        new_widget_id = request_data['widget_id']
    except KeyError:
        new_widget_id = (widgets[-1])['widget_id'] + 1

    new_widget = {
        "widget_id": new_widget_id,
        "widget_name": request_data['widget_name'],
        "description": request_data['description']
    }

    # Preserve the old count of widgets
    old_count = len(widgets)
    # Append the newly created widget to the widgets list
    widgets.append(new_widget)

    if len(widgets) == (old_count + 1):
        # Return the newly created widget in JSON format
        content = jsonify(new_widget)
        return content, status.HTTP_201_CREATED
    else:
        # Return 400
        content = jsonify({"POST_FAILED": "Failed to create new widget"})
        return content, status.HTTP_400_BAD_REQUEST


"""
Execution Result:
curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets 
-d "{\"widget_name\": \"Test Widget\", \"description\": \"Description\"}"
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 87
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Mon, 03 Dec 2018 14:26:01 GMT

{
  "description": "Description",
  "widget_id": 2,
  "widget_name": "Test Widget"
}


curl -i -X GET  http://127.0.0.1:5000/widgets
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 239
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Mon, 03 Dec 2018 14:26:30 GMT

{
  "widgets": [
    {
      "description": "Description",
      "widget_id": 1,
      "widget_name": "Test Widget"
    },
    {
      "description": "Description",
      "widget_id": 2,
      "widget_name": "Test Widget"
    }
  ]
}

"""


# GET: Get a single widget
# https://dev.rackspace.example.com/widgets/{widget_id}
"""
GET: Get a single widget
    Response:
        Code: 200 if successful, 400 if not
        Type: JSON
            Example:
            {
                "widget_id" : 1,
                "widget_name": "Test Widget",
                "description": "Description"
            }
"""


@app.route('/widgets/<int:widget_id>', methods=['GET'])
def get_single_widget(widget_id):

    # Iterate through the widgets list to find widget with the mentioned 'widget_id'
    for widget in widgets:
        if widget['widget_id'] == widget_id:

            # If found, return the widget in JSON format
            content = jsonify(widget)
            return content, status.HTTP_200_OK

    else:
        # Return an error message, if the widget in not found
        content = jsonify({'GET_FAILED': f"Widget with mentioned ID '{widget_id}' not found"})
        return content, status.HTTP_400_BAD_REQUEST


"""
Execution Result:
curl -i -X GET  http://127.0.0.1:5000/widgets/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 87
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Mon, 03 Dec 2018 15:00:57 GMT

{
  "description": "Description",
  "widget_id": 1,
  "widget_name": "Test Widget"
}

curl -i -X GET  http://127.0.0.1:5000/widgets/3
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 57
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Mon, 03 Dec 2018 15:01:00 GMT

{
  "GET_FAILED": "Widget with mentioned ID not found"
}

"""


# PUT: Update an existing widget
# https://dev.rackspace.example.com/widgets/{widget_id}
"""
PUT: Update an existing widget
    Request:
        Type: JSON
        Header: X-Auth-Token
            Example:
            {
                "description": "A new description"
            }
    Response:
        Code: 204 if successful, 400 if not
"""


@app.route('/widgets/<int:widget_id>', methods=['PUT'])
def update_single_existing_widget(widget_id):

    # Iterate through the widgets list to find widget with the mentioned 'widget_id'
    for widget in widgets:
        if widget['widget_id'] == widget_id:

            # Update the description
            widget['description'] = "A new description"

            # Response doesn't contain any body
            content = jsonify("")
            return content, status.HTTP_204_NO_CONTENT

    else:
        # Return an error message, if the widget in not found
        content = jsonify({'PUT_FAILED': f"Widget with mentioned ID '{widget_id}' not found"})
        return content, status.HTTP_400_BAD_REQUEST


"""
Execution Result:
curl -i -X PUT -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/4 
-d "{\"description\": \"A new description\"}"
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Content-Length: 0
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Tue, 04 Dec 2018 02:59:19 GMT

curl -i -X PUT -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/14 
-d "{\"description\": \"A new description\"}"
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 62
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Tue, 04 Dec 2018 03:01:09 GMT

{
  "PUT_FAILED": "Widget with mentioned ID '14' not found"
}

"""


# DELETE: Delete a widget
"""
DELETE: Delete a widget
    Request:
        Header: X-Auth-Token
    Response:
        Code: 204 if successful, 400 if not
"""


@app.route('/widgets/<int:widget_id>', methods=['DELETE'])
def delete_single_widget(widget_id):

    # Iterate through the widgets list to find widget with the mentioned 'widget_id'
    for widget_index, widget in enumerate(widgets):
        if widget['widget_id'] == widget_id:

            # Once widget is found, remove that element from the list
            widgets.remove(widgets[widget_index])

            # Response doesn't contain any body
            content = jsonify("")
            return content, status.HTTP_204_NO_CONTENT

    else:
        # Return an error message, if the widget in not found
        content = jsonify({'DELETE_FAILED': f"Widget with mentioned ID '{widget_id}' not found"})
        return content, status.HTTP_400_BAD_REQUEST


"""
Execution Result:
curl -i -X DELETE -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/3
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Content-Length: 0
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Tue, 04 Dec 2018 03:28:19 GMT


curl -i -X DELETE -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/13
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 65
Server: Werkzeug/0.12.2 Python/3.6.3
Date: Tue, 04 Dec 2018 03:28:30 GMT

{
  "DELETE_FAILED": "Widget with mentioned ID '13' not found"
}

"""

if __name__ == "__main__":
    app.run(debug=True)
