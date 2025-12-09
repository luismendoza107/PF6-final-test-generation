import requests

def dish_fetch(num):  
    mis_platos = {
        1: "Ajiaco - Bogotá",
        2: "Bandeja Paisa - Antioquia", 
        3: "Sancocho - Todo Colombia"
    }
    
    plato = mis_platos.get(num, "No existe")
    
    try:
        datos = requests.get("https://api-colombia.com/api/v1/Department").json()
        
        for depto in datos:

            if "Bogotá" in plato and "Bogotá" in depto["name"]:
                return {
                    "nombre": "Ajiaco Bogotano 🇨🇴",
                    "lugar": depto["name"],
                    "info": depto["description"][:100] + "..."
                }
            elif "Antioquia" in plato and "Antioquia" in depto["name"]:
                return {
                    "nombre": "Bandeja Paisa ",
                    "lugar": depto["name"],
                    "info": depto["description"][:100] + "..."
                }
    except:
        pass
    

    return {
        "nombre": plato, 
        "lugar": "Colombia", 
        "info": "¡Delicioso plato colombiano!"
    }

def main():
    print("¡Hola, estudiantes! 🇨🇴")
    
    while True:
        print("\n1. Ajiaco  2. Bandeja  3. Sancocho  0.Salir")
        opcion = input("Elige: ")
        
        if opcion == "0":
            break
        elif opcion in ["1", "2", "3"]:
            plato = dish_fetch(int(opcion))
            print(f"\n¡{plato['nombre']} de {plato['lugar']}!")
            print(f" {plato['info']}")
        else:
            print("Número malo")

if __name__ == "__main__":
    main()
