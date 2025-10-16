import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    _init_swagger(app)
    _init_docs(app)

    return app


def _init_swagger(app: Flask) -> None:
    # A-lia Swagger
    restx_api = Api(app, title='My test backend',
                    description='A simple backend')  # https://flask-restx.readthedocs.io/

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


def _init_docs(app: Flask) -> None:
    def _generate_openapi_spec(server_url: str = "/"):
        spec = {
            "openapi": "3.0.3",
            "info": {
                "title": "Shop API",
                "version": "1.0.0",
                "description": "Auto-generated docs for existing endpoints.",
            },
            "servers": [{"url": (server_url or '/').rstrip('/') or '/'}],
            "paths": {},
            "components": {
                "schemas": {
                    "Id": {"type": "integer", "format": "int32", "minimum": 1, "example": 1},
                }
            },
        }
#1234
        def add_collection(path: str, plural: str):
            spec["paths"][path] = {
                "get": {"summary": f"List {plural}", "responses": {"200": {"description": "OK"}}},
                "post": {
                    "summary": f"Create {plural[:-1] if plural.endswith('s') else plural}",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"type": "object", "additionalProperties": True},
                                "example": {"key": "value"}
                            }
                        }
                    },
                    "responses": {"201": {"description": "Created"}},
                },
            }

        def add_by_id(path: str, singular: str):
            spec["paths"][path] = {
                "get": {
                    "summary": f"Get {singular} by id",
                    "parameters": [{"in": "path", "name": "id", "required": True, "schema": {"$ref": "#/components/schemas/Id"}}],
                    "responses": {"200": {"description": "OK"}, "404": {"description": "Not Found"}},
                },
                "put": {
                    "summary": f"Update {singular}",
                    "parameters": [{"in": "path", "name": "id", "required": True, "schema": {"$ref": "#/components/schemas/Id"}}],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"type": "object", "additionalProperties": True},
                                "example": {"key": "new value"}
                            }
                        }
                    },
                    "responses": {"200": {"description": "Updated"}},
                },
                "delete": {
                    "summary": f"Delete {singular}",
                    "parameters": [{"in": "path", "name": "id", "required": True, "schema": {"$ref": "#/components/schemas/Id"}}],
                    "responses": {"204": {"description": "No Content"}},
                },
            }

        # CRUD endpoints inferred from blueprints
        add_collection("/product", "products")
        add_by_id("/product/{id}", "product")

        add_collection("/category", "categories")
        add_by_id("/category/{id}", "category")

        add_collection("/customer", "customers")
        add_by_id("/customer/{id}", "customer")

        add_collection("/store", "stores")
        add_by_id("/store/{id}", "store")

        add_collection("/store_contact", "store contacts")
        add_by_id("/store_contact/{id}", "store contact")

        add_collection("/order_status", "order statuses")
        add_by_id("/order_status/{id}", "order status")

        add_collection("/brand", "brands")
        add_by_id("/brand/{id}", "brand")

        add_collection("/review", "reviews")
        add_by_id("/review/{id}", "review")

        add_collection("/order_item", "order items")
        add_by_id("/order_item/{id}", "order item")

        add_collection("/order", "orders")
        add_by_id("/order/{id}", "order")

        # Composite relation
        spec["paths"]["/orders_has_order_items"] = {
            "get": {"summary": "List order-item relations", "responses": {"200": {"description": "OK"}}},
            "post": {
                "summary": "Create order-item relation",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"type": "object", "additionalProperties": True},
                            "example": {"order_id": 1, "order_item_id": 1}
                        }
                    }
                },
                "responses": {"201": {"description": "Created"}},
            },
            "delete": {
                "summary": "Delete order-item relation (composite)",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["order_id", "order_item_id"],
                                "properties": {"order_id": {"type": "integer"}, "order_item_id": {"type": "integer"}},
                            },
                            "example": {"order_id": 1, "order_item_id": 1}
                        }
                    },
                },
                "responses": {"204": {"description": "No Content"}, "400": {"description": "Bad Request"}},
            },
        }

        return spec

    @app.get('/openapi.json')
    def openapi_spec():
        server_url = app.config.get('SERVER_NAME', '/') or '/'
        return jsonify(_generate_openapi_spec(server_url))

    @app.get('/docs')
    def swagger_ui():
        return (
            """
<!doctype html>
<html>
  <head>
    <meta charset=\"utf-8\"/>
    <title>API Docs</title>
    <link rel=\"stylesheet\" href=\"https://unpkg.com/swagger-ui-dist@5/swagger-ui.css\" />
  </head>
  <body>
    <div id=\"swagger\"></div>
    <script src=\"https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js\"></script>
    <script>
      window.ui = SwaggerUIBundle({ url: '/openapi.json', dom_id: '#swagger' });
    </script>
  </body>
</html>
""",
            200,
            {"Content-Type": "text/html; charset=utf-8"},
        )

def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    # Ensure dependent models are loaded before creating tables (FKs resolution)
    from my_project.auth.domain.orders.Order import Order  # noqa: F401
    from my_project.auth.domain.orders.OrderItem import OrderItem  # noqa: F401
    from my_project.auth.domain.orders.OrdersHasOrderItems import OrdersHasOrderItems  # noqa: F401
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password (kept for compatibility if format placeholders are used)
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])

    uri = app_config[SQLALCHEMY_DATABASE_URI]
    # If URI contains placeholders, format them, else leave as-is
    try:
        if '{' in uri and '}' in uri:
            uri = uri.format(root_user, root_password)
    except Exception:
        # Fallback to original URI
        pass

    # Ensure SSL for Azure MySQL and robust connection handling
    if uri.startswith("mysql://") and "ssl_mode=" not in uri:
        separator = '&' if '?' in uri else '?'
        uri = f"{uri}{separator}ssl_mode=REQUIRED"

    app_config[SQLALCHEMY_DATABASE_URI] = uri
    # Enable pool_pre_ping to revive stale connections
    app_config.setdefault('SQLALCHEMY_ENGINE_OPTIONS', {})
    app_config['SQLALCHEMY_ENGINE_OPTIONS']['pool_pre_ping'] = True
