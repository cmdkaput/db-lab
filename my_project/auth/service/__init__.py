# Import services using HelloWorld naming convention
from .orders.StoreService import StoreService
from .orders.OrderStatusService import OrderStatusService
from .orders.StoreContactService import StoreContactService
from .orders.OrderHasOrderItemsService import OrdersHasOrderItemsService
from .orders.AdressService import AdressService
from .orders.ProductService import ProductService
from .orders.ReviewService import ReviewService
from .orders.BrandService import BrandService
from .orders.CategoryService import CategoryService
from .orders.CustomerService import CustomerService
from .orders.OrderItemService import OrderItemService
from .orders.OrderService import OrderService

# Initialize service instances with HelloWorld naming style
storeService = StoreService()
reviewService = ReviewService()
storeContactService = StoreContactService()
ordersHasOrderItemsService = OrdersHasOrderItemsService()
adressService = AdressService()
categoryService = CategoryService()
orderItemService = OrderItemService()
brandService = BrandService()
customerService = CustomerService()
productService = ProductService()
orderStatusService = OrderStatusService()
orderService = OrderService()
