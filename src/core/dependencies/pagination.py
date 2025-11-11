from fastapi import Query


class PaginationParams:
    def __init__(
        self,
        limit: int = Query(10, ge=1, le=100, description="Number of items per page"),
        offset: int = Query(0, ge=0, description="Offset from start"),
    ):
        self.limit = limit
        self.offset = offset
