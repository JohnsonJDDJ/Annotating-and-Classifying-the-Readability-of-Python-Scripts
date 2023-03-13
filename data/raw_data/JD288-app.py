import essential as x
import sqlite3
import rituais

def app():
    isRunning = True
    command = ""
    
    while isRunning:
        
        x.clear()
        
        if command == "": 
            ficha()
        
        if command == "rituais": 
            rituais.menu_rituais()
            command = ""
            continue
        
        
        command = input("""
comandos:
[rituais] - menu de rituais
[habilidades] - menu de habilidades
[poderes] - menu de poderes
[editar] - editar informações da ficha
[exit] - fechar aplicação

insira um comando: """)
        
        if command.lower() == "exit":
            isRunning = False

def ficha():
    conn = sqlite3.connect(x.DBPATH)
    cur = conn.cursor()

    query = f"SELECT * FROM usuario WHERE id = 1"
    cur.execute(query)
    
    user = cur.fetchone()
    
    rituais = eval(user[3])
    # TODO: Habilidades e poderes
    habilidades = eval(user[4])
    poderes = eval(user[5])
    status = eval(user[6])
    ritual_text = ""
    
    ritual_ids = []
    
    if len(rituais) > 0:
        for ritual in rituais:
            ritual_ids.append(ritual['id'])
        
        ids_tuple = tuple(ritual_ids)
        query = f"SELECT * FROM rituais WHERE id IN {ids_tuple}"
        
        cur.execute(query)
        rituais_list = cur.fetchall()
        
        index = 0
        # TODO: aguardar complemento dos rituais
        for ritual in rituais_list:
            ritual_text += f"\n[{index + 1}] - [{ritual[1]}] "
            index += 1
        
    else: ritual_text += "\nNão tem rituais"
    
    print(f"""
             vida: {status['hp']}/{status['hp_atual']}
         sanidade: {status['sn']}/{status['sn_atual']}
pontos de esforço: {status['pe']}/{status['pe_atual']}
=========================================================
rituais: {ritual_text}
    """)