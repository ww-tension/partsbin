# === Stage 35: Add active user switching and user-specific records ===
# Project: PartsBin
class ActiveUser:
    def __init__(self, username):
        self.username = username
        self.records = []
        self.is_active = False

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        if record in self.records:
            self.records.remove(record)

    def active_record(self, record):
        return record in self.records

    def active_records(self):
        return list(self.records)


active_users = {}
current_user = None


def switch_user(username):
    global current_user
    if username not in active_users:
        active_users[username] = ActiveUser(username)
    active_users[username].is_active = True
    current_user = active_users[username]
    return current_user


def deactivate_user(username):
    global current_user
    if username in active_users:
        active_users[username].is_active = False
    if current_user is not None and current_user.username == username:
        current_user = None


def current_user_name():
    return current_user.username if current_user is not None else None


def add_record_to_current_user(record):
    if current_user is not None:
        current_user.add_record(record)


def remove_record_from_current_user(record):
    if current_user is not None:
        current_user.remove_record(record)


def get_active_records():
    if current_user is not None:
        return current_user.active_records()
    return []


def set_current_user(username):
    global current_user
    if username in active_users:
        current_user = active_users[username]
    else:
        current_user = None
