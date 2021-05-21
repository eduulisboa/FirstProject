from sqlalchemy.orm import Session

from src.schemas.template_schema import TemplateSchema
from src.entities.template_entity import TemplateEntity


class TemplateRepository:

    def __init__(self, database_session: Session):
        self.__database = database_session

    def is_connected(self) -> bool:
        return True if self.__database else False

    def get_all(self):
        templates = self.__database.query(TemplateEntity).all()
        return templates

    def get_one(self, template_id):
        template = self.__database.query(TemplateEntity).get(template_id)

        if not template:
            return None

        return template

    def create(self, template: TemplateSchema):
        new_template = TemplateEntity(
            anything=template.anything,
        )

        self.__database.add(new_template)
        self.__database.commit()
        self.__database.refresh(new_template)

        return new_template

    def update(self, template_id, template: TemplateSchema):
        db_template = self.__database.query(TemplateEntity).get(template_id)

        if not db_template:
            return None

        updated_template = template.__dict__

        for key, value in updated_template.items():
            setattr(db_template, key, value)

        self.__database.commit()
        self.__database.refresh(db_template)

        return db_template

    def delete(self, template_id):
        template = self.__database.query(TemplateEntity).get(template_id)

        if not template:
            return None

        self.__database.delete(template)
        self.__database.commit()

        return template
