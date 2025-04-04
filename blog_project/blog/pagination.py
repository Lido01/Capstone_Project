from rest_framework.pagination import (
    LimitOffsetPagination,
    BasePagination
)

class PostLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10