import requests

def setup_proxy(proxy_url="http://proxy.tch.harvard.edu:3128", proxy_username=None, proxy_password=None, proxy_site_test='https://huggingface.co'):
    # Create a proxy dictionary with the appropriate protocol (http/https)
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    # If the proxy requires authentication, include it in the proxies dictionary
    if proxy_username and proxy_password:
        proxies['http'] = f"http://{proxy_username}:{proxy_password}@{proxy_url}"
        proxies['https'] = f"http://{proxy_username}:{proxy_password}@{proxy_url}"

    # Set the proxies in the requests library
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'

    # Now you can make requests with the proxies
    try:
        response = requests.get(proxy_site_test, proxies=proxies)
        # Your code here to handle the response
        print("Response")
        print(response.status_code)
        if response.status_code == 200: 
            print("Proxy is working")
        else:
            print("Proxy may not be working. ")
            print("Proxy site test is:")
            print(proxy_site_test)
            print("proxy url is")
            print(proxy_url)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")    

    # return proxies
if __name__=='__main__':
	setup_proxy()