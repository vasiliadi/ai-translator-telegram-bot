from pony import orm
from config import DB_SETTINGS


db = orm.Database()


class UsersOrm(db.Entity):
    _table_ = "users"

    user_id = orm.PrimaryKey(int, auto=False)
    first_name = orm.Optional(str, nullable=True)
    last_name = orm.Optional(str, nullable=True)
    username = orm.Optional(str, nullable=True)
    approved = orm.Required(bool)


db.bind(**DB_SETTINGS)
db.generate_mapping(create_tables=True)


@orm.db_session
def auth(user_id):
    return UsersOrm.get(user_id=user_id).approved


@orm.db_session
def register_user(
    user_id,
    first_name,
    last_name,
    username,
    approved=False,
):
    if not UsersOrm.exists(user_id=user_id):
        UsersOrm(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            approved=approved,
        )
        return True
    else:
        return False  # already registered user
