# billing_store


* ``checkout.py`` class has all the logic related to buying and checkout of items. <br>
* ``pricingRulesUtil.py`` class reads data related to items from json-file and cache it, so<br>
    that we don't read file multiple-times. If the json-file is modified, cache gets updated with latest values. <br>
    ``os.stat(filepath)`` return file-stats like modified-time etc. Based on modified-time we update the cache.
* Item details(Code, Name, Price,Discount) are in the ``itemStore.json`` file. Following is the format: <br>
    
    ``` { 
        "VOUCHER": {
                "name": "NoviCap Voucher",
                "price": 5,
                "discount": "2-for-1"
                }
        }
        ```
    
* To test the code run ``test.py`` using command in terminal ``python test.py``. It contains 4 test-cases mentioned in the challenge.
 
