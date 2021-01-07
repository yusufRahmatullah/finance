from model.base import Base as BaseModel


class Base:
    @staticmethod
    def serialize(model: BaseModel):
        return {
            'id': model.id,
            'created_at': model.created_at,
            'updated_at': model.updated_at
        }

    @staticmethod
    def _merge(json_a, json_b):
        return dict(**json_a, **json_b)
