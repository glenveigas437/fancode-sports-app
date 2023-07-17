from flask import request
from datetime import datetime

def pagination(schema):
    offset = request.args.get("offset", 1, type=int)
    limit = request.args.get("limit", 10, type=int)

    obj = schema.paginate(per_page=limit, page=offset)

    pagination_details = {
        "total_items": obj.total,
        "per_page": obj.per_page,
        "current_page": obj.page,
        "last_page": obj.pages,
    }
    return obj.items, pagination_details

def convert_datetime_to_string(datetime_obj):
    if type(datetime_obj) == datetime:
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return str(datetime_obj)