from filestack import Client


class FileSharer:
    YOUR_API = "Put your API key from Filestack here!"

    def __init__(self, filepath, api_key=YOUR_API):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url