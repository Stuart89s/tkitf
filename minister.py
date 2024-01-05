import random

class Minister:
    def __init__(self,
                 name=random.randint(40,80),
                 age=random.randint(20,50),
                 loyalty=random.randint(40,80),
                 honesty=random.randint(40,80),
                 rank=random.randint(1,9),
                 money=random.randint(40,80),
                 genom_a=random.randint(0,100),
                 genom_b=random.randint(0,100),
                 disposition_a=random.randint(0,100),
                 disposition_b=random.randint(0,100),
                 admin=random.randint(40,80),
                 combat=random.randint(40,80),
                 greed=random.randint(40,80),
                 health=random.randint(40,80)):
        self.name = name
        self.loyalty = loyalty
        self.honesty = honesty
        self.disposition_a = disposition_a
        self.disposition_b = disposition_b
        self.genom_a = genom_a
        self.genom_b = genom_b
        self.rank = rank
        self.money = money
        self.age = age
        self.administration = admin
        self.combat = combat
        self.greed = greed
        self.health = health
        self.current_mission = None

    def assign_mission(self, mission):
        self.current_mission = mission
        mission.apply_mission_effects(self)

    def report_mission(self):
        # 충성도와 탐욕에 따른 보고 정확도 결정
        if self.loyalty > 50 and self.greed < 50:
            return f"정확한 보고: {self.current_mission.name} 완료"
        else:
            return f"거짓 보고: {self.current_mission.name} 완료, 개인 이득 취함"

