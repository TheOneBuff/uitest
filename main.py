import unittest
import os
from datetime import datetime
from utils.logger import get_logger
from report import HTMLTestRunner
from report import WHPRunner
from utils.read_config import get_base_url

logger = get_logger(__name__)

if __name__ == '__main__':
    logger.info('Start testing...')
    suite = unittest.defaultTestLoader.discover('testcase',pattern='add_point.py')
    report_file = 'report/test_report_{}.html'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report', description='Test Result')
        runner.run(suite)

    logger.info('Testing finished. Report file: {}'.format(report_file))

    # # 将截图嵌入测试报告
    # with open(report_file, 'r+', encoding='utf-8') as f:
    #     content = f.read()
    #     for root, dirs, files in os.walk('C:\\Users\\Administrator\\Desktop\\git\\uitest\\report\\screenshots'):
    #         for file in files:
    #             screenshot_file = os.path.join(root, file)
    #             if 'test_report' not in screenshot_file:
    #                 screenshot_name = os.path.splitext(os.path.basename(screenshot_file))[0]
    #                 # screenshot_time = datetime.strptime(screenshot_name.split('_')[-2], '%Y-%m-%d')
    #                 screenshot_url = os.path.join(get_base_url(), screenshot_file)
    #                 content = content.replace('{}"'.format(screenshot_name), '{}" width="50%"'.format(screenshot_url))
    #     f.seek(0)
    #     f.write(content)
#http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css
#http://libs.baidu.com/jquery/2.0.0/jquery.min.js
#http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js
#https://img.hcharts.cn/highcharts/highcharts.js
#https://img.hcharts.cn/highcharts/modules/exporting.js
#https://img.hcharts.cn/highcharts/modules/exporting.js