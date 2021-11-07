import dropbox
class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.A7czM0BfO4gvzA0Bgn5yR6ZXyxQRiUAD2FKd4EO3mvn0v4kip8IpJBGgazpwXQLsDANhNT93vFa0cceUrbMpNbc-L1yz9EXQAYrg_eQFau-aQQ7evERtysv0UMCuwQr76suwrvo"
    transferdata=Transferdata(access_token)
    file_from=input("Enter the file path to transfer:")
    file_to=input("Enter the full path to upload to dropbox:")
    transferdata.upload_file(file_from,file_to)
    print("file has been moved")

main()