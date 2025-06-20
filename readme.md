# Saves Time

Tool for using my favourite pro feature on [Http Toolkit](https://httptoolkit.com/). Created since I don't want to pay for saving time.

![alt text](https://raw.githubusercontent.com/petrovxc/http-toolkit-requests/refs/heads/main/screenshot.png)

Uploaded and working (20/06/25)

#### How this works
Correct splitting of URL and HEADERS, which are written into a new file using the numpy module.

#

Check the docs on toolkit by clicking [this link](https://httptoolkit.com/docs/)!

## Remove Data:

In lines 31-36 in create.py you can remove the extra section i added for the data that is sent along with the request if you want.

```py
if self.oneline == True:
    x = f"""import requests\n\nurl = "{self.url}" """ + """\n\ndata = {\n    "" : "",\n    "" : "",\n    "" : ""\n}""" + f"""\n\nheaders = {str(self.headers)}"""
elif self.oneline == None:
    x = f"""import requests\n\nurl = "{self.url}" """ + """\n\ndata = {\n    "" : "",\n    "" : "",\n    "" : ""\n}""" + f"""\n\nheaders = {json.dumps(self.headers, indent=4)}"""

return  x + f"""\n\nresponse = requests.{self.method}(url, headers=headers)\n\nprint(response.content)"""
```


#### Set Up

Numpy only thing you need.

Run this command in ur cmd:

```
pip install numpy
```

If you have further questions open an issue and I'll gladly help :)
#
