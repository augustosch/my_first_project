
apetece_helado_input = input("¿Te apetece un helado? (si/no): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO"
    apetece_helado = False
else:
    print("te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (si/no): ").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (si/no)").upper()
esta_tu_tia_input = input("¿Estás con tu tia?").upper()

apetece_helado = apetece_helado_input == "SI"
tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puedes_permitirtelo = tiene_dinero_input or esta_tu_tia_input
esta_el_senor_helados = esta_el_senor_helados_input == "SI"


if apetece_helado and puedes_permitirtelo and esta_el_senor_helados:
    print("pues comete un helado")
else:
    print("pues nada")