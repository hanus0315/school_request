import send
import request
import tkinter as tk

student_number = int(input('请输入学号:'))
mail_smtp = input('SMTP地址')
mail_user = input('SMTP用户名')
mail_password = input('SMTP授权码')
send_user = input('发送者邮箱地址')
receivers = input('接受者邮箱地址')

# mail_smtp = 'smtp.163.com'
# mail_user = 'he1669447030'
# mail_password = 'FKJKSVDCQXDIBSJJ'
# send_user = 'he1669447030@163.com'
# receivers = 'tobyhe@dgideas.cn'

respons = request.send_request(student_number)
if 'Error' in str(respons):
    print("Error:请求时发生错误")
    print(respons)
else:
    if respons[0] < 13.0 :
        send.send_mail(mail_smtp,mail_user,mail_password,send_user,receivers,int(respons[0]),student_number,respons[1])
    else:
        print('卡里还有钱')
