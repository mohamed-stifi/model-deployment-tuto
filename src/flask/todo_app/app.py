from flask import Flask, jsonify, request, Response
from todo import Todo


app = Flask(__name__)

URL = "/todo/api/v1.0"


@app.route(f"{URL}/all", methods=["GET"])
def get_all() -> Response:

    res = {}

    res["tasks"] = [task.to_dict() for task in Todo.all()]
    res["count"] = Todo.count()

    return jsonify(res)


@app.route(f"{URL}/task", methods=["GET"])
def get_task_by_id() -> Response:

    res = {}

    id = request.args.get("id")
    if not id: id = 0 

    res["tasks"] = [Todo.get(id), ]

    return jsonify(res)

    

if __name__ == "__main__":

    Todo.create_task(title = "some title", desc = "some desc", done = False)
    Todo.create_task(title = "title 2", desc ="desc 2", done = False)

    app.run(debug=True)