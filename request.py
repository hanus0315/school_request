# requests file
import requests
import json
from operator import itemgetter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'    #发送AJAX请求
}  # 伪装浏览器请求头

url = 'http://zmtzx.hljxt.com.cn/CardRecharge/Weixin/searchCode.html?person_code='  # 请求地址

if __name__ == '__main__':
    student_numbers = 20221603  # 测试学号



def send_request(student_numbers):
    global headers,url,person_out,person_name,leftmonry,lastUpdateTime
    try:
        person_code = str(student_numbers)  #转换为整型

        responses = requests.get( headers=headers, url = url+person_code)   #拼接请求地址
        response = responses.json() #获取返回的json

        keys = ['rs', 'leftMoney', 'lastUpdateTime']
        out, leftmonry, lastUpdateTime = itemgetter(*keys)(response)

        person_out, person_name = itemgetter(*['personcode', 'personname'])(out)
        leftmonry = float(leftmonry)

        if leftmonry <= 13.00:
            person_poll = person_name
            output_poll = '{0}没钱吃饭啦，只剩{1}元'.format(person_name, leftmonry)
            return print(output_poll)
        else:
            output_enough = print('{0}还有{1}元钱'.format(person_name,leftmonry))
            return output_enough

    except KeyError:  # 捕捉错误
        error = print('Error:未查找到学号为{0}'.format(person_code))
        return error
    except requests.exceptions.ConnectionError:
        error = print('Error:网络错误')
        return error
    except KeyboardInterrupt:
        error = print('Error:用户自行取消')
        return error
    except:
        error = print('Error:发生未知错误')
        return error

if __name__ == '__main__' :
    send_request(student_numbers)
    print('学号:{0:|^10},姓名:{1:|^5},剩余钱数:{2:|^7},最后更新时间:{3:|^21}'.format(person_out,person_name,leftmonry,lastUpdateTime))  #格式化并打印数据


