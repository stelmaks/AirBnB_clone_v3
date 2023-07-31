#!/usr/bin/python3
"""Module containing views
"""

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status of application
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Retrieve count of objects in storage
    """
    from models.amenity import Amenity
    from models.review import Review
    from models.state import State
    from models.user import User
    from models.city import City
    from models.place import Place
    

    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review,
               "states": State, "users": User}
    json_dict = {}

    for name, cls in classes.items():
        json_dict.update({name: storage.count(cls)})

    return jsonify(json_dict)
