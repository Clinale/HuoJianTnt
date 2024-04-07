import os
import sys
import json
import login 
import getWebStatu
import yagmail

def send_email(sender, passwd, receiver, contents):
    subject = "火箭TNT签到"
    # 初始化yagmail客户端
    yag = yagmail.SMTP(user=sender, password=passwd, host='smtp.qq.com', encoding='GBK')
    # 发送邮件
    yag.send(to=receiver, subject=subject, contents=contents)
    # 不需要手动关闭连接，yagmail会自动处理

baseUrl = getWebStatu.getWebUrl()
checkUrl = baseUrl + 'user/checkin'
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
# 初始化邮箱参数
sender = os.environ['SENDER']
sender_passwd = os.environ['SENDER_PASSWORD']
receiver = os.environ['RECEIVER']

if __name__ == "__main__":
    loginCode =  login.login(username, password)
    if loginCode != 1: 
        print('登录失败')
    session = login.session
    # 请求签到
    checkin = session.post(checkUrl).text
    checkin = json.loads(checkin)
    # 签到状态
    if checkin['ret'] == 1:
        contents = ["火箭TNT签到成功", checkUrl, str(checkin['msg']),'https://github.com/1802024110/HuoJianTnt','火箭TNT']
    else:
        contents = ["火箭TNT签到失败", checkUrl, str(checkin['msg']),'https://github.com/1802024110/HuoJianTnt','火箭TNT']
    print(contents)
    send_email(sender, sender_passwd, receiver, '\n'.join(contents))
