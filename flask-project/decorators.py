from flask import Flask, render_template, url_for, request, redirect, session
from functools import wraps


# 登录限制装饰器
def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user_id"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
