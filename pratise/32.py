# 获取操作系统信息（版本，名称，位数，架构等）
import platform


print(platform.machine())
print(platform.node())
print(platform.platform(True))
print(platform.system())
print(platform.uname())
print(platform.architecture())
