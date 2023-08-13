import unittest
from datetime import datetime
from utils.logger import get_logger
from report import HTMLTestRunner

logger = get_logger(__name__)

if __name__ == '__main__':
    logger.info('Start testing...')
    suite = unittest.defaultTestLoader.discover('testcase')
    report_file = 'report/test_report_{}.html'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report', description='Test Result')
        runner.run(suite)
    logger.info('Testing finished. Report file: {}'.format(report_file))

    # 将截图嵌入测试报告
    with open(report_file, 'r+', encoding='utf-8') as f:
        content = f.read()
        for root, dirs, files in os.walk('report/screenshots'):
            for file in files:
                screenshot_file = os.path.join(root, file)
                if 'test_report' not in screenshot_file:
                    screenshot_name = os.path.splitext(os.path.basename(screenshot_file))[0]
                    screenshot_time = datetime.strptime(screenshot_name.split('_')[-2], '%Y-%m-%d')
                    screenshot_url = os.path.join(get_base_url(), screenshot_file)
                    content = content.replace('{}"'.format(screenshot_name), '{}" width="50%"'.format(screenshot_url))
        f.seek(0)
        f.write(content)