import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.lang import Builder

# Definir a versão mínima do Kivy
kivy.require('2.1.0')

# Carregar o arquivo KV
Builder.load_file('combustivel.kv')

# Tela principal para cálculo de combustível
class TelaCalculoCombustivel(Screen):
    resultado = StringProperty('')
    
    def calcular_melhor_combustivel(self):
        try:
            preco_gasolina = float(self.ids.preco_gasolina.text.replace(',', '.'))
            preco_etanol = float(self.ids.preco_etanol.text.replace(',', '.'))
            
            if preco_etanol / preco_gasolina > 0.7:
                self.resultado = f'Melhor abastecer com GASOLINA\nRelação: {preco_etanol/preco_gasolina:.2f}'
            else:
                self.resultado = f'Melhor abastecer com ETANOL\nRelação: {preco_etanol/preco_gasolina:.2f}'
        except ValueError:
            self.mostrar_erro('Por favor, insira valores numéricos válidos.')
    
    def limpar_campos(self):
        self.ids.preco_gasolina.text = ''
        self.ids.preco_etanol.text = ''
        self.resultado = ''
    
    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro',
                     content=Label(text=mensagem),
                     size_hint=(None, None), size=(400, 200))
        popup.open()

# Tela para cálculo de consumo médio
class TelaConsumoMedio(Screen):
    resultado_consumo = StringProperty('')
    
    def calcular_consumo(self):
        try:
            km_percorridos = float(self.ids.km_percorridos.text.replace(',', '.'))
            litros_consumidos = float(self.ids.litros_consumidos.text.replace(',', '.'))
            
            consumo = km_percorridos / litros_consumidos
            self.resultado_consumo = f'Consumo médio: {consumo:.2f} km/L'
        except ValueError:
            self.mostrar_erro('Por favor, insira valores numéricos válidos.')
        except ZeroDivisionError:
            self.mostrar_erro('A quantidade de litros não pode ser zero.')
    
    def limpar_campos(self):
        self.ids.km_percorridos.text = ''
        self.ids.litros_consumidos.text = ''
        self.resultado_consumo = ''
    
    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro',
                     content=Label(text=mensagem),
                     size_hint=(None, None), size=(400, 200))
        popup.open()

# Tela para estimativa de gastos
class TelaEstimativaGastos(Screen):
    resultado_estimativa = StringProperty('')
    
    def calcular_estimativa(self):
        try:
            distancia = float(self.ids.distancia.text.replace(',', '.'))
            consumo_medio = float(self.ids.consumo_medio.text.replace(',', '.'))
            preco_combustivel = float(self.ids.preco_combustivel.text.replace(',', '.'))
            
            litros_necessarios = distancia / consumo_medio
            custo_total = litros_necessarios * preco_combustivel
            
            self.resultado_estimativa = f'Litros necessários: {litros_necessarios:.2f} L\nCusto estimado: R$ {custo_total:.2f}'
        except ValueError:
            self.mostrar_erro('Por favor, insira valores numéricos válidos.')
        except ZeroDivisionError:
            self.mostrar_erro('O consumo médio não pode ser zero.')
    
    def limpar_campos(self):
        self.ids.distancia.text = ''
        self.ids.consumo_medio.text = ''
        self.ids.preco_combustivel.text = ''
        self.resultado_estimativa = ''
    
    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro',
                     content=Label(text=mensagem),
                     size_hint=(None, None), size=(400, 200))
        popup.open()

# Gerenciador de telas
class GerenciadorTelas(ScreenManager):
    pass

# Aplicativo principal
class CalculadoraCombustivelApp(App):
    def build(self):
        # Definir cor de fundo da janela
        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        return GerenciadorTelas()

# Executar o aplicativo
if __name__ == '__main__':
    CalculadoraCombustivelApp().run()