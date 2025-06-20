import numpy, json, os

class ColventerHttp:
    def __init__(self) -> None:
        self.oneline = None
        self.request_string = None
        self.request_string_converted = None
        self.methods_string = {"POST":"post","GET":"get"}

        self.method = None
        self.url = None
        self.headers = {}

    def convert(self,code,oneline=None):
        self.oneline = oneline
        self.request_string = code
        return self.start()

    def start(self):
        self.method = self.methods_string[self.request_string.split("METHOD: ")[1].split("\n")[0]]
        self.url = self.request_string.split("URL\n")[1].split("\n")[0]
        if "HEADERS\n" in self.request_string:

            lines = self.request_string.split("HEADERS\n")[1].splitlines() 
            pairs = zip(lines[0::2], lines[1::2])
            for i in list(pairs):
                self.headers[numpy.asarray(i)[0][:-1]] = numpy.asarray(i)[1]
        else:
            self.headers = None
        
        if self.oneline == True:
            x = f"""import requests\n\nurl = "{self.url}" """ + """\n\ndata = {\n    "" : "",\n    "" : "",\n    "" : ""\n}""" + f"""\n\nheaders = {str(self.headers)}"""
        elif self.oneline == None:
            x = f"""import requests\n\nurl = "{self.url}" """ + """\n\ndata = {\n    "" : "",\n    "" : "",\n    "" : ""\n}""" + f"""\n\nheaders = {json.dumps(self.headers, indent=4)}"""

        return  x + f"""\n\nresponse = requests.{self.method}(url, headers=headers)\n\nprint(response.content)"""


def main():
    stringx = open('input.txt', 'r').read()

    res     = ColventerHttp().convert(stringx, oneline=None)

    with open('input.txt', 'w') as file:
        pass
    if os.path.exists('test.py'):
        os.remove('test.py')

    open('test.py', 'w').write(res)

if __name__ == "__main__":
    main()