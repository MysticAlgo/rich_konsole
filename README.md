# rich_konsole

**rich_konsole** is a Python module that makes your tracebacks and prints more beautiful! The module also adds some custom prints

## How to install
**Python 3.8 or higher is recommended**
To install this module, you need to run the following command:
```
python3 -m pip install -U https://github.com/MysticAlgo/rich_konsole.git
```

## Usage
> Import the module
```py
>>> from rich_konsole.Konsole import konsole
```


#### print()
> This is the default print function. It formats the message with a green text.
```py
print("Hello world!")
```
![image](https://user-images.githubusercontent.com/126123983/223703507-de718501-bd9d-461c-872a-d15968918336.png)


#### konsole.info()
> This method is used to display informational messages in the console output. It formats the message with a blue text, and displays it with an "INFO" label.
```py
konsole.info("Insert imporatant informations here\nVery useful to debug your code")
```
![image](https://user-images.githubusercontent.com/126123983/223708296-f85d5049-ce73-4a07-9a6f-3007e6a1f416.png)


### konsole.warn()
> This method is used to display warning messages in the console output. It formats the message with a yellow text, and displays it with a "WARN" label.
```py
konsole.warn("Debug mode is turned on!")
```
![image](https://user-images.githubusercontent.com/126123983/223708980-388e2511-8331-4bf7-a616-9c7fa4fd57fc.png)


#### konsole.error()
> This method is used to display error messages in the console output. It formats the message with a red text, and displays it with a "ERROR" label.
```py
konsole.error("Something went horribly wrong!")
```
![image](https://user-images.githubusercontent.com/126123983/223709647-763321a4-ac7c-41c3-bf40-ae4cebbee91d.png)


## Tracebacks
> Instead of the default traceback, the konsole.error() method is used to output the traceback. This results in a more readable and user-friendly format for displaying errors in the console output.
![image](https://user-images.githubusercontent.com/126123983/223710243-c188a210-55a9-473f-8f67-b9b87af9541a.png)