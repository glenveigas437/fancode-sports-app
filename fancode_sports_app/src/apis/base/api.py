from flask import request
from flask_restx import Resource


class BaseApi(Resource):

    @staticmethod
    def build_response(data, status_code=200, pagination = None):
        body = {
            'data': data,
            'pagination': pagination
        }
    
        return (
            body, 
            status_code
        )

    @staticmethod
    def build_errors(data, status_code=500, errors=''):
        errors = data
        body = {
            'data': None,
            'errors': errors
        }

        return (
            body,
            status_code
        )

    @staticmethod
    def build_single_response(data, status_code=201):
        body = {
            'data': data
        }

        return (
            body,
            status_code
        )
