class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = velocidade


    def get_marca(self):
        return self.__marca
    
    
    def set_marca(self, marca):
        self.__marca = marca


    def get_modelo(self):
        return self.__modelo
    

    def set_modelo(self, modelo):
        self.__modelo = modelo


    def get_ano(self):
        return self.__ano
    

    def set_ano(self, ano):
        self.__ano = ano


    def mostrar_velocidade(self):
        if self.__velocidade == 0:
            print("\nStatus: parado\n O seu veículo não está em movimento no momento.\n")
        
        elif self.__velocidade > 0:
            print(f"\nStatus: em movimento.\n A velocidade atual do veículo é de: {self.__velocidade} km/h.\n")

        else:
            print(f"Veículo {self.__marca} {self.__modelo} não encontrado.\n")
            return
        

    def acelerar(self, incremento):
        self.__velocidade += incremento
        print("\nACELERANDO...\n")


    def frear(self, incremento):
        if self.__velocidade == 0:
            pass


        