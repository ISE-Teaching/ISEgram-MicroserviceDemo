import requests
import os
import json
import random
import logging
import pathlib

import grpc
import posts_pb2
import posts_pb2_grpc

from flask import Flask, jsonify, render_template


app = Flask(__name__)
port = int(os.environ.get('PORT', 80))

posts_grpc_url = "posts:50051"
users_url = "http://users"

service_id = random.randrange(1, 100000)    
pod = ""
try:
    pod = pathlib.Path("/etc/hostname").read_text()
except:
    pod = "unknown"

def get_users():
    users = None
    try:
        users_json = requests.get(f"{users_url}/users")
        users = json.loads(users_json.text)
    except requests.exceptions.ConnectionError as e:
        logging.warning("error accessing users aah")
        logging.warning(e)
    return users

def get_posts():
    posts = []
    try:
        channel = grpc.insecure_channel(posts_grpc_url)
        stub = posts_pb2_grpc.PostsServiceStub(channel)
        response = stub.GetPosts(posts_pb2.PostsRequest())
        posts = response.posts
    except grpc.RpcError as e:
        logging.warning("error accessing posts aah")
        logging.warning(e)
    return posts

@app.route("/")
def home():
    posts = get_posts()
    users = get_users()

    if not users:
        return "cannot access users service 😢"

    # convert posts from protobuf objects to dicts
    posts = [{"user_id": post.user_id, "id": post.id, "text": post.text} for post in posts]

    for post in posts:
        post['username'] = "".join([u['username'] for u in users if u['id'] == post['user_id']])

    # return "Hello, this is a Flask Microservice" + html

    return render_template(
        'index.html',
         posts=posts,
         users=users,
         pod=pod,
         )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)

