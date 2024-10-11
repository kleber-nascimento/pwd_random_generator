##### CREATE A RANDOM PASSWORD #####
import random
import string

def create_random_pwd(length, use_lowercase=True, use_uppercase=True, use_punctuation=True, use_digits=True):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase 
    if use_uppercase:
        characters += string.ascii_uppercase 
    if use_punctuation:
        characters += string.punctuation 
    if use_digits:
        characters += string.digits
    if not characters:
        raise ValueError('Escolha pelo menos um tipo de caracter!')
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# CRIAR UMA OPÇÃO PARA QUE O USUÁRIO ESCOLHA SE QUER DETERMINAR OS TIPOS DE CARACTERES. CASO NÃO, GERA COM TDS AS OPÇÕES!!

if __name__ == "__main__":

    while True: 
        length = int(input('Digite o tamanho da senha: '))
        if length >= 10:
            break
        else:
            print("A senha deve ter mais que 10 caracteres! Tente novamente!!")
    
    non_characters = input("Deseja escolher os tipos de caracteres a serem usados na senha? (s/n): ").lower()
    if non_characters == 's':
            use_lowercase = input("Deseja usar letras minusculas? (s/n):").lower() == 's'
            use_uppercase = input("Deseja usar letras maiusculas? (s/n):").lower() == 's'
            use_punctuation = input("Deseja usar letras pontuações? (s/n):").lower() == 's'
            use_digits = input("Deseja usar letras digitos? (s/n):").lower() == 's'
            
            try: 
                password = create_random_pwd(length, use_lowercase, use_uppercase, use_punctuation, use_digits)
                print('Senha gerada:', password )
                print(f'A senha gerada possui', len(password), 'caracteres!')
            except ValueError as error:
                print(error)
    else:
        password = create_random_pwd(length)
        print('Senha gerada:', password)
        print(f'A senha gerada possui', len(password), 'caracteres!')
        
    from salvar_senha import salvar_senha
    salvar_senha(password)