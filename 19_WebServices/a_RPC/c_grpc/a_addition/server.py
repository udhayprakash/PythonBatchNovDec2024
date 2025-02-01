from concurrent import futures
import grpc
import addition_pb2
import addition_pb2_grpc


class AdderServicer(addition_pb2_grpc.AdderServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return addition_pb2.AddResponse(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addition_pb2_grpc.add_AdderServicer_to_server(AdderServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()