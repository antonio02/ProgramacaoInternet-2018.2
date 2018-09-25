import requests

def main():
    while True:
        try:
            url = input('Digite a Url: ')

            if(url.strip().endswith('.jpg')):
                response = requests.get(url)
                break

            else:
                print('Digite uma url para uma imagem .jpg')
        except:
            print('Digite uma url valida')

    if response.status_code == 200:

        with open("Foto.jpg", "wb") as f:

            f.write(response.content)



if __name__ == '__main__':
    main()