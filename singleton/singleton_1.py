class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'

if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'Tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)