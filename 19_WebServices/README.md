# WebServices

Machine to Machine communication
    protocols


## Types of WebServices

1) FTP (File Transfer Protocol):
    - Used for transferring files between client and server.
    - Supports operations like uploading, downloading, and managing files on servers.
    - Advanced
        - SFTP (SSH File Transfer Protocol):
        - FTPS (FTP Secure):

2) RPC
    XML-RPC:
        A remote procedure call protocol that uses XML to encode calls.
        Allows communication between different systems.

    JSON-RPC:
        Similar to XML-RPC but uses JSON for message formatting.
        Enables remote procedure calls with ease of use.

    gRPC:
        A modern open-source RPC framework that uses HTTP/2 for transport.
        Supports multiple programming languages and uses Protocol Buffers for serialization.


2) SOAP Web Services:
    Use the Simple Object Access Protocol (SOAP) for communication.
    Rely on XML for message format and support WS-* standards for security.

3) RESTful Web Services:
    Use Representational State Transfer (REST) architecture.
    Typically utilize HTTP methods (GET, POST, PUT, DELETE) and can return various formats (JSON, XML).

4) GraphQL:
    A query language for APIs that allows clients to request specific data.
    Uses a single endpoint for all interactions, providing more flexibility than REST.

WebSocket Services:
    Provides full-duplex communication channels over a single TCP connection.
    Ideal for real-time applications like chat and notifications.
Microservices:
    An architectural style that structures applications as a collection of small, loosely coupled services.
    Each service is independently deployable and communicates over APIs.
Serverless Web Services:
    Focus on running code in response to events without managing servers.
    Often associated with cloud services (e.g., AWS Lambda).
Streaming Services:
    Used for transmitting continuous data streams, often seen in media services (e.g., video streaming).
