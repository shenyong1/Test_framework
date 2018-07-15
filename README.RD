安装依赖
    python 3
    pip install ddt
    pip install pyyaml
    pip install BeautifulReport
    pip install yagmail
    pip install request

文件夹简介：
1、bin—>run.py：主函数 运行case 生成报告 发送邮件
2、case_data—>login.yml：数据驱动的数据源，用于生成测试用及校验测试结果
3、cases:存放测试用例
4、conf—>base.txt：测试用例模版，用于生成测试用例
5、conf—>setting.py：测试环境配置
6、lib:框架的基工具
   lib—>commonTools.py：通用方法，如：获取时间、生成随机数等
   lib—>log.py：管理生成日志
   lib—>my_redis.py：对于redis操作的二次封装
   lib—>my_request.py：对于request请求的二次封装，如新加异常处理，日志记录
   lib—>my_sql.py：数据操作方法
   lib—>send_mail.py：发送测试报告邮件
   lib—>tool.py：生成测试用例，运行测试用例等
7、log:存放输出的日志
8、report:存放生成的测试报告




