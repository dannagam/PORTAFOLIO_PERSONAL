uv=int(input("dime el indice de uv: "))
if uv<=2:
    print("bajo: usa gafas de sol.")
elif uv<=5:
    print("Moderado: aplica bloqueador FPS 20.")
elif uv<=7:
     print("Alto: bloqueador FPS 50 y gorra.")
elif uv<=10:
    print("muy alto: evita el sol al mediodia.")
elif uv>10:
    print("extremo: permanece bajo techo")
    