from distutils.core import setup

setup(name="message_package",  # 包名
      version="1.0",  # 版本
      description="发送和接受消息模块",  # 描述信息
      long_description="完整的发送和接受消息模块",  # 完整的饿描述信息
      author="zwl",  # 作者
      author_email="470211273@qq.com",  # 作者邮箱
      url="www.zwl.com",  # 主页
      py_modules=["message.send_message", "message.receive_message"]
      )

