from selenium import webdriver
import time
import random

class WhatsappBot:
    def __init__(self):
        
        self.mensagem = ["MESSAGES GOES HERE"] # MESSAGES SENT WHEN A PERSON WRITES
        self.welcome = ["WELCOME MESSAGES GOES HERE"] # MESSAGES SENT AFTER STARTING/ENTERING THE GROUP
        self.key = True
        self.count = 0
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def SendMessage(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        grupo = self.driver.find_element_by_xpath("//span[@title='GROUP NAME GOES HERE']") # GROUP THAT YOU WANT TO ENTER
        time.sleep(3)
        grupo.click()
        print("Entrando no grupo!")
        chat_box = self.driver.find_element_by_class_name('_13mgZ')
        chat_box.click()
        time.sleep(1)
        chat_box.send_keys("START MESSAGE GOES HERE") # START MESSAGES
        botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        time.sleep(1)
        botao_enviar.click()
        chat_box = self.driver.find_element_by_class_name('_13mgZ')
        time.sleep(1)
        chat_box.click()
        time.sleep(5)
        sort = random.randint(0, 1) # CHANGE NUM 1 TO N - 1 WELCOME MESSAGES //N = WELCOME MESSAGES
        chat_box.send_keys(self.welcome[sort])
        botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        time.sleep(1)
        botao_enviar.click()
        while(1):
            log = self.driver.find_elements_by_xpath("//span[@class='_1uQFN _18GNg _F7Vk']")[-1]
            time.sleep(1)
            self.count = random.randint(0,3) # SORTING TO SEND AN GORILA EMOJI
            if(log.text != "CONTACT NAME"): # PUT THE CONTACT NAME OF THE PERSON WHO YOU WANT TO ANSWER
                self.key = True
            if(log.text == "CONTACT NAME" and self.count == 1 and self.key == True): # PUT THE CONTACT NAME OF THE PERSON WHO YOU WANT TO ANSWER
                emoji_button = self.driver.find_element_by_xpath('//span[@data-icon="smiley"]')
                emoji_button.click()
                box = self.driver.find_element_by_xpath('//input[@class="_2GXNm copyable-text selectable-text"]')
                box.click()
                box.send_keys("gorila") # SEARCHES THE GORILA IN THE EMOJI SEARCH
                monkey_emoji = self.driver.find_element_by_xpath('//span[@class="b96 emojik apple"]') # GET'S THE GORILA EMOJI ELEMENT
                time.sleep(1)
                monkey_emoji.click()
                botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                botao_enviar.click()
                self.key = False
                self.count = 0
                time.sleep(5)
            elif(log.text == "CONTACT NAME" and self.key == True): # PUT THE CONTACT NAME OF THE PERSON WHO YOU WANT TO ANSWER
                sort = random.randint(0,10) # CHANGE NUM 10 TO N - 1 WELCOME MESSAGES //N = WELCOME MESSAGES
                print(sort)
                print("User escreveu!")
                chat_box = self.driver.find_element_by_class_name('_13mgZ')
                chat_box.click()
                print("Abrindo caixa de texto...")
                chat_box.send_keys(self.mensagem[sort])
                time.sleep(1)
                print("Enviando mensagem...")
                botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                time.sleep(0.7)
                botao_enviar.click()
                print("Mensagem enviada!")
                self.key = False
                time.sleep(5)

bot = WhatsappBot()
bot.SendMessage()
