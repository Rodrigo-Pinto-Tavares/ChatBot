import openai

openai.api_key = 'sVn14...'

count_prompt = 0
limite = 20
password = 'password'                                                                   #il faudrait cripter ce mot_de_passe

def generate_blog(user_prompt):
    global count_prompt
    count_prompt += 1                                                                   #incrémentation du compteur à chaque appel
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt= user_prompt,                                                            #on permet de générer n'importe quelle demande de l'utilisateur
        max_tokens= 600,
        temperature= 0.3                                                                #ici la temperature [0;1] est en fait le niveau de précision des réponses plus il est proche de 0 plus il est logique, structuré et cohérent
    )
    return response.choices[0].text                                                     #ici on lui demande de prendre la première réponse possible qu'il génére, si on met un 1 alors on en aura 2 des réponses aléatoires

mdp = input("Password: ") #password

if mdp != password:
    print("Password incorrect. Accès refusé.")
else:
    print('Password correct, vous pouvez prompter.')

    while count_prompt >= limite:                                                       #boucle jusqu'à 20 prompts
        print(f'Prompts envoyés: {count_prompt}/{limite}')                              #affichage du compteur de prompts
        user_input = input("You: ")

        if user_input == 'Bye':                                                         #ici nous avons une condition de réponse pour que si on lui dit Bye il nous réponde
            print('Chatbot: Goodbye!')
            break

        reponse = generate_blog(user_input)
        print(f'Chatbot: \n {reponse}')

print("T'as déjà réalisé 20 prompt...")                                                 #réponse une fois les 20 prompts réalisés