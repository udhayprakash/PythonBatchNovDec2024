- REST
---------
- REST stands for REpresentational State Transfer
- It's principles are:
	- It should be stateless
	- It should access all the resources from the server using only URI
	- It does not have inbuilt encryption
	- It does not have session
	- It uses one and only one protocol - HTTP
	- For CRUD operations, it should use HTTP methods like
		GET  - to retrieve one or more records
		POST - to create record
		PUT  - to update an existing record
		PATCH- to update a specific column in existing record
		DELETE- to delete a record

		HEAD - response identical to GET, but without response body
		CONNECT- establishes a tunnel to server identifier by the target resource
		OPTIONS- used to describe the communication options for the target resource.
		TRACE- performs a message loop-back test along the path to the target resource.
		PATCH- used to apply partial modifications to a resource

	- response can be JSON or XML, atom, OData etc.

	Idempotence - If something is idempotent, then no matter how many times you do it, the result will always be the same.
	1. POST is NOT idempotent.
	2. GET, PUT, DELETE, HEAD, OPTIONS and TRACE are idempotent.
	Nulipotent- GET is so because nothing is added or changed, except logging.

- PATCH operations
	add		: Adds a new value to the resource.
	remove	: Removes a value from the resource.
	replace	: Replaces the value of a property.
	move	: Moves a property to a new location.
	copy	: Copies a property to a new location.
	test	: Tests whether a property has a particular value.

- Header locations in REST API
	- Request headers: Request headers are typically sent with the request, before the body of the request.
		- Contains request information like
			- type of content
			- the caching policy, and
			- the authentication credentials .
	- Response headers: Response headers are sent with the response, after the body of the response.
		- Contains response information like
			- type of content,
			- the caching policy, and
			- the status code

- REST API with large data
	- Pagination as query parameter like page=1 and pagesize=100
	- offset parameter specifies the number of records to skip before returning the response

- REST based vs RESTFUL
	- REST based services follow some of the above principles and not all
	- RESTFUL services means it follows all the above principles.

- Richardson-maturity-model
	- to know level of RESTful your API is.
	- https://developers.redhat.com/blog/2017/09/13/know-how-restful-your-api-is-an-overview-of-the-richardson-maturity-model

- Best practice for RESTful API design is that
	- path params are used to identify a specific resource or resources,
	  while query parameters are used to sort/filter those resources.
	- We shouldn’t use verbs in our endpoint paths. Instead, we should use the nouns which represent the entity that the endpoint that we’re retrieving or manipulating as the pathname.
	- Use logical nesting on endpoints
		-  If one object can contain another object, you should design the endpoint to reflect that.
		- say, there were articles, and comments for each article, then use "/articles/:articleId/comments"
		- also, suppose to return the author of particular comments, we can use /articles/:articleId/comments/:commentId/author
	- Handle errors gracefully and return standard error codes
	- Allowing filtering, sorting, and pagination
		- /employees?lastName=Smith&age=30
		- http://example.com/articles?sort=+author,-datepublished
			- + means ascending and - means descending
			-  author’s name in alphabetical order
			- datepublished from most recent to least recent
	- Cache data to improve performance, using  Redis or in-memory caching
	- Versioning our APIs, like /v1/, /v2/, etc.


- REST Design Patterns
	1) Layered Architecture
		- will improve system scalability and security
		- When client and server doesnt know about any intermediaries, we can place
		proxy or load balancer, and improve scalability.
		Also, adding separate layer of security enhances system safety
	2) Caching
		- results in low server latency, increase in app speed and responsiveness
	3) Stateless interactions
		- results in enhanced performance, app reliability
	4) Adding Common parameters to API, like
		Filtering - to filter the payload size, by filtering on multiple fields
			GET /users?age=30

		Pagination - will help, ease the burden of overloading either client or server
			- Also, previous and next page links can be provided in the link
			GET /users?page=3&results_per_page=20

		Sorting - will help to sort the payload based on one or more fields
			GET /users?sort_by=first_name&order=asc

API documentation tools
=======================
	- Swagger was used for most of the time.
	- Earlier used RAML (RESTful API Modeling Language)

CORS
=====
	- CORS means Cross-origin resource sharing
	- Its a security mechanism that blocks web pages from accessing resources from a different domain, by default.
	- It enables the browser to check with the server and receive permission to access the requested resource based on the security policy configured on the server.

REST vs SOAP
=============
	RESTful supports JSON, XML,
		SOAP supports only XML
	REST is faster than SOAP based web services
		SOAP is more secure
	REST allows a greater variety of data formats,
		SOAP only allows XML.

	1) SOAP
		- Communication happens using XML only
		- Request is sent to SOAP methods
		- Documentation is in WSDL (Wizdal)
		- Heavy, more secure, more stable
		- getting less popular
	2) REST API
		- Communication happens using Json, XML
		- Requests are sent to API methods/urls using
		- Communication happens in HTTP(Internet)
		- Lightweight, stable
		- Easy to develop and automate
		- very popular

Authentication vs authorisation
================================
	- Authentication is validating the user.
	- Authorization is Validating the role of valid user.
	- Simple Analogy is that in the company office only employees (means valid people) can enter.
		But only few people can access secured rooms.

API Authentication
===================
	1) HTTP Authentication
		- Basic HTTP Auth
			- where we send credentials to server, in http header. so less secure.
		- Bearer HTTP Auth
			- where we send a token to the server. Eg: Authorization: Bearer <Token>
		- JWT (Json Web Token)
			- It gives user-level access
			- Also, contains additional information like expiration date, user's uniqueID, ...
	2) API Keys
		- its a long unique code used to access APIs
		- used for both authentication of users and tracking usage statistics.
	3) OAuth
		- provides a way for users to grant 3rd party access to their web resources
		  without sharing their passwords.
		- oauth providers can be social logins like facebook, google, twitter, ...
		- Also, we can create using AWS Cognito

		openID - facebook, google, twitter, etc

OAuth
======
	OAuth is an open-standard authorization protocol or framework that provides applications the ability for “secure designated access.”
	OAuth doesn’t share password data but instead uses authorization tokens to prove an identity between consumers and service providers.

	OAuth is about authorization and not authentication. Authorization is asking for permission to do stuff. Authentication is about proving you are the correct person because you know things. OAuth doesn’t pass authentication data between consumers and service providers – but instead acts as an authorization token of sorts.

	OAuth transaction has THREE parts - the user, the consumer, and the service provider.

	Ex: If user wants to access a website using Oauth Provider, like facebook.

	Step 1: User will come to the website, click on facebook login.
	Step 2: The application will redirect the user, to facebook for authorization.
	Step 3: Facebook, which is the Oauth provider, will validate the user, and the website too.
		Means Invalid user cant access the website.
		Also, user is protected from accessing a Phising Website( which is similar to Original Website)

		Finally, after validation, Oauth provider will reply token, with some expiry time.
	Step 4: So, from then, user will access the website using that token, for the given time.

	OAuth Servers can choose their token format; but mostly JSON Web Token (JWT) is choosen.

OAuth vs OAuth2
===============
	OAuth 2.0 is a complete redesign from OAuth 1.0, and the two are not compatible.
	OAuth 1.0 is deprecated now.

	OAuth 2.0 is faster and easier to implement.
	OAuth 1.0 used complicated cryptographic requirements, only supported three flows, and did not scale.

	OAuth 2.0 has six flows for different types of applications and requirements and enables signed secrets over HTTPS.
	OAuth tokens no longer need to be encrypted on the endpoints in 2.0 since they are encrypted in transit.


SAML
====
	SAML means Security Assertion Markup Language
	It is an alternative federated authentication standard that many enterprises use for Single-Sign On (SSO).
	SAML enables enterprises to monitor who has access to corporate resources.

SAML vs OAuth
=============
	SAML uses XML to pass messages, and OAuth uses JSON.
	OAuth uses API calls extensively, so, suitable for mobile applications, modern web applications, game consoles, and Internet of Things (IoT) devices.
	Whereas SAML drops a session cookie in a browser that allows a user to access certain web pages - great for short-lived web pages.


OAuth vs JWT
============
	- OAuth 2.0 defines a protocol, i.e. specifies how tokens are transferred,
	  JWT defines a token format.
	- OAuth 2.0 and "JWT authentication" have similar appearance when it comes
	  to the (2nd) stage where the Client presents the token to the Resource Server:
	  the token is passed in a header.
	- But "JWT authentication" is not a standard and does not specify how the Client
	  obtains the token in the first place (the 1st stage).
	  That is where the perceived complexity of OAuth comes from: it also defines
	  various ways in which the Client can obtain an access token from something
	  that is called an Authorization Server.
	- So, JWT is just a token format, OAuth 2.0 is a protocol (that may use a
	  JWT as a token format).


JWT (JSON Web Tokens)
	- It is just a token format. JWT tokens are JSON encoded data structures contains
	information about issuer, subject (claims), expiration time etc.
	- It is signed for tamper proof and authenticity and it can be encrypted to
	protect the token information using symmetric or asymmetric approach.
	- JWT is simpler than SAML 1.1/2.0 and supported by all devices and it is more
	powerful than SWT(Simple Web Token).

	- sections of a JSON Web Token (JWT):
		1) Header: The header contains the type of token (JWT), the hashing algorithm used to sign the token, and the token's kid (key ID).
		2) Payload: The payload contains the claims, which are the data that is being transmitted. The claims can be anything, but they are typically used to represent the identity of the user, the time the token was issued, and the time the token expires.
		3) Signature: The signature is used to verify the authenticity of the token. It is calculated using the header, the payload, and a secret key.

OAuth2
	- OAuth2 solve a problem that user wants to access the data using client
	 software like browse based web apps, native mobile apps or desktop apps.
	- OAuth2 is just for authorization, client software can be authorized to
	 access the resources on-behalf of end user using access token.

OpenID Connect
	- OpenID Connect builds on top of OAuth2 and add authentication.
	- OpenID Connect add some constraint to OAuth2 like UserInfo Endpoint,
	  ID Token, discovery and dynamic registration of OpenID Connect providers
	  and session management.
	- JWT is the mandatory format for the token.

CSRF protection
	- we don't need implement the CSRF protection if you do not store token
	  in the browser's cookie.



REST features
=============
	- Performance
		— best suited for systems requiring rapid iteration and HTTP standardized verbiage,
	- Scalability
		— allows the support of large numbers of components and interactions among them,
	- Simplicity
		— REST has a uniform interface which simplifies and decouples the architecture,
	- Modifiability
		— components can be modified to fit changing needs even while the application is running.


GraphQL features
================
	- Adaptability
		— the client decides what data they want, how they want it and what format they
          want to get it in,
	- Efficiency
		— delivers exactly what the client requests without over fetching,
	- Flexibility
		— GraphQl is cross-platform and supports more than a dozen languages (Perl, Java,
          Python, PHP among others).

	- My experince
		- worked with GraphQL using AWS AppSync, and with python module, strawberry-graphql
	- Why GraphQL
		- when we give REST API, if the user is interested in part of data from, say,
		  three endpoints, then they will collective all the data and filter what they need
		- It is resource exhaustive from both serving and consuming sides.
		- If the user has the flexibility to customize the feed as per their need, then
		  we can exactly send the data, as needed.
		- That is the main reason for moving from REST API, to GraphQL

GRPC features
=============
	- Lightweight and quick system for requesting data
	- RPC functions on contracts, the negotiation is defined by the relationship
    	between the server and the client not by the architecture.
	  Most of the power relies on the client-side while handling and computations
	  are offloaded to a remote server hosting the resource.

	- lightweight
		- requires very little resources which makes it a handy solution for even
		extremely low powered situations
	- efficient
		- gPRC uses protobufs, a method of serializing structured data which focuses
		on serializing communication in an effective manner
	- open-source
	- Mainly suited for systems where requester is low power or want to preserve resources.
	- suitable for IoT devices like voice controllers, smart light switches,
	  smock alarm locks, cameras.


MicroService vs Web Service
----------------------------
	- microservice is a small, independent, application that performs a highly focused service
	  as well as possible.
	- web service is an internet-based interface that makes the "services" of one application
	  available to applications running on different platforms.


HTTP Status Codes
==================
	Informational responses (100–199)
		100 Continue
		101 Switching Protocols
		102 Processing (WebDAV)
		103 Early Hints

	Successful responses (200–299)
		200 OK
		201 Created
		202 Accepted
		203 Non-Authoritative Information
		204 No Content
		205 Reset Content
		206 Partial Content
		207 Multi-Status (WebDAV)
		208 Already Reported (WebDAV)
		226 IM Used (HTTP Delta encoding)

	Redirection messages (300–399)
		300 Multiple Choices
		301 Moved Permanently
		302 Found
		303 See Other
		304 Not Modified
		305 Use Proxy
		306 unused
		307 Temporary Redirect
		308 Permanent Redirect

	Client error responses (400–499)
		400 Bad Request
		401 Unauthorized
		402 Payment Required
		403 Forbidden
		404 Not Found
		405 Method Not Allowed
		406 Not Acceptable
		407 Proxy Authentication Required
		408 Request Timeout
		409 Conflict
		410 Gone
		411 Length Required
		412 Precondition Failed
		413 Payload Too Large
		414 URI Too Long
		415 Unsupported Media Type
		416 Range Not Satisfiable
		417 Expectation Failed

		429 Too Many Requests
		431 Request Header Fields Too Large
		451 Unavailable For Legal Reasons

	Server error responses (500–599)
		500 Internal Server Error
		501 Not Implemented
		502 Bad Gateway
		503 Service Unavailable
		504 Gateway Timeout
		505 HTTP Version Not Supported
		506 Variant Also Negotiates
		507 Insufficient Storage (WebDAV)
		508 Loop Detected (WebDAV)
		510 Not Extended
		511 Network Authentication Required


401 vs 403

	401 Unauthorized is the status code to return when the client provides no credentials or invalid credentials.
	403 Forbidden is the status code to return when a client has valid credentials but not enough privileges to perform an action on a resource.

cookie
	- cookies have three primary purposes
		1) Tracking
			- Tracking builds statistics about the user, and this data can be used for AD personalization.
		2) Session Management
			- Cookies store data from sites so that when you return, your changes are kept.
			- Ex: Items you put into a shopping cart, or login information.
		3) Personalization
			- Cookies can also retain data on user preferences such as languages, themes, location, and layout.

	- How cookies work
		- Step 1: Server sets cookies by adding a set-cookie header to the HTTP response
				This set-cookie value allows a server to identify each unique client user.
		- Step 2: Then, client's browser attaches a cookie header with the value sent by the server in set-cookie.

		- This process repeats for every request, till session time-out.


- API Integration
------------------




- What happens after typing a URL into the browser?
------------------------------------------------------
	1. The user prompts the URL into the browser and press Enter.
		The URL includes a scheme, the website's domain name, and a resource path.

	2. The browser uses a domain name system (DNS) lookup to determine the IP address for the domain.
		Data can be cached at several levels to speed up the lookup process.
		For example, it can be cached in the browser cache or in the ISP cache.
		The browser gets the IP address from the DNS servers if it is not yet cached.

	3. The browser establishes a TCP connection with the server and sends an HTTP request to it.

	4. The server processes the request,
			within the application server,
				first, Validate the data in the request
				then, Validated the authenticity of the request
				and finally, sends back the response

	5. When a successful response with status code 200 is received, the browser renders the HTML content.