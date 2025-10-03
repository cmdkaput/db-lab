# Orders DB imports for DAOs corresponding to each entity, using HelloWorld naming
from .orders.ReviewDao import ReviewDAO
from .orders.StoreContactDao import StoreContactDAO
from .orders.StoreDao import StoreDAO
from .orders.OrdersHasOrderItemsDao import OrdersHasOrderItemsDAO
from .orders.AdressDao import AdressDAO
from .orders.CategoryDao import CategoryDAO
from .orders.OrderItemDao import OrderItemDAO
from .orders.BrandsDao import BrandDAO
from .orders.CustomerDao import CustomerDAO
from .orders.ProductDao import ProductDAO
from .orders.OrderStatusDao import OrderStatusDAO
from .orders.OrderDao import OrderDAO

# Initialize DAOs for each entity with HelloWorld naming style
reviewDao = ReviewDAO()
storeContactDao = StoreContactDAO()
storeDao = StoreDAO()
ordersHasOrderItemsDao = OrdersHasOrderItemsDAO()
adressDao = AdressDAO()
categoryDao = CategoryDAO()
orderItemDao = OrderItemDAO()
brandDao = BrandDAO()
customerDao = CustomerDAO()
productDao = ProductDAO()
orderStatusDao = OrderStatusDAO()
orderDao = OrderDAO()
