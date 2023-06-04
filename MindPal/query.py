from app import Conditions, User, db

user_id = 1

condition = db.session.query(Conditions.condition_name).join(
    User).filter(User.id == user_id).all()
print(condition.condition_name)
