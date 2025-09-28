from abc import abstractmethod
from typing import override

class BaseCharacter:
    @abstractmethod
    def get_name(self) -> str:
        pass

class BaseInActionCharacter:
    pass

class BaseCosplayer:
    pass

class BaseHuman:
    @abstractmethod
    def isHuman(self) -> bool:
        pass

class BaseFunkoPop:
    @abstractmethod
    def display(self) -> None:
        pass

class MixinSpeakable:
    @abstractmethod
    def speaking(self) -> None:
        pass

class MixinAnimated:
    @abstractmethod
    def is_animated(self) -> bool:
        pass
        
class MixinFunny:
    @abstractmethod
    def makes_laugh(self) -> None:
        pass
        
class MixinActionable:
    @abstractmethod
    def performs_action(self) -> None:
        pass
        
class MixinCollectible:
    @abstractmethod
    def is_collectible(self) -> bool:
        pass
        
class MixinPoseable:
    @abstractmethod
    def poseable(self) -> None:
        pass
        
class MixinCostumeWearable:
    @abstractmethod
    def costume_wearing(self) -> str:
        pass
        
class Shrek(BaseCharacter, MixinSpeakable, MixinAnimated, MixinFunny):
    def get_name(self):
        return 'Shrek'
    def speaking(self):
        return '2 просьбы: заткни хлЕБАЛО и поищи лестницу!'
    def is_animated(self):
        return True
    def makes_laugh(self):
        return 'hahaha, поверил, ну и бредятина!'
    
class PussInBoots(BaseCharacter, MixinSpeakable, MixinAnimated, MixinFunny):
    def get_name(self):
        return 'Puss In Boots'
    def speaking(self):
        return 'бойтесь суки я кот with шпага'
    def is_animated(self):
        return True
    def makes_laught(self):
        return 'hahaha meow meow'

class JackHorner(BaseCharacter, MixinSpeakable, MixinAnimated):
    def get_name(self):
        return 'Jack Horner'
    def speaking(self):
        return 'вам пизда'
    def is_animated(self):
        return True
    
class Donkey(BaseCharacter, MixinSpeakable, MixinAnimated, MixinFunny):
    def get_name(self):
        return 'Donkey'
    def speaking(self):
        return 'мы уже приехали?'
    def is_animated(self):
        return True
    def makes_laught(self):
        return 'hahaha я osyol'
    
class ShrekInAction(MixinActionable, BaseInActionCharacter):
    def performs_action(self):
        return 'Shrek SMASH'
    def get_name(self):
        return 'Shrek In Action'

class DonkeyInAction(MixinActionable, BaseInActionCharacter):
    def performs_action(self):
        return 'osyol makes osyol noices'
    def get_name(self):
        return 'Donkey In Action'
    
class PussInBootsInAction(MixinActionable, BaseInActionCharacter):
    def performs_action(self):
        return 'makes моська'
    def get_name(self):
        return 'Puss In Boots In Action'
    
class JackHornerInAction(MixinActionable, BaseInActionCharacter):
    def performs_action(self):
        return 'do some bad guy stuff'
    def get_name(self):
        return 'Jack Horner In Action'
    
class ShrekFunkoPop(MixinCollectible, BaseFunkoPop):
    def get_name(self):
        return 'Shrek FunkoPOP'
    def is_collectible(self):
        return True
    def display(self):
        return 'Displaying Funko: Shrek'

class DonkeyFunkoPop(MixinCollectible, BaseFunkoPop):
    def get_name(self):
        return 'Donkey FunkoPOP'
    def is_collectible(self):
        return True
    def display(self):
        return 'Displaying Funko: Donkey'

class PussInBootsFunkoPop(MixinCollectible, BaseFunkoPop):
    def get_name(self):
        return 'Puss In Boots FunkoPOP'
    def is_collectible(self):
        return True
    def display(self):
        return 'Displaying Funko: Puss In Boots'

class JackHornerFunkoPop(MixinCollectible, BaseFunkoPop):
    def get_name(self):
        return 'Jack Horner FunkoPOP'
    def is_collectible(self):
        return True
    def display(self):
        return 'Displaying Funko: Egg-Head'

class ShrekCosplayer(MixinPoseable, MixinCostumeWearable, BaseHuman, BaseCosplayer):
    def isHuman(self):
        return True
    def get_name(self):
        return 'Shrek Cosplayer'
    def poseable(self):
        return 'Poses as Shrek'
    def costume_wearing(self):
        return 'Wearing Green costume'

class DonkeyCosplayer(MixinPoseable, MixinCostumeWearable, BaseHuman, BaseCosplayer):
    def isHuman(self):
        return True
    def get_name(self):
        return 'Donkey Cosplayer'
    def poseable(self):
        return 'Poses as donkey animal'
    def costume_wearing(self):
        return 'Wearing funny osyol costume'
    
class PussInBootsCosplayer(MixinPoseable, MixinCostumeWearable, BaseHuman, BaseCosplayer):
    def isHuman(self):
        return True
    def get_name(self):
        return 'Pussy Cosplayer'
    def poseable(self):
        return 'Poses as cat animal'
    def costume_wearing(self):
        return 'Wearing cool cat costume'

class JackHornerCosplayer(MixinPoseable, MixinCostumeWearable, BaseHuman, BaseCosplayer):
    def isHuman(self):
        return True
    def get_name(self):
        return 'Bad Guy Cosplayer'
    def poseable(self):
        return 'Poses as Bad Guy'
    def costume_wearing(self):
        return 'Wearing some shit'

if __name__ == "__main__":
    shrek = Shrek()
    print(shrek.speaking())
    print("чо шрек внатуре ANIMATED?", shrek.is_animated())
    print(shrek.makes_laugh())