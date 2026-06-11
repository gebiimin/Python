import random


def print_status(player):
    print("\n=== 상태 ===")
    print(f"이름: {player['name']}")
    print(f"레벨: {player['level']}")
    print(f"체력: {player['hp']} / {player['max_hp']}")
    print(f"공격력: {player['attack']}")
    print(f"골드: {player['gold']}")
    print(f"물약: {player['potions']}개")


def create_monster(player_level):
    monsters = [
        {"name": "슬라임", "hp": 20, "attack": 5, "gold": 8},
        {"name": "고블린", "hp": 30, "attack": 7, "gold": 12},
        {"name": "늑대", "hp": 25, "attack": 9, "gold": 10},
    ]

    monster = random.choice(monsters).copy()
    monster["hp"] += player_level * 5
    monster["attack"] += player_level * 2
    monster["gold"] += player_level * 3
    return monster


def use_potion(player):
    if player["potions"] <= 0:
        print("물약이 없습니다!")
        return

    heal = 30
    player["potions"] -= 1
    player["hp"] = min(player["max_hp"], player["hp"] + heal)
    print(f"물약을 사용했습니다. 체력이 {heal} 회복되었습니다.")


def battle(player):
    monster = create_monster(player["level"])
    print(f"\n야생의 {monster['name']}이(가) 나타났습니다!")

    while player["hp"] > 0 and monster["hp"] > 0:
        print(f"\n{player['name']} 체력: {player['hp']}")
        print(f"{monster['name']} 체력: {monster['hp']}")
        print("1. 공격")
        print("2. 물약 사용")
        print("3. 도망")

        choice = input("행동을 선택하세요: ")

        if choice == "1":
            damage = random.randint(player["attack"] - 3, player["attack"] + 3)
            damage = max(1, damage)
            monster["hp"] -= damage
            print(f"{monster['name']}에게 {damage} 피해를 주었습니다!")

            if monster["hp"] <= 0:
                print(f"{monster['name']}을(를) 물리쳤습니다!")
                player["gold"] += monster["gold"]
                print(f"{monster['gold']} 골드를 얻었습니다.")
                level_up(player)
                return

        elif choice == "2":
            use_potion(player)
        elif choice == "3":
            if random.random() < 0.5:
                print("도망에 성공했습니다!")
                return
            print("도망에 실패했습니다!")
        else:
            print("잘못된 입력입니다.")
            continue

        monster_damage = random.randint(monster["attack"] - 2, monster["attack"] + 2)
        monster_damage = max(1, monster_damage)
        player["hp"] -= monster_damage
        print(f"{monster['name']}에게 {monster_damage} 피해를 받았습니다.")

    if player["hp"] <= 0:
        print("\n쓰러졌습니다... 마을에서 회복합니다.")
        player["hp"] = player["max_hp"]
        player["gold"] = max(0, player["gold"] - 10)


def level_up(player):
    player["exp"] += 1

    if player["exp"] >= player["level"]:
        player["exp"] = 0
        player["level"] += 1
        player["max_hp"] += 10
        player["attack"] += 3
        player["hp"] = player["max_hp"]
        print(f"레벨 업! 현재 레벨은 {player['level']}입니다.")


def shop(player):
    while True:
        print("\n=== 상점 ===")
        print("1. 물약 구매 (10 골드)")
        print("2. 여관에서 회복 (5 골드)")
        print("3. 나가기")

        choice = input("선택하세요: ")

        if choice == "1":
            if player["gold"] >= 10:
                player["gold"] -= 10
                player["potions"] += 1
                print("물약을 1개 구매했습니다.")
            else:
                print("골드가 부족합니다.")
        elif choice == "2":
            if player["gold"] >= 5:
                player["gold"] -= 5
                player["hp"] = player["max_hp"]
                print("체력을 모두 회복했습니다.")
            else:
                print("골드가 부족합니다.")
        elif choice == "3":
            return
        else:
            print("잘못된 입력입니다.")


def main():
    print("=== 작은 파이썬 RPG ===")
    name = input("용사의 이름을 입력하세요: ")

    player = {
        "name": name,
        "level": 1,
        "exp": 0,
        "hp": 100,
        "max_hp": 100,
        "attack": 12,
        "gold": 20,
        "potions": 2,
    }

    while True:
        print("\n=== 마을 ===")
        print("1. 모험 떠나기")
        print("2. 상점 가기")
        print("3. 상태 보기")
        print("4. 게임 종료")

        choice = input("선택하세요: ")

        if choice == "1":
            battle(player)
        elif choice == "2":
            shop(player)
        elif choice == "3":
            print_status(player)
        elif choice == "4":
            print("게임을 종료합니다. 다음 모험에서 만나요!")
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
