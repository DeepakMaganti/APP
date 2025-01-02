from flask import Blueprint, render_template, jsonify
from flask import request
from .models import Course
from . import db
import json
import os

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    query = request.args.get('query')
    if query:
        courses = Course.query.filter(
            db.or_(
                Course.title.contains(query),
                Course.overview.contains(query)
            )
        ).all()
    else:
        courses = Course.query.all()
    return render_template('course_view.html', courses=courses)

import os

@routes.route('/loaddata')
def loaddata():
    try:
        # Define the file path
        file_path = r"C:\Users\dmaga\OneDrive\Desktop\Deepak\APP\flaskapplication\courses.json"
        # Alternatively, use os.path for cross-platform compatibility:
        # file_path = os.path.join("C:", "Users", "dmaga", "OneDrive", "Desktop", "Deepak", "APP", "flaskapplication", "courses.json")

        # Open and load the JSON file
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            courses = json.load(f)

        # Rest of your code for processing courses...
        for course in courses:
            missing_keys = [k for k in ('title', 'author', 'overview', 'img', 'url', 'free') if k not in course]
            if missing_keys:
                print(f"Missing keys: {missing_keys} in course: {course}")
                return jsonify({"error": "Invalid JSON format. Missing keys.Missing keys: {missing_keys} in course: {course}"}), 400

            new_course = Course(
                title=course['title'],
                author=course['author'],
                overview=course['overview'],
                image=course['img'],
                url=course['url']
            )
            db.session.add(new_course)

        db.session.commit()
        return jsonify({"message": "Data loaded successfully"}), 200

    except FileNotFoundError:
        return jsonify({"error": f"File not found: {file_path}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

