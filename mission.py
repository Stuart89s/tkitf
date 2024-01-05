import random

class GameState:
    special_events_triggered = {}

# 특별 이벤트 트리거 함수
def trigger_special_event(mission_name):
    if mission_name not in GameState.special_events_triggered:
        if random.random() < 0.01:  # 1% 확률
            GameState.special_events_triggered[mission_name] = True
            return True
    return False


class Mission:
    def __init__(self, name, duration, admin_effect, combat_effect, greed_effect, health_effect):
        self.name = name
        self.duration = duration  # 1개월에서 6개월 사이의 정수
        self.admin_effect = admin_effect
        self.combat_effect = combat_effect
        self.greed_effect = greed_effect
        self.health_effect = health_effect

    def apply_mission_effects(self, minister):
        minister.administration += self.admin_effect
        minister.combat += self.combat_effect
        minister.greed += self.greed_effect
        minister.health -= self.health_effect  # 건강 감소는 음수로 처리

    def trigger_special_event_effect(self, minister):
        # 특별 이벤트 효과 적용 로직
        pass
    

# 시장 개발 미션
class MarketDevelopmentMission(Mission):
    def __init__(self, duration):
        super().__init__("시장 개발", duration, admin_effect=10, combat_effect=0, greed_effect=20, health_effect=0)

    def apply_mission_effects(self, minister):
        # 시장 개발 특유의 효과를 적용하는 특별한 로직
        super().apply_mission_effects(minister)
        # 추가적인 효과가 필요하다면 여기에 구현

# 호랑이 사냥 미션
class TigerHuntMission(Mission):
    def __init__(self, duration):
        super().__init__("호랑이 사냥", duration, admin_effect=0, combat_effect=20, greed_effect=0, health_effect=-30)

    def apply_mission_effects(self, minister):
        # 호랑이 사냥 특유의 효과를 적용하는 특별한 로직
        super().apply_mission_effects(minister)
        # 추가적인 효과가 필요하다면 여기에 구현
