#安装依赖
    python 3
    pip install ddt
    pip install pyyaml
    pip install nnlog
    pip install BeautifulReport
    pip install yagmail
    pip install request

文件夹简介：
1、bin—>dingdang_run.py：主函数 包含多线程运行case 多线程生成报告
2、appcase—>dingdang_test.py：测试的case，把需要测试的case添加到这里
3、lib—>page—>app—>dingdang_case.py：各个case的具体实现
4、lib—>core：框架的基本工具
5、lib—>core—>appController.py：开启server、启动app driver（server、driver的一些管理操作）
6、lib—>core—>commonTools.py：写case时用到的基本工具，如点击
7、conf—>appCcontroller.yml：相关配置，如手机操作系统、测试的app的appPcackage/appActivity
8、conf—>element_dingdang_login.yml：需要操作的页面元素
9、log—>android Emulator.log：输出的日志
10、report—>app—>android Emulator.html：生成的测试报告，可在浏览器中查看（右击android Emulator.html—>Copy Path—>黏贴到浏览器中打开）


需要下载的东西：
3、appium
2、nodejs
1、android sdk
4、python
5、python运行环境，如pyCharm


获取手机信息：
platformName: Android
platformVersion: 手机的版本号
ip: 127.0.0.1
port: 开启appium时会显示
udid: 命令行adb devices（前提：安装了adb）
deviceName: 随便取


写 case 时，根据自己的需求补充对应的文件：
1、conf—>appCcontroller.yml：根据自己的测试手机和测试app修改相关配置
2、conf—>element_dingdang_login.yml：添加页面中需要操作的元素
3、ib—>page—>app—>dingdang_case.py：各个case的具体实现
4、appcase—>dingdang_test.py：从步骤3中调用需测试的case


测试步骤：
1、开启appium服务，在命令行输入：
            Windows ：C:/Program Files/Appium/node.exe（具体根据自己电脑上appium所在文件夹）
                                C:/Program Files/Appium/node_modules/appium/bin/appium.js
            Mac电脑：appium
2、运行：bin—>dingdang_run.py
3、测试完毕关闭服务，在命令行输入：
            Windows：taskkill /F /im node.exe
            Mac电脑：pkill -9 node /t