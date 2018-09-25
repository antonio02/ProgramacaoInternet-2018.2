import requests

def main():
    while True:
        try:
            response = requests.get(input('Digite a Url: '))
            break
        except:
            print('Digite uma url valida')

    print('\nStatus:' , response.status_code)

    print('\nHeaders: ')
    for i in response.headers.items():
        print(' ', i)

    print('\nContent lenght: ', response.headers['Content-Length'])



if __name__ == '__main__':
    main()