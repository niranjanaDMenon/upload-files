import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dx= dropbox.Dropbox(self.access_token)


    d= open(file_from,'rb')
    dx.files_upload(d.read() , file_to)


    def main():
        access_token = 'sl.A7M9bflRZA7zFa9_b29WDovwl6tyGJGX5ErfGUuJG7RtAU-EqRYSRHl2aU4I6QLnOm
        transferData = TransferData(access_token)