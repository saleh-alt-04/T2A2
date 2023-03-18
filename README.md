# T2A2: flask api saleh Altamimi

## R1: Identification of the _problem_ you are trying to solve by building this particular _app_?

An e-commerce API (Application Programming Interface) can solve a wide range of problems related to online shopping, such as:

Inventory Management: An e-commerce API can help manage inventory levels by providing real-time updates on product availability, allowing businesses to avoid overselling or running out of stock.
    
 Order Management: E-commerce APIs can manage orders, including tracking orders and providing updates on the status of an order. This can help businesses to streamline their order management process and improve customer service.

## R2 :Why is it a _problem_ that needs solving?

Inventory Management: E-commerce businesses often face challenges with managing their inventory levels, as they need to balance stock levels with demand to avoid stockouts or overstocking. This can result in lost sales, reduced revenue, and poor customer experience. With an e-commerce API that provides real-time inventory updates, businesses can accurately manage their inventory levels, avoid stockouts and overstocking, and provide a positive shopping experience for their customers.
    
Order Management: Efficient order management is essential for businesses to ensure that they fulfill customer orders in a timely manner. Without an effective order management system, businesses may miss orders, delay deliveries, or send incorrect products to customers. This can result in dissatisfied customers, negative reviews, and damage to the business's reputation. With an e-commerce API that provides efficient order management, businesses can ensure that they fulfill customer orders accurately and quickly, resulting in happy customers and repeat business.

## R3 :Why have you chosen this database system. What are the drawbacks compared to others?
SQLite is a lightweight, open-source, embedded relational database management system that is designed for local storage and is often used in small-scale applications such as mobile apps and desktop applications. SQLite is easy to set up and requires minimal configuration, making it a popular choice for developers who want a simple, self-contained database system. SQLite also supports SQL queries, transactions, and multiple concurrent users.

One of the main advantages of SQLite is its simplicity and ease of use. It is a self-contained, serverless database that requires no separate installation or configuration, which makes it easy to set up and use. SQLite is also highly portable and can be used across multiple platforms and operating systems.

However, one of the main drawbacks of SQLite is that it may not be suitable for large-scale applications or those with high concurrency needs, as it does not support multiple writers at the same time. Additionally, SQLite has limited support for advanced features such as stored procedures, triggers, and user-defined functions.

Compared to other database systems, such as MySQL or PostgreSQL, SQLite has fewer features and may not be as scalable or performant for large-scale applications. However, it is a good choice for small-scale projects or applications that require a simple, self-contained database system with minimal configuration requirements.

## R4 Identify and discuss the key functionalities and benefits of an ORM

ORM, or Object-Relational Mapping, is a programming technique that maps object-oriented programming language constructs to relational database structures. The key functionalities and benefits of an ORM are as follows:

1.  Simplified Database Interactions: ORM enables developers to work with databases using object-oriented programming constructs, such as classes and objects, instead of having to write complex SQL queries. This simplifies database interactions and reduces the amount of boilerplate code required to interact with the database.
    
2.  Database Abstraction: ORM provides a layer of abstraction between the application code and the underlying database. This allows developers to work with multiple database systems, such as MySQL, PostgreSQL, and Oracle, without having to learn the specific syntax and quirks of each system.
    
3.  Data Modeling: ORM allows developers to define database schemas using object-oriented programming constructs. This simplifies the process of designing and managing database schemas, as developers can use familiar
programming concepts such as inheritance, encapsulation, and polymorphism to model complex data structures.
    

Overall, the key functionalities and benefits of an ORM include simplified database interactions, database abstraction, data modelling, security and reliability, and performance optimization. ORM can simplify the development process, make database interactions easier, provide better data modelling, improve security, and optimise performance.

## R5 Document all endpoints for your API

## `GET /categories`

  

Retrieves all the categories stored in the database.

  

### Request

  

- Method: GET

- Endpoint: `/categories`

- Headers:

- Content-Type: application/json

  

### Response

  

- Status Code: 200 OK

- Headers:

- Content-Type: application/json

- Body:

jsonCopy code

`{

"categories": [

{

"id": 1,

"name": "Category 1"

},

{

"id": 2,

"name": "Category 2"

},

...

]

}`

  

## `GET /categories/{id}`

  

Retrieves the category with the given ID.

  

### Request

  

- Method: GET

- Endpoint: `/categories/{id}`

- Headers:

- Content-Type: application/json

- URL Parameters:

- id (int): The ID of the category to retrieve.

  

### Response

  

- Status Code: 200 OK

- Headers:

- Content-Type: application/json

- Body:

jsonCopy code

`{

"id": 1,

"name": "Category 1"

}`

  

## `PUT /categories/{id}`

  

Updates the category with the given ID.

  

### Request

  

- Method: PUT

- Endpoint: `/categories/{id}`

- Headers:

- Content-Type: application/json

- URL Parameters:

- id (int): The ID of the category to update.

- Body:

jsonCopy code

`{

"name": "New Category Name"

}`

  

### Response

  

- Status Code: 200 OK

- Headers:

- Content-Type: application/json

- Body:

jsonCopy code

`{

"id": 1,

"name": "New Category Name"

}`

  

## `DELETE /categories/{id}`

  

Deletes the category with the given ID.

  

### Request

  

- Method: DELETE

- Endpoint: `/categories/{id}`

- Headers:

- Content-Type: application/json

- URL Parameters:

- id (int): The ID of the category to delete.

  

### Response

  

- Status Code: 200 OK

- Headers:

- Content-Type: application/json

- Body:

jsonCopy code

`{

"id": 1,

"name": "Category 1"

}`

  

## `POST /delivery`

  

Creates a new delivery for an order.

  

### Request

  

- Method: POST

- Endpoint: `/delivery`

- Headers:

- Content-Type: application/json

- Body:

jsonCopy code

`{

"order_id": 1,

"delivery_date": "2023-03-19",

"address": "123 Main St",

"city": "Anytown",

"state": "CA",

"zipcode": "12345"

}`

  

### Response

  

- Status Code: 200 OK

- Headers:

- Content-Type: application/json

- Body:

jsonCopy code

`{

"id": 1,

"order_id": 1,

"delivery_date": "2023-03-19",

"address": "123 Main St",

"city": "Anytown",

"state": "CA",

"zipcode": "12345",

"delivery_status": "pending"

}`

  

## `GET /delivery`

  

Retrieves all the deliveries stored in the database.

  

### Request

  

- Method: GET

- Endpoint: `/delivery`

- Headers:

- Content-Type: application/json

  

### Response

  

- Status Code: 200 OK

- Headers:

- Content-Type: application/json

- Body:

Copy code

  

# Get single product by ID

  

@product_bp.route('/product/<id>', methods=['GET']) def get_product(id): product = Product.query.get(id) return product_schema.jsonify(product)

  

# Update a product by ID

  

@product_bp.route('/product/<id>', methods=['PUT']) def update_product(id): product = Product.query.get(id)

  

scssCopy code

  

`name = request.json['name']

description = request.json['description']

price = request.json['price']

qty = request.json['qty']

category_id = request.json['category_id']

  

product.name = name

product.description = description

product.price = price

product.qty = qty

product.category_id = category_id

  

db.session.commit()

  

return product_schema.jsonify(product)`

  

# Delete a product by ID

  

@product_bp.route('/product/<id>', methods=['DELETE']) def delete_product(id): product = Product.query.get(id) db.session.delete(product) db.session.commit()

  

kotlinCopy code

  

`return product_schema.jsonify(product)`

  

@user_bp.route('/user', methods=['POST']) def add_user(): name = request.json['name'] email = request.json['email'] password = request.json['password'] address = request.json['address'] city = request.json['city'] state = request.json['state'] zipcode = request.json['zipcode'] country = request.json['country'] new_user = User(name, email, password, address, city, state, zipcode, country)

  

scssCopy code

  

`db.session.add(new_user)

db.session.commit()

  

return user_schema.jsonify(new_user)`

  

# Get all users

  

@user_bp.route('/users', methods=['GET']) def get_users(): all_users = User.query.all() result = users_schema.dump(all_users) return jsonify(result)

  

# Get single user by ID

  

@user_bp.route('/user/<id>', methods=['GET']) def get_user(id): user = User.query.get(id) return user_schema.jsonify(user)

  

# Update a user by ID

  

@user_bp.route('/user/<id>', methods=['PUT']) def update_user(id): user = User.query.get(id)

  

cssCopy code

  

`name = request.json['name']

email = request.json['email']

password = request.json['password']

address = request.json['address']

city = request.json['city']

state = request.json['state']

zipcode = request.json['zipcode']

country = request.json['country']

  

user.name = name

user.email = email

user.password = password

user.address = address

user.city = city

user.state = state

user.zipcode = zipcode

user.country = country

  

db.session.commit()

  

return user_schema.jsonify(user)`

  

# Delete a user by ID

  

@user_bp.route('/user/<id>', methods=['DELETE']) def delete_user(id): user = User.query.get(id) db.session.delete(user) db.session.commit()

  

kotlinCopy code

  

`return user_schema.jsonify(user)`

## R6 An ERD for your _app_

![erd](https://user-images.githubusercontent.com/117635352/226112668-c9133b5c-1ca7-4962-b38b-246a54498c3c.png)


## R7 Detail any third party services that your _app_ will use
    
1.  Flask - Flask is a popular Python web framework that allows developers to quickly create web applications. It is used here to create an instance of the Flask application and define routes for handling incoming requests.
    
2.  SQLAlchemy and Flask-SQLAlchemy - SQLAlchemy is a Python SQL toolkit and Object-Relational Mapping (ORM) library. Flask-SQLAlchemy is a Flask extension that provides integration between Flask and SQLAlchemy, making it easier to use SQLAlchemy within a Flask application. It is used here to define the database schema and manage the database connection.
    
3.  Flask-Marshmallow - Flask-Marshmallow is a Flask extension for object serialization and deserialization. It provides an easy way to convert complex Python objects to JSON, which can be useful when building RESTful APIs. It is used here to define the schema for the product data and serialize/deserialize the data when interacting with the database.
    
4.  Flask-JWT-Extended - Flask-JWT-Extended is a Flask extension that provides JSON Web Token (JWT) authentication support. JWT is a standard for securely transmitting information between parties as a JSON object. It is used here to authenticate requests to the API, ensuring that only authorized users can access the data.

## R8 Describe your projects _models_ in terms of the relationships they have with each other
 A User can have many Orders. This is represented by the user_id foreign key in the Order class.

An Order can have one Product. This is represented by the product_id foreign key in the Order class.

A Category can have many Products. This is represented by the category_id foreign key in the Product class, and the relationship between Category and Product is established by the backref in the Product class.

An Order can have one Delivery. This is represented by the order_id foreign key in the Delivery class.
## R9 Discuss the database relations to be implemented in your application
One user can place many orders, but each order is associated with only one user. Therefore, the User table should have a one-to-many relationship with the Order table. This can be achieved by adding a foreign key column in the Order table that references the id column of the User table.

One order can have multiple products, and each product can belong to multiple orders. This represents a many-to-many relationship between the Order and Product tables. To implement this relationship, a junction table should be created with columns for the order_id and product_id. The order_id column will be a foreign key referencing the id column in the Order table, and the product_id column will be a foreign key referencing the id column in the Product table.

Each product belongs to only one category, but each category can have multiple products. This represents a one-to-many relationship between the Category and Product tables. To implement this relationship, the Product table should have a foreign key column that references the id column in the Category table.

Each order can have only one delivery, but a delivery can be associated with multiple orders. This represents a one-to-many relationship between the Delivery and Order tables. To implement this relationship, the Order table should have a foreign key column that references the id column in the Delivery table.
## R10 Describe the way tasks are allocated and tracked in your project
As a sole developer working on my e-commerce project, I have adopted an Agile approach to manage my tasks effectively. To begin with, I have created a comprehensive backlog of all the features that I need to implement in my app, keeping in mind any dependencies between them.

To keep track of my progress, I use a Trello board where I have arranged the tasks in order of priority and their ability to be completed. The list hierarchy allows me to see which tasks I need to work on first and which ones can wait. I have also added notes to each task, detailing potential challenges or roadblocks I may face while developing them.

Once I start working on a particular feature, I move its corresponding card to the "In Dev" column. After completing the task, I move it to the "Dev Done" column, where it is considered provisionally complete.

Periodically, I revisit the cards in the "Dev Done" column and reassess their status. Depending on the situation, I either move them to the backlog if they require further development, keep them in "Dev Done" if they need more work, or move them to the "Done" column if they are fully completed.

This approach helps me to stay organized and maintain an overview of my progress, ensuring that I am on track to deliver a successful e-commerce app.
