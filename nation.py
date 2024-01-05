import random
from collections import deque

class Tile:
    def __init__(self, x, y, terrain_type):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type  # 'land', 'ocean', 'mountain'
        self.controlled_by = None  # 타일을 지배하는 국가

class Map:
    def __init__(self, size=30, ocean_ratio=0.5, land_ratio=0.4, mountain_ratio=0.1):
        self.size = size
        self.tiles = [[None for _ in range(size)] for _ in range(size)]
        self.create_map(ocean_ratio, land_ratio, mountain_ratio)

    def create_map(self, ocean_ratio, land_ratio, mountain_ratio):
        total_tiles = self.size * self.size
        ocean_tiles = int(total_tiles * ocean_ratio)
        mountain_tiles = int(total_tiles * mountain_ratio)

        # 모든 타일을 육지로 초기화
        for x in range(self.size):
            for y in range(self.size):
                self.tiles[x][y] = Tile(x, y, 'land')

        # 바다 타일 생성
        self.create_terrain(ocean_tiles, 'ocean')
        
        # 산 타일 생성
        self.create_terrain(mountain_tiles, 'mountain')

    def create_terrain(self, terrain_tiles, terrain_type):
        # 초기 바다 타일 생성 (테두리)
        if terrain_type == 'ocean':
            for x in range(self.size):
                for y in range(self.size):
                    if x == 0 or y == 0 or x == self.size - 1 or y == self.size - 1:
                        self.tiles[x][y].terrain_type = 'ocean'
                        terrain_tiles -= 1

        # 추가적인 바다/산 타일 생성
        while terrain_tiles > 0:
            x, y = random.randint(1, self.size - 2), random.randint(1, self.size - 2)
            tile = self.tiles[x][y]
            if tile.terrain_type == 'land':
                tile.terrain_type = terrain_type
                terrain_tiles -= 1

                # 인접한 타일을 바다로 변환 (확산)
                if terrain_type == 'ocean':
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.size and 0 <= ny < self.size:
                            neighbor_tile = self.tiles[nx][ny]
                            if neighbor_tile.terrain_type == 'land':
                                neighbor_tile.terrain_type = 'ocean'
                                terrain_tiles -= 1

class Country:
    def __init__(self, name, symbol):
        self.name = name
        self.territory = []
        self.symbol = symbol

    def add_territory(self, tile):
        self.territory.append(tile)
        tile.controlled_by = self

def assign_territory(world_map, country, start_tile, min_territory=5, max_territory=30):
    queue = deque([start_tile])
    visited = set([start_tile])
    territory_count = random.randint(min_territory, max_territory)

    while queue and len(country.territory) < territory_count:
        current_tile = queue.popleft()
        
        # 육지 타일 확인
        if current_tile.controlled_by is None and current_tile.terrain_type == 'land':
            country.add_territory(current_tile)
        
        # 인접한 타일 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            x, y = current_tile.x + dx, current_tile.y + dy
            if 0 <= x < world_map.size and 0 <= y < world_map.size:
                neighbor_tile = world_map.tiles[x][y]
                if neighbor_tile not in visited:
                    visited.add(neighbor_tile)
                    queue.append(neighbor_tile)



# 국가별 심볼 (예: A, B, C, ...)
symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 지도 생성
world_map = Map()
countries = [Country(f"Country {i+1}", symbols[i]) for i in range(8)]


for country in countries:
    # 무작위 시작 타일 선택
    start_x, start_y = random.randint(0, 29), random.randint(0, 29)
    start_tile = world_map.tiles[start_x][start_y]
    assign_territory(world_map, country, start_tile)

# 지도 출력
def print_map(world_map, countries):
    terrain_symbols = {'land': '.', 'ocean': '~', 'mountain': '^'}
    country_symbols = {country: country.symbol for country in countries}

    for x in range(world_map.size):
        for y in range(world_map.size):
            tile = world_map.tiles[x][y]
            if tile.controlled_by:
                print(country_symbols[tile.controlled_by], end=' ')
            else:
                print(terrain_symbols[tile.terrain_type], end=' ')
        print()

print_map(world_map, countries)

