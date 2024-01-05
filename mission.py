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
    def __init__(self, name, duration, minister, admin_effect, combat_effect, greed_effect, health_effect):
        self.name = name
        self.duration = duration  # 1개월에서 6개월 사이의 정수
        self.admin_effect = admin_effect
        self.combat_effect = combat_effect
        self.greed_effect = greed_effect
        self.health_effect = health_effect
        self.minister =minister
        # self.level = level

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
    def __init__(self, duration, minister):
        super().__init__("호랑이 사냥", duration, minister, admin_effect=0, combat_effect=20, greed_effect=0, health_effect=-30)

        # 미션 성공률 계산
        success_rate = 0.5  # 기본 성공률 50%
        combat_bonus = self.minister.combat / 1000  # 전투력을 100으로 나누어 추가 확률 계산
        success_rate += combat_bonus

        # 미션 성공 여부 결정
        self.mission_success = random.random() < success_rate

    def apply_mission_effects(self):
        # 기본 미션 효과 적용
        super().apply_mission_effects(self.minister)

        # 미션 성공률 계산

        if self.mission_success:
            # 성공 로직
            result = f"호랑이 사냥 성공: 전투력 증가"
            self.minister.combat += random.randint(1, 30)/10
            print(f'combat = {self.minister.combat}')
        else:
            # 실패 로직
            result = f"호랑이 사냥 실패: 추가 건강 감소"
            additional_health_loss = random.randint(10, 20)
            self.minister.health -= additional_health_loss
            print(f'health = {self.minister.health}')

        print(self.report_mission())

        return result

    def report_mission(self):
        honesty_prob = self.minister.honesty / 100
        loyalty_factor = self.minister.loyalty / 100
        greed_factor = 1 - self.minister.greed / 100

        overall_prob = (honesty_prob + loyalty_factor + greed_factor)/3

        if self.mission_success:
            if random.random() < overall_prob:
                report = f"{self.minister.name}은(는) 호랑이 사냥에 성공했다고 정직하게 보고합니다."
            else:
                report = f"{self.minister.name}은(는) 호랑이 사냥에 성공했음에도 불구하고 거짓 보고합니다."
        else:
            if random.random() < overall_prob:
                report = f"{self.minister.name}은(는) 호랑이 사냥에 실패했다고 정직하게 보고합니다."
            else:
                report = f"{self.minister.name}은(는) 호랑이 사냥에 실패했음에도 불구하고 성공했다고 거짓 보고합니다."

        return report