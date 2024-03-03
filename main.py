import send
import request
if __name__ == '__main__':
    student_number = int(input('请输入学号:'))
    request.send_request(student_number)
