import grpc
import addition_pb2
import addition_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = addition_pb2_grpc.AdderStub(channel)
        response = stub.Add(addition_pb2.AddRequest(a=3, b=5))
        print(f'The sum of 3 and 5 is: {response.result}')

if __name__ == '__main__':
    run()