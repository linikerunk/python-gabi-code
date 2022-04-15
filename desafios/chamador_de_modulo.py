import modulo_power_ranger


if __name__ == '__main__':
    
    class Human():

        def __init__(self, *args, **kwargs):
            self.name = None
            self.color_ranger = None
    
    human = Human()
    human.name = 'Guilherme'
    human.color_ranger = 'Azul'
    
    human2 = Human()
    human2.name = 'Eduardo'
    human2.color_ranger = 'Vermelho'
    
    human3 = Human()
    human3.name = 'S3'
    human3.color_ranger = 'Roxo'
    
    print(modulo_power_ranger.morfar(human.name, human.color_ranger))
    print(modulo_power_ranger.morfar(human2.name, human2.color_ranger))
    print(modulo_power_ranger.morfar(human3.name, human3.color_ranger))