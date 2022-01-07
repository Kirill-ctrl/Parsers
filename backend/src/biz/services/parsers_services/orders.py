from datetime import datetime
import pytz
from bson import ObjectId
from src.biz.services.base_service import BaseService
from src.biz.exceptions.custom import NotFoundError

from src.biz.exceptions.enums import ExceptionEnum


class OrderService(BaseService):

    def __init__(self):
        super(OrderService, self).__init__()
        self.collection = self.db_name['orders']

    def update_status_order(self, order_id: str):
        self.collection.update_one({"_id": ObjectId(order_id)}, {"$set": {"status_ready": True}})

    def create_order(self, data, email):
        order = self.collection.insert_one({
            "data": data,
            "email": email,
            "created_at": datetime.now(tz=pytz.UTC),
            "status_ready": False
        })
        return str(order.inserted_id)

    def get_by_email(self, email):
        results = self.collection.find(
            {
                "email": email,
                "status_ready": True
            }
        )
        results = [result for result in results]
        return results

    def delete_by_id(self, order_id: str):
        self.get_by_id(order_id)
        result = self.collection.delete_one({"_id": ObjectId(order_id)})
        return True

    def get_by_id(self, order_id: str):
        order = self.collection.find_one({"_id": ObjectId(order_id)})
        if not order:
            raise NotFoundError(ExceptionEnum.order_not_found)
        return order
