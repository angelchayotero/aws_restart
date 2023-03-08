userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("vuelve cuando lo requieras")
    exit();

userReply = input("Qué le gustaria comprar estampas, sobre o hacer una copia?")


if userReply == "estampas":
    print("Tenemos muchos diseños")
    
elif userReply == "sobre":
    print("Tenemos muchos sobres")
elif userReply == "copia":
    copies =  input("Cuantas copias quiere sacar?")
    print("Se sacará el número de copias:", copies)
else:
    print("Gracias, vuelva pronto")