import grpc
import logging
from concurrent import futures

import posts_pb2    
import posts_pb2_grpc

from posts import fake_post

class PostsServiceServicer(posts_pb2_grpc.PostsServiceServicer):
    
    def GetPosts(self, request, context):
        num_posts = 100
        posts = [fake_post() for _ in range(num_posts)]
        posts_messages = [posts_pb2.Post(id=post["id"], user_id=post["user_id"], text=post["text"]) for post in posts]
        return posts_pb2.PostsReply(posts=posts_messages)


logging.basicConfig()
print("trying to start server...")

# https://grpc.io/docs/languages/python/basics/
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
posts_pb2_grpc.add_PostsServiceServicer_to_server(PostsServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("gRPC server for PostsService started on port 50051")
server.wait_for_termination()
