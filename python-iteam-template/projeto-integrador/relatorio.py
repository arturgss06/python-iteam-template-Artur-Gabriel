def mostrar_resultado(candidatos): 
    print("\n RESULTADO FINAL ") 
    
    vencedor = None 
    maior_votos = -1 
    
    for candidato in candidatos: 
        print(f"{candidato.nome}: {candidato.votos} voto(s)") 
        
        if candidato.votos > maior_votos: 
            maior_votos = candidato.votos 
            vencedor = candidato 
            
            if vencedor:
                print(f"\nVencedor: {vencedor.nome}")