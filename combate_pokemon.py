
pokemon_elegido = input("¿Contra que pokemos quieres combatir? (Squirtle / Charmander / Bullbasaur)")

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_ele
    nombre_pokemon gido == "Charmander":
    vida_enemigo = 80= "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "Bullbasaur":
    vida_enemigo = 100
    nombre_pokemon = "Bullbasaur"
    ataque_pokemon = 10



while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vamos a usar? (chispazo / bola voltio)")

    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12
    #
        print ("La vida del {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

       print("{} te hace un ataque de 8 de daño".format(nombre_pokemon)
       vida_pikachu -= ataque_pokemon

       print("Tu vida ahora es de {}"r.fomat(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")

if  vida_pikachu <= 0:
    print("¡Has perdido!")

