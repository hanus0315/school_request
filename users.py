import time

users = {
    'user1': {
        'name': 'Alice',
        'student_number': 20221603,
        'email': 'alice@example.com'
    },
    'user2': {
        'name': 'Bob',
        'student_number': 20221604,
        'email': 'bob@example.com'
    },
    'user3': {
        'name': 'Bob',
        'student_number': 20221605,
        'email': 'bob@example.com'
    }
}

# 无限循环每隔5秒逐个获取用户的学号
while True:
    for user_id, student_number in users.items():
        users_num = student_number['student_number']
        print(users_num)
        time.sleep(5)

