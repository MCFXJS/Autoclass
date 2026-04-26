import PyInstaller
from PyInstaller.__main__ import run

# if __name__ == '__main__':
#     opts = [
#         'Autoclass-V1.4.2.py',
#         '--collect-all', 'selenium',
#         '-i=logo.ico',
#         '--name=Autoclass-V1.4.2',
#         #edge驱动
#         '--hidden-import=selenium.webdriver.edge.service',
#         '--hidden-import=selenium.webdriver.edge.options',
#         '--hidden-import=selenium.webdriver.common.service',
#         #Chrome 驱动
#         '--hidden-import=selenium.webdriver.chrome.service',
#         '--hidden-import=selenium.webdriver.chrome.options',
#         '--hidden-import=selenium.webdriver.chrome.webdriver',
#     ]
#     run(opts)



if __name__ == '__main__':
    opts = [
        'data.py',
        '--collect-all', 'selenium',
        '-i=logo.ico',
        '--name=data',
        # edge驱动
        '--hidden-import=selenium.webdriver.edge.service',
        '--hidden-import=selenium.webdriver.edge.options',
        '--hidden-import=selenium.webdriver.common.service',
        # Chrome 驱动
        '--hidden-import=selenium.webdriver.chrome.service',
        '--hidden-import=selenium.webdriver.chrome.options',
        '--hidden-import=selenium.webdriver.chrome.webdriver',

        '-F'

    ]
    run(opts)
