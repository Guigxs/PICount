from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class piApp(App):
    def build(self):
        self.conte = 0
        self.contenu = []
        self.virgule = 0

        self.title = 'Salut'
        self.box = BoxLayout(orientation = 'vertical')
        self.label = Label(text = 'Bonjour, veuillez entrer le premier chiffre de pi...', font_size = 30)

        self.box.add_widget(self.label)


        self.afficheur()

        self.box.add_widget(self.pad_box)

        return self.box

    def affichage(self, source):
        try :
            if source.text != "Supr." and source.text != ",": #SI ON CLIC SUR CHIFFRE, ON L'AJOUTE A LA LISTE
                self.contenu.append(source.text)

            if source.text == "," and self.virgule == 0: #SI C'EST UNE "," ON L'AJOUTE
                self.contenu.append(source.text)
                self.virgule = 1

            if source.text == "Supr.": #SUPPRIME LE DERNIER ELEMENT 
                if self.contenu[-1] == ",":
                    self.virgule = 0

                self.contenu.pop(-1)
                
        except :
            print("Plus de place")

        finally:
            self.conte = len(self.contenu)
            self.check()


    
    def afficheur(self): #PAD D'AFFICHAGE (CLAVIER)

        self.pad_box = GridLayout(rows = 4, cols = 3)

        for i in range(7, 10):
            self.button = Button(text = str(i))
            self.button.bind(on_press=self.affichage)
            self.pad_box.add_widget(self.button)
        
        for i in range(4, 7):
            self.button = Button(text = str(i))
            self.button.bind(on_press=self.affichage)
            self.pad_box.add_widget(self.button)
        
        for i in range(1, 4):
            self.button = Button(text = str(i))
            self.button.bind(on_press=self.affichage)
            self.pad_box.add_widget(self.button)

        self.button_supr = Button(text = "Supr.")
        self.button_supr.bind(on_press=self.affichage)
        self.pad_box.add_widget(self.button_supr)
        
        self.button_zero = Button(text = "0")
        self.button_zero.bind(on_press=self.affichage)
        self.pad_box.add_widget(self.button_zero)

        self.button_virg = Button(text = ",")
        self.button_virg.bind(on_press=self.affichage)
        self.pad_box.add_widget(self.button_virg)



    def check(self):
        print("Contenu:", self.contenu)
        self.affiche = ""  #AFFICHE LA LISTE DANS LE LABEL 
        for i in self.contenu:
            self.affiche += str(i) 

        with open ("pi.txt", "r") as file:
            self.pi = file.read()

        self.label.text = self.affiche
        print("Affiche:", self.affiche)

        a = ""
        for i in range(len(self.affiche)):
            a += str(self.pi[i])
        
        if a == self.affiche:
            print("OK")
            self.label.color = [0, 1, 0, 1]
        else: 
            print("Chiffre faux")
            self.label.color = [1, 0, 0, 1]


piApp().run()