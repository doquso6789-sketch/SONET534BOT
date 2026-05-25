import time

USER_COOLDOWN = {}
COOLDOWN_TIME = 10


def is_allowed(user_id):
    now = time.time()

    if user_id not in USER_COOLDOWN:
        USER_COOLDOWN[user_id] = now
        return True

    diff = now - USER_COOLDOWN[user_id]

    if diff >= COOLDOWN_TIME:
        USER_COOLDOWN[user_id] = now
        return True

    return False
