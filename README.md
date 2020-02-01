# billing_store


* ``checkout.py`` class has all the checkout of items realted logic. <br>
* ``pricingRulesUtil.py`` class reads data related to items from json-file and cache it, so<br>
    tha we don't read file multiple-times. If the json-file is modified, cache gets updated with latest values. <br>
* To test the code run ``test.py``. It contains 4 test-cases mentioned in the challenge.
