#Lab: 모든 조합 출력하기

persons = ["Kim","Park","Lee"]
retaurants = ["Korean","American","French"]

for person in persons:
    for restaurant in retaurants:
        print(person + "이" + restaurant+"식당을 방문")