def rol():
    try:
        print("Introduzca los atributos del personaje: ")
        fza = float(input("Fuerza: "))
        dex = float(input("Agilidad: "))
        sta = float(input("Aguante: "))
        fda = float(input("Fuerza del arma: "))
        pda = float(input("Peso del arma: "))

        pj = {
        "Fuerza": fza,
        "Agilidad": dex,
        "Aguante": sta,
        "Fuerza del arma": fda,
        "Peso del arma": pda
        }

        print(f"El personaje tiene los siguientes atributos: {pj}")
        
        print("Introduzca los atributos del enemigo: ")
        enemy_sta = float(input("Aguante: "))
        enemy_dex = float(input("Agilidad: "))
        enemy_shield = float(input("Escudo: "))
        enemy_health = float(input("Vida: "))

        pj_enemigo = {
        "Aguante": enemy_sta,
        "Agilidad": enemy_dex,
        "Escudo": enemy_shield,
        "Vida": enemy_health,
        }

        print(f"El enemigo tiene los siguientes atributos: {pj_enemigo}")

        suerte = int(input("Introduzca el valor del dado de la suerte: "))
        if suerte >= 5:
            print("BENDICIÓN DIVINA! El ataque atravesará el escudo enemigo.")
        punteria = int(input("Introduzca el valor del dado de la puntería: "))

        base_damage = (fza + dex) - (pda % sta)
        if pda % fda == 0:
            bonificacion_por_arma_equilibrada = ((base_damage * 3) / 100)
            base_damage += bonificacion_por_arma_equilibrada
            print(f"BONIFICACIÓN POR ARMA EQUILIBRADA! +{bonificacion_por_arma_equilibrada} de ataque.")
        elif fza < pda:
            penalidad_por_exceso_de_peso = ((fda * 2) / 100)
            base_damage = (base_damage - penalidad_por_exceso_de_peso)
            print(f"PENALIDAD POR EXCESO DE PESO! -{penalidad_por_exceso_de_peso} de ataque.")
        elif punteria % 2 == 0:
            base_damage = (base_damage + punteria)
        elif suerte >= 5:
            enemy_shield = 0

        defensa_enemigo = (enemy_sta * enemy_dex) + (enemy_shield + (enemy_shield / 2))
        damage_dealt = base_damage - defensa_enemigo
        if damage_dealt < 0:
            damage_dealt = 0
        else:
            enemy_health = enemy_health - damage_dealt
        print(f"""
            1. Nuestro daño de ataque es de: {base_damage}
            2. El puntaje de defensa del enemigo es de: {defensa_enemigo}
            3. El valor de la vida del enemigo luego de aplicar el daño es de: {enemy_health}
            """)
        if enemy_health <= 0:
            print("El enemigo ha muerto!")
    except:
        print("Valor incorrecto")
        rol()
rol()