import requests
from tkinter import *


def get_address():

        link = f'https://cep.awesomeapi.com.br/json/{int(input_cep.get())}'

        req = requests.get(link)

        if req.status_code == 200:
                ans = req.json()
                text_out_app['text'] = print(ans)
                address = ans['address']
                district = ans['district']
                city = ans['city']
                state = ans['state']
                cod_cep = ans['cep']
                address_out_put = f'{address}, {district}, {city}-{state}, {cod_cep}'
                text_out_app['text'] = address_out_put

        elif req.status_code == 404:
                text_out_app['text'] = 'CEP não localizado!'

        else:
                text_out_app['text'] = 'CEP Inválido!'

## map

# cep = int(input('digite o cep: '))
# link = f'https://cep.awesomeapi.com.br/json/{cep}'
# req = requests.get(link)
# ans = req.json()
# address = ans['address']
# district = ans['district']
# city = ans['city']
# state = ans['state']
# cod_cep = ans['cep']
# address_out_put = f'{address}, {district}, {city}-{state}, {cod_cep}'

# application
main_window = Tk()

main_window.geometry('650x150')

main_window.title('Busca endereço')
text_position = Label(main_window, text='Informe o CEP')
text_position.grid(row=0, column=0)
input_cep = Entry(main_window)
input_cep.place(width=150, height=50)
input_cep.grid(row=0, column=1)


button_get_address = Button(main_window, text='Buscar', command=get_address)
button_get_address.grid(row=0, column=2)

text_out_app = Label(main_window, text='')
text_out_app.grid(row=5, column=1)

main_window.mainloop()
