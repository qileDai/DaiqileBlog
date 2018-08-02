# _*_coding=utf8_*_
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'Myblog.settings'

if __name__ == '__main__':
    subject, from_email, to = '来自www.liujiangblog.com的测试邮件', '1101187142@qq.com', '1666431030@qq.com'
    text_content = '欢迎访问http://127.0.0.1:8000/blog/，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()