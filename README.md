# bch_proxy

Setup correct BCH proxy in your python code. 

Required when trying to fetch files via python libraries (e.g. downloading deep learning models via 'huggingface' library) 

Add this to the start of your python code 

```
# Add the path of the directory containing proxy.py to your Python path
import sys
sys.path.append("/path/to/directory/containing/proxy.py")

# Now you can import and use the setup_proxy function
from proxy import setup_proxy

setup_proxy()

```


Alternatively, just use: 
```
import os
os.environ['HTTP_PROXY'] = "http://proxy.tch.harvard.edu:3128"
os.environ['HTTPS_PROXY'] = "http://proxy.tch.harvard.edu:3128"
```
