import PyInstaller
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        'Autoclass-V1.2.2.py',
        '--collect-all', 'selenium',
        '-i=logo.ico',
        '--name=Autoclass-V1.2.2',
        '--hidden-import=selenium.webdriver.edge.service',
        '--hidden-import=selenium.webdriver.edge.options',
        '--hidden-import=selenium.webdriver.common.service',
    ]
    run(opts)


#
# if __name__ == '__main__':
#     opts = [
#         'data.py',
#         '-F'
#     ]
#     run(opts)