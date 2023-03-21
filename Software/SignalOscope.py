from machine import Pin, ADC, I2C
from time import sleep_ms, ticks_ms
from ssd1306 import SSD1306_I2C
# from screens import load_screen, interface_screen
import framebuf


class Configs():
    # pins
    amplitude_pot_pin: int
    frequency_pot_pin: int
    input_pin: int
    sda_oled_pin: int
    scl_oled_pin: int
    
    # consts
    max_amplitude: float
    min_amplitude: float
    max_frequency: float
    min_frequency: float
    oled_height: int
    oled_width: int
    
    def __init__(self) -> None:
        pass
    
    
    def default(self) -> None:
        self.amplitude_pot_pin = 26
        self.frequency_pot_pin = 27
        self.input_pin = 28
        self.sda_oled_pin = 0
        self.scl_oled_pin = 1
        self.oled_height = 32
        self.oled_width = 128
        
        self.max_amplitude = 3.3
        self.min_amplitude = 0
        self.max_frequency = 0.1
        self.min_frequency = 1 / 0.018


class Machine():
    ## options
    configs: Configs
    
    ## calculated
    mv: float
    mf: float
    
    ## states
    frequency: float
    ampliude: float
    sample: list
    
    ## pins
    amplitude_pot: Pin
    frequency_pot: Pin
    input_pin: Pin
    
    ## objects
    oled: SSD1306_I2C
    
    ## screens
    # load_arr: list = load_screen
    # interface_arr: list = interface_screen
    
    ## init
    def __init__(self, configs: Configs, setup: any, loop: any) -> None:
        # options
        self.configs = configs
        
        # calculated
        self.mv = (configs.max_amplitude - configs.min_amplitude) / 2**16
        self.mf = (configs.max_frequency - configs.min_frequency) / 2**16
        
        ## hooks
        self.setup = setup
        self.loop = loop
        
        #
        
        # i2c = I2C(sda = configs.sda_oled_pin, scl = configs.scl_oled_pin)
        
        # self.oled = SSD1306_I2C(128, 32, i2c)
        
    # getters
    def getAmplitude(self) -> float:
        return self.mv * self.voltage_pot.value() + self.min_voltage
    
    def getFrequency(self) -> float:
        return self.mf * self.frequency_pot.value() + self.min_frequency
    
    def getSample(self) -> float:
        pass
    
    
    ## events
    def onSampled(self) -> bool:
        return op != self.getOption()
    
    # hooks
    def start(self) -> None:
        self.begin()
        self.setup(self)
        while True:
            self.step()
            self.loop(self)
    
    
    def begin(self) -> None:
        self.op = self.getOption()
    
    
    def step(self) -> None: 
        if self.otionChanged():
            pass
            
    ## program 
    def setup(self) -> None:
        pass

    def loop(self) -> None:
        pass
    
    ## hooks
        
        
        

