import uuid
from datetime import datetime


class Message:
    props: dict

    def __init__(self, **kwargs) -> None:
        self.props = {"id": str(uuid.uuid1()), "timestamp": str(datetime.now())}
        for key, value in kwargs.items():
            self.props[key] = value

    def __str__(self) -> str:
        return str(self.props)

    @staticmethod
    def validate(obj: dict):
        if obj.get("id", None) is None or type(obj["id"]) is not str:
            raise ValueError("'id' attribute invalid:", obj.get("id", None))
        if (
            obj.get("timestamp", None) is None
            or type(obj["timestamp"]) is not str
            or datetime.fromisoformat(obj["timestamp"]) > datetime.now()
        ):
            raise ValueError("'timestamp' attribute invalid:", obj.get("timestamp", None))
