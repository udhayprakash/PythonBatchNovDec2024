# gRPC


RPC - remote procedure call

functions are called procedure/routine

## comparision

### protocols

    xmlrpc, jsonrpc go with http
    restapi with http 1.1, come are with http/2

    grpc http/2

### Serialization

    xmlrpc uses xml 
    jsonrpc uses json
    REST API -- json/xml/OData

    gRPC - Employs Protocol Buffers (protobuf) for efficient binary serialization
         - smaller message sizes and faster processing
            .proto

### directiona
    xmlrpc/jsonRPC doesnt support streaming
    RESTAPI suports with streaming, but only one directional

    gRPC supports bidirectional streaming



# Installation

    pip install grpcio grpcio-tools

## Process 

Step 1: create an `addition.proto` file

Step 2: run 

    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. addition.proto
