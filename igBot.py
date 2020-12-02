from selenium import webdriver
from selenium.webdriver.common import keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"")##Diretorio do geckodriver.

    def login(self):
        print('Inciando o instaBot')
        driver = self.driver
        driver.get("https://www.instragam.com")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_entrar = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        campo_entrar.click()
        time.sleep(5)
        agora_nao = driver.find_element_by_class_name("yWX7d")
        agora_nao.click()
        time.sleep(3)
        agora_nao2 = driver.find_element_by_class_name("HoLwm")
        agora_nao2.click()
        self.comente_nas_fotos()
    
    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,3))

    def comente_nas_fotos(self):

        a = 1

        while(1):
       
            driver = self.driver
            time.sleep(5)
            sorteio = "" ##Link do sorteio.
            driver.get(sorteio)

            try:
                comments = [
                ##adicionar os @ aqui dentro.
                ]
                comentar = driver.find_element_by_class_name("Ypffh")
                comentar.click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 10))
            
                pessoa_1 = random.choice(comments)
                pessoa_2 = random.choice(comments)
                marcar_2_pessoas = pessoa_1 + " " + pessoa_2

                if sorteio:
                    self.type_like_a_person(marcar_2_pessoas, comment_input_box)
                print("Comentei: ", marcar_2_pessoas, " no post: ", sorteio, "")
            
                time.sleep(random.randint(1, 4))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()

                a = a + 1
                print('Vezes comentadas: ')
                print(a)

                time.sleep(60)  
           

            except Exception as e:
              print(e)
            time.sleep(5)

instaBot = InstagramBot('seu usuario', 'sua senha')
instaBot.login()