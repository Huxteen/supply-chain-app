from rest_framework.exceptions import APIException


class ProductOutOfStockValidation(APIException):
    status_code = 400
    default_detail = "product out of stock."
    default_code = "product_out_of_stock"
