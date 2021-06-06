import random
import string
from datetime import datetime
from ecommerce.controllers import Controller
from ecommerce.databases.models.Order import Order
from ecommerce.databases.models.Order_Item import Order_Item
class OrderController(Controller):
    def __init__(self):
        self.order = Order()
        self.order_item = Order_Item()

    def Update_data(self, data):
        S = 32 # for order id genration
        order_dict={}
        orderItems_dict={}
        orderItems_dict['order_id'] = str(''.join(random.choices(string.ascii_lowercase + string.digits, k=32)))
        order_dict['order_id'] = orderItems_dict['order_id']
        order_dict['customer_id'] = data['customer_id']
        order_dict['order_purchase_timestamp']=datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        order_dict['order_approved_at'] = order_dict['order_purchase_timestamp']
        order_dict['order_delivered_carrier_date'] = ''
        order_dict['order_delivered_customer_date'] = ''
        order_dict['order_estimated_delivery_date']= ''
        self.order.create(order_dict)

        """
                  Now Assuming data we recive from cart is in format 
                  {'customer_id':value , 'product_id':value , ,'seller_id':value , 'product_price':value}
        """
        k=0 # for removing customer ID
        for key in data.keys:
            if(k>0):
                orderItems_dict[key]=data[key]
            k=k+1
        self.order_item.create(orderItems_dict)







