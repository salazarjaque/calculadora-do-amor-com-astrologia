from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (350, 300)

class TelaCalculadoraAmor(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.imagem = Image(source='love.png', allow_stretch=True, keep_ratio=False,
                            size_hint=(0.6, 0.4), 
                            pos_hint={'center_x': 0.5, 'top': 1})  
        layout.add_widget(self.imagem)

        # título
        self.label_titulo = Label(text='Quanto ele/ela está a fim de você?', font_size=20,
                                  size_hint=(None, None), size=(500, 50),
                                  pos_hint={'center_x': 0.5, 'y': 0.8})
        layout.add_widget(self.label_titulo)
        
        # Entrada de nomes
        self.label_nome1 = Label(text="Escreva seu nome:", size_hint=(None, None), size=(200, 50),
                                 pos_hint={'center_x': 0.5, 'y': 0.55})
        layout.add_widget(self.label_nome1)
        self.entrada_nome1 = TextInput(multiline=False, size_hint=(None, None), size=(200, 50),
                                       pos_hint={'center_x': 0.5, 'y': 0.45})
        layout.add_widget(self.entrada_nome1)

        self.label_nome2 = Label(text="Escreva o nome do(a) seu(sua) parceiro(a):", size_hint=(None, None), size=(300, 50),
                                 pos_hint={'center_x': 0.5, 'y': 0.35})
        layout.add_widget(self.label_nome2)
        self.entrada_nome2 = TextInput(multiline=False, size_hint=(None, None), size=(200, 50),
                                       pos_hint={'center_x': 0.5, 'y': 0.30})
        layout.add_widget(self.entrada_nome2)

        # Botão de calcular
        self.botao_calcular = Button(text="Calcular", size_hint=(None, None), size=(150, 50),
                                     pos_hint={'center_x': 0.5, 'y': 0.20})
        self.botao_calcular.bind(on_press=self.calcular_amor)
        layout.add_widget(self.botao_calcular)
        
        # Botão de compatibilidade astrológica
        self.botao_astrologia = Button(text="Compatibilidade Astrológica", size_hint=(None, None), size=(200, 50),
                                       pos_hint={'center_x': 0.5, 'y': 0.05})
        self.botao_astrologia.bind(on_press=self.ir_para_astrologia)
        layout.add_widget(self.botao_astrologia)
        
        self.add_widget(layout)

    def calcular_amor(self, instance):
        nome1 = self.entrada_nome1.text
        nome2 = self.entrada_nome2.text

        nomes_combinados = (nome1 + nome2).lower()
        t = nomes_combinados.count("t")
        r = nomes_combinados.count("r")
        u = nomes_combinados.count("u")
        e = nomes_combinados.count("e")
        primeiro_digito = t + r + u + e

        l = nomes_combinados.count("l")
        o = nomes_combinados.count("o")
        v = nomes_combinados.count("v")
        e = nomes_combinados.count("e")
        segundo_digito = l + o + v + e

        pontuacao = int(f"{primeiro_digito}{segundo_digito}")

        if (pontuacao < 10) or (pontuacao > 90):
            texto_resultado = f"Sua pontuação é {pontuacao}, vocês combinam como coca e mentos."
        elif (pontuacao >= 40) and (pontuacao <= 50):
            texto_resultado = f"Sua pontuação é {pontuacao}, vocês são mais ou menos."
        else:
            texto_resultado = f"Sua pontuação é {pontuacao}."

        popup = Popup(title='Resultado do Amor', content=Label(text=texto_resultado), 
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def ir_para_astrologia(self, instance):
        self.manager.current = 'calculadora_astrologia'

class TelaCalculadoraAstrologia(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # titulo
        self.label_titulo = Label(text='Compatibilidade Astrológica', font_size=20,
                                  size_hint=(None, None), size=(300, 50),
                                  pos_hint={'center_x': 0.5, 'y': 0.8})
        layout.add_widget(self.label_titulo)

        # entra de datas do nascimento
        self.label_nascimento1 = Label(text="Data de nascimento da pessoa 1 (dd/mm):", size_hint=(None, None), size=(300, 50),
                                       pos_hint={'center_x': 0.5, 'y': 0.55})
        layout.add_widget(self.label_nascimento1)
        self.entrada_nascimento1 = TextInput(multiline=False, size_hint=(None, None), size=(200, 50),
                                             pos_hint={'center_x': 0.5, 'y': 0.45})
        layout.add_widget(self.entrada_nascimento1)

        self.label_nascimento2 = Label(text="Data de nascimento da pessoa 2 (dd/mm):", size_hint=(None, None), size=(300, 50),
                                       pos_hint={'center_x': 0.5, 'y': 0.35})
        layout.add_widget(self.label_nascimento2)
        self.entrada_nascimento2 = TextInput(multiline=False, size_hint=(None, None), size=(200, 50),
                                             pos_hint={'center_x': 0.5, 'y': 0.30})
        layout.add_widget(self.entrada_nascimento2)

        # botão de calcular compatibilidade 
        self.botao_calcular = Button(text="Calcular Compatibilidade", size_hint=(None, None), size=(200, 50),
                                     pos_hint={'center_x': 0.5, 'y': 0.15})
        self.botao_calcular.bind(on_press=self.calcular_compatibilidade_astrologica)
        layout.add_widget(self.botao_calcular)

        # botão de voltar
        self.botao_voltar = Button(text="Voltar", size_hint=(None, None), size=(100, 50),
                                   pos_hint={'x': 0, 'y': 0})
        self.botao_voltar.bind(on_press=self.voltar_para_calculadora_amor)
        layout.add_widget(self.botao_voltar)

        self.add_widget(layout)

    def calcular_compatibilidade_astrologica(self, instance):
        nascimento1 = self.entrada_nascimento1.text.split('/')
        nascimento2 = self.entrada_nascimento2.text.split('/')

        if len(nascimento1) == 2 and len(nascimento2) == 2:
            dia1, mes1 = int(nascimento1[0]), int(nascimento1[1])
            dia2, mes2 = int(nascimento2[0]), int(nascimento2[1])

            compatibilidade = self.calcular_compatibilidade_por_signo(dia1, mes1, dia2, mes2)
            texto_resultado = f"A compatibilidade astrológica entre vocês dois é de {compatibilidade}%!"
        else:
            texto_resultado = "Por favor, insira as datas de nascimento corretamente."

        popup = Popup(title='Resultado da Compatibilidade', content=Label(text=texto_resultado), 
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def obter_signo(self, dia, mes):
        if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
            return 'Áries'   
        if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
            return 'Touro'
        if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
            return 'Gêmeos'
        if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
            return 'Câncer'
        if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
            return 'Leão'
        if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
            return 'Virgem'
        if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
            return 'Libra'
        if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
            return 'Escorpião'
        if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
            return 'Sagitário'
        if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
            return 'Capricórnio'
        if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
            return 'Aquário'
        if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
            return 'Peixes'

        # q demora mds

    def calcular_compatibilidade_por_signo(self, dia1, mes1, dia2, mes2):
        signo1 = self.obter_signo(dia1, mes1)
        signo2 = self.obter_signo(dia2, mes2)

        tabela_compatibilidade = {
            ('Áries', 'Touro'): 50,
            ('Áries', 'Gêmeos'): 70,
            ('Áries', 'Câncer'): 30,
            ('Áries', 'Leão'): 60,
            ('Áries', 'Virgem'): 60,
            ('Aquário,' 'Libra'): 15,
            ('Aquário,' 'Virgem'): 80,
            ('Virgem', 'Touro'): 90,
            ('Capricórnio', 'Libra'): 35,
            ('Sagitário', 'Escorpião'): 1000,
            ('Sagitário', 'Libra'): 55,
            ('Câncer', 'Leão'): 68,
            ('Leão', 'Leão'): 90,
            ('Gêmeos', 'Escorpião'): 40,
            ('Sagitário', 'Sagitário'): 90,
            ('Virgem', 'Capricórnio'): 80,
            ('Peixes', 'Capricórnio'): 80,
            ('Peixes', 'Aquário'): 40,
            ('Peixes', 'Peixes'): 70
            # espero q seja suficiente esse tanto
        }

        return tabela_compatibilidade.get((signo1, signo2), 50)

    def voltar_para_calculadora_amor(self, instance):
        self.manager.current = 'calculadora_amor'

class TelaMenuPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.label_titulo = Label(text="Menu Principal", font_size=30,
                                  size_hint=(None, None), size=(400, 50),
                                  pos_hint={'center_x': 0.5, 'y': 0.8})
        layout.add_widget(self.label_titulo)

        self.botao_ir_para_calculadora_amor = Button(text="Ir para Calculadora de Amor",
                                                     size_hint=(None, None), size=(300, 50),
                                                     pos_hint={'center_x': 0.5, 'y': 0.5})
        self.botao_ir_para_calculadora_amor.bind(on_press=self.ir_para_calculadora_amor)
        layout.add_widget(self.botao_ir_para_calculadora_amor)

        self.add_widget(layout)

    def ir_para_calculadora_amor(self, instance):
        self.manager.current = 'calculadora_amor'

class GerenciadorTelas(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tela_menu_principal = TelaMenuPrincipal(name='menu_principal')
        self.tela_calculadora_amor = TelaCalculadoraAmor(name='calculadora_amor')
        self.tela_calculadora_astrologia = TelaCalculadoraAstrologia(name='calculadora_astrologia')

        self.add_widget(self.tela_menu_principal)
        self.add_widget(self.tela_calculadora_amor)
        self.add_widget(self.tela_calculadora_astrologia)

class MeuApp(App):
    def build(self):
        return GerenciadorTelas()

if __name__ == '__main__':
    MeuApp().run()

