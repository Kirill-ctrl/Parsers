from src.biz.services.base_service import BaseService


class MapReviewsService(BaseService):

    def __init__(self):
        super(MapReviewsService, self).__init__()
        self.collection = self.db_name['reviews']

    def save_reviews(self, data: dict, html_filename: str, order_id: str) -> None:
        """
        Сохранить отзывы

        :param data: дата по которой парсились отзывы
        :param html_filename: имя файла
        :param order_id: Order id
        :return:
        """
        self.collection.insert_one(
            {
                "html_filename": html_filename,
                "data": data,
                "order_id": order_id
            }
        )

    def get_by_order_id(self, order_id: str) -> dict:
        """
        Получить по order Id
        :param order_id: Order Id
        :return: сущность отзывов по карте
        """
        result = self.collection.find_one({"order_id": order_id})
        return result
