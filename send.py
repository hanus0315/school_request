import smtplib
from email.mime.text import MIMEText

def send_mail(mail_smtp,mail_user,mail_password,send_user,receivers,respons,student_number,name):
# 定义函数方便在main中调用
    print('wait')
    message = MIMEText('{2}|{1}|没钱吃饭啦，只剩|{0}|元钱了'.format(respons,student_number,name),'plain','utf-8')
    # 邮件正文
    message['Subject'] = '来自检测程序的报告'
    # 邮件标题
    message['From'] = send_user
    # 邮件发送者邮箱
    message['To'] = receivers
    #邮件接受者邮箱

    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_smtp,25)
        # 连接服务器
        smtpobj.login(mail_user,mail_password)
        # 使用信息登陆
        smtpobj.sendmail(send_user,receivers,message.as_string())
        # 发送邮件
        smtpobj.quit()        
        # 结束动作
        return print("已发送邮件提醒父母充值")
        # 给予用户反馈
    except AttributeError:
        print('Error:未能从所依赖的网页中获取源数据')
    except smtplib.SMTPServerDisconnected:
        print('未正确输入所需数据')
    except :
        print('Error:未知错误')
    # 错误捕捉

if __name__ == '__main__' :
    send_mail(mail_smtp = 'smtp.163.com',mail_user = 'he1669447030',mail_password = 'FKJKSVDCQXDIBSJJ',send_user = 'he1669447030@163.com',receivers = '1669447030@qq.com',respons=15,student_number=20221603)
# 测试用数据