from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CarPaginator(LimitOffsetPagination):
    max_limit = 1000

    def get_paginated_response(self, data):
        return Response({
            'link': {
                'next': self.get_next_link(),
                'prev': self.get_previous_link()
            },
            'count': self.count,
            'data': data
        })
