Checkout process

1. Cart --> Checkout view
    ?
    - login / register or enter an email (as guest)
    - shipping address
    - billing info
        - billing address
        - credit card payment


2. Billing App / Component
    - Billing Profile
        - User or email (Guest email)
        - Generate payment processor token ( Stripe or Braintree)


3. Orders / Invoices component
    - Connecting the billing profile
    - Shipping / Billing Address
    - Cart 
    - Status -- Shipped ? Cancelled?


4. Backup Fixtures
      python .\manage.py dumpdata products  --format json --indent 4 > products./fixtures/products.json 

5. UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte if you wanna load the data so you should the change the the encoding so open the file json with notepad++ and change the encoding to utf-8 it should work after that (https://www.hesk.com/knowledgebase/index.php?article=87)