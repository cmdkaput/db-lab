"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities
    from .orders.ProductBlueprint import product_bp
    from .orders.StoreBlueprint import store_bp
    from .orders.StoreContactBlueprint import store_contact_bp
    from .orders.OrderStatusBlueprint import order_status_bp
    from .orders.AdressBlueprint import adress_bp
    from .orders.BrandBlueprint import brand_bp
    from .orders.OrderBlueprint import order_bp
    from .orders.CategoryBlueprint import category_bp
    from .orders.CustomerBlueprint import customer_bp
    from .orders.ReviewBlueprint import review_bp
    from .orders.OrderItemBlueprint import order_item_bp
    from .orders.OrdersHasOrderItemsBlueprint import orders_has_order_items_bp

    # Register each blueprint with the app
    app.register_blueprint(product_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(store_contact_bp)
    app.register_blueprint(order_status_bp)
    app.register_blueprint(adress_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(order_item_bp)
    app.register_blueprint(orders_has_order_items_bp)
