import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import email
import pycep_correios
import json
import urllib.request as urllib2
import sys
import smtplib


print('Carregando seu assistente')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def saudacao():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Bom dia")
        print("Bom dia")
    elif hour>=12 and hour<18:
        speak("Boa tarde")
        print("Boa tarde")
    else:
        speak("Boa noite")
        print("Boa noite")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='pt-br')
            print(f"voce disse:{statement}\n")

        except Exception as e:
            speak("Por favor, repita")
            return "Nada"
        return statement

speak("Carregando seu assistente")
saudacao()


if __name__=='__main__':


    while True:
        speak("Como posso ajudar?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "tchau" in statement or "ok tchau" in statement or "parar" in statement:
            speak('Encerrando assistente! Até a próxima!')
            print('Encerrando assistente! Até mais!')
            break



        if 'wikipédia' in statement:
            speak('Pesquisando Wikipedia...')
            statement =statement.replace("wikipedia", "")
            lang = wikipedia.set_lang("pt")
            resultados = wikipedia.summary(statement)
            speak("De acordo com o wikipedia")
            print(resultados)
            speak(resultados)
            
        elif 'sobre você' in statement or 'ajuda' in statement:
            speak('Sou seu assistente Python em português, e ajudo você em tarefas como: pesquisar o wikipedia, abrir o google, youtube, gmail, facebook, consultar um cep, ver as noticias e ver o tempo')     

        elif 'abrir youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube aberto")
            time.sleep(5)
            
              

        elif 'abrir google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google aberto")
            time.sleep(5)

        elif 'abrir gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("gmail aberto")
            time.sleep(5)

                    
        elif 'cep' in statement:
            speak("Qual o numero do cep")
            cep = takeCommand()
            endereco = pycep_correios.get_address_from_cep(cep)
            speak(endereco)
            print(endereco)
            
            
        elif 'tempo' in statement:
            global api_key_openweather
            global cidade
            global pais
            api_key_openweather = "8a3ff12127e3eebd389785d477587fde" 
            cidade_select = speak("Qual a cidade desejada?")
            cidade=takeCommand()
            pais = "br"
            
          
            url_http_req = "http://api.openweathermap.org/data/2.5/weather?q="+cidade+","+pais+"&appid="+api_key_openweather
            dados_clima = requests.get(url_http_req).json()
 
     
            temp_atual_kelvin = dados_clima["main"]["temp"]
            umidade = dados_clima["main"]["humidity"]
            nebulosidade = dados_clima["clouds"]["all"]
 
            temp_atual_celsius = int(float(temp_atual_kelvin) - 273.15)
            umidade_atual = float(umidade)
            nebulosidade = float(nebulosidade)
            speak("Temperatura atual")
            speak(temp_atual_celsius)
            speak("Nebulosidade")
            speak(nebulosidade)
            speak("Umidade atual")
            speak(umidade_atual)
                      

        elif 'hora' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hora certa {strTime}")

        elif 'facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com/")
            speak("facebook aberto")
            
        elif 'calcular' in statement:
            speak("Informe o primeiro numero")
            numero1 = takeCommand()
            speak("Informe o segundo numero")
            numero2 = takeCommand()
            speak ("Exibindo resultado")
            soma= int(numero1) + int(numero2)
            print(soma)
            subt = int(numero1) - int(numero2)
            print(subt)
            mult = int(numero1) * int (numero2)
            print(mult)
            div = int(numero1)/int(numero2)
            print(div)
        
               
        elif 'notícias' in statement:
            noticias = webbrowser.open_new_tab("https://g1.globo.com/")
            speak('Noticias do G1')
            time.sleep(6)
       
        elif 'e-mail' in statement:
        
         email = smtplib.SMTP('smtp.gmail.com', 587) 
  
    
         email.starttls() 
  
         
         email.login("teu email", "tua senha") #use uma conta do gmail
  
         #Se o comando de voz não funcionar, diga e-máil (letra e fechada e letra a aberta). Como está habilitado para português, algumas palavras em inglês podem não funcionar bem.
         #para evitar erro de autenticação, acesse a pagina https://myaccount.google.com/lesssecureapps e marque a opcão permitir
         #aplicativos menos seguros. Ao fazer isso, será possível enviar.
         #por enquanto está habilitado apenas o texto da mensagem, sem título (será colocada a opção título)
   
       
         mensagem = speak ("Diga o texto da mensagem")
         save_msg = takeCommand().encode('utf-8')
  
      
         email.sendmail("teu email", "email da pessoa", save_msg) 
  
         speak("Mensagem enviada!")
    
         email.quit()
            
                  
             
       

    time.sleep(3)
