import random

class Minister:
    def __init__(self, name, age, loyalty, honesty, rank, money, genom_a, genom_b, disposition_a, disposition_b, admin, combat, greed, health):
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

