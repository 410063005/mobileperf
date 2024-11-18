# mobileperf
# [US English]

mobileperf is a Python PC tool  that can collect Android performance data: cpu,memory,fps,logcat log,traffic,process thread number,process launch log.mobileperf also support monkey test.

## Features

 * Support most versions of Android OS from 5.0 to 10.0
 * No need root device,no need integrate SDK
 * Support Mac, linux, windows
 * Good stability, can run continuously for more than 72 hours
 * a little PC resource occupation, consume PC memory about 12M

## Getting started

- Python3，recommend python3.7
- adb，ensure system path contains adb

- edit config file in mobileperf root dir,example config.conf
- run ,in mobileperf root dir，mac or linux execute sh run.sh ,windows double click run.bat,end test wait timeout or click ctrl+C

# [简体中文]

mobileperf is python PC 工具，可以收集Android性能数据: cpu 内存 流畅度fps logcat日志 流量 进程线程数 进程启动日志，mobileperf也支持原生monkey test

## 特性

- 支持Android5.0-10.0，兼容性好
- 无需root设备，无需集成SDK，非侵入式，使用成本低
- 支持mac linux windows
- 稳定性好，能连续运行72小时以上
- 少量占用PC资源，消耗PC内存约12M左右

## 使用方法

- 安装和配置Python
    - 安装python3.7 [python下载链接](https://www.python.org/downloads/)，加入到环境变量中，执行python --version，确保是python3
    - (可选) 创建 Python 虚拟环境，`python -m venv .venv`
    - (可选) 激活 Python 虚拟环境，`source .venv/bin/activate`
    - 安装 Python 依赖库，`pip install -r requirement.txt`
- 安装和使用 Redis
    - 安装 redis，`brew install redis`
    - 启动 redis 服务器，`redis-server`
    - (可选) 启动 redis 客户端，`redis-cli`。
    - (可选) 在 redis 客户端中观察消息事件，`subscribe flask-socketio`
- 安装adb，确保adb devices能找到设备
- 修改配置文件，示例参考根目录下config.conf
- 运行，mac、linux 在mobileperf工具根目录下执行sh run.sh，windows 双击run.bat，结束测试，等待设置测试时长到或按Ctrl+C
