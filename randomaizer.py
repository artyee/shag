import random

nomer1 = int(input("Vvedy pershe chyslo "))
nomer2 = int(input("Vvedy druge chyslo "))
vybir_doli = random.randint(nomer1, nomer2)

print("chyslo ", vybir_doli)

if vybir_doli == 1:
    print("викінути 3 гравця за карту")
elif vybir_doli == 2:
    print("розігнатися до надзвукової швидкості")
elif vybir_doli == 3:
    print("еволіціонувати до бекрумса")
elif vybir_doli == 4:
    print("пройти 4 перших кімнат")
elif vybir_doli == 5:
    print("втікти від бактерії в присяді")
elif vybir_doli == 6:
    print("з першого разу пройти 2 лвл")
elif vybir_doli == 7:
    print("залісти на саме високе дерево")
elif vybir_doli == 8:
    print("почати з самого початку в роботі")
elif vybir_doli == 9:
    print("пройти перший рівень без бігу")
elif vybir_doli == 10:
    print("зробити все що ти вже робив до цього")
elif vybir_doli == 0:
    print("перекрут")
elif vybir_doli == -1:
    print("нічого")