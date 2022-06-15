import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 
    transferData = TransferData(access_token)

    file_from = input("Qual é o arquivo que vai ser enviado? ") 
    print("exemplo: '/test_dropbox/texto.txt' ")
    file_to = input("Qual é o caminho do dropbox")
    # API v2
    transferData.upload_file(file_from, file_to)
    print("Arquivo Enviado")
main()

