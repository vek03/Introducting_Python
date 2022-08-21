#aprendendo a usar packages e requests
import requests

def return_data_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def return_pokemon_data(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def return_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = return_response('https://g1.globo.com/')
    print(response)
    #return_data_cep('08485200')
    #dados_pokemon = return_pokemon_data('pikachu')
    #print(dados_pokemon)