# Postcode Request
###Postcode request task  
1. Create a package
2. Ask user for a post code
3. Return postcode info  
###Prerequisites
1. Python
2. 'requests' package
###How to install
* #####Using PIP install
1. Open Terminal
2. Type "pip install package_postcoderequest"
###How to use
1. import package_postcoderequest    
   ```python 
   from package_postcoderequest import PostCode
   ```
2. create instance of your postcode search
    ```python
   Variable_name = PostCode("ExamplePostcode")
   ```
3. Method examples.  
   1. check postcode length
   ```python
   Variable_name.check_length()
   ```
   2. check full info
   ```python
   Variable_name.output_full()
   ```
   3. check location info
   ```python
   Variable_name.output_location()
   ```
###How to contribute
If you would like to contribute please append the **'postcode_class.py'** file in the '**app_code**' folder and then 
add yourself as a contributor to the '**README.md**' file.
###Contributors
Arcan  
Ed  
Kieran  
Luke
###Acknowledgements
Paula
###License information
Unlicensed