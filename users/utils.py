def setup_new_user(instance, email):
    instance.username = email
    instance.is_staff = True
    # TODO Setup permissions


