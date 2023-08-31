import unittest
import os
from datetime import datetime
from utils.logger import get_logger
from report import HTMLTestRunner
logger = get_logger(__name__)

if __name__ == '__main__':
    logger.info('Start testing...')
    suite = unittest.defaultTestLoader.discover('testcase', pattern='point_view.py')
    report_file = 'report/test_report_{}.html'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report', description='Test Result')
        runner.run(suite)
    logger.info('Testing finished. Report file: {}'.format(report_file))
