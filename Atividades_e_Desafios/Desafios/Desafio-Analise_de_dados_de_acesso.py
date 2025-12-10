registros_acessos = []          
usuarios_sucesso = set()        
tempo_total_sucesso = 0         

while True:
    usuario = input("Informe o nome do usuário (ou digite 0 para encerrar): ").strip()
    if usuario == "0":
        break
    if not usuario:
        print("Aviso: nome de usuário vazio. Registro não realizado.\n")
        continue

    while True:
        print("Selecione o status de acesso:")
        print("1 - Sucesso")
        print("2 - Falha")
        opc = input("Opção escolhida: ").strip()
        if opc in ("1", "2"):
            status = "Sucesso" if opc == "1" else "Falha"
            break
        print("Aviso: opção inválida. Escolha 1 ou 2.")

    try:
        duracao = int(input("Informe a duração da sessão (em minutos): ").strip())
    except ValueError:
        print("Aviso: valor inválido. Utilize apenas números inteiros.\n")
        continue

    if duracao < 0:
        print("Aviso: a duração não pode ser negativa. Registro não realizado.\n")
        continue

    registros_acessos.append((usuario, status, duracao))

    if status == "Sucesso":
        usuarios_sucesso.add(usuario)
        tempo_total_sucesso += duracao

    print("Registro efetuado com sucesso.\n")

print("\n=== Resumo dos Registros de Acesso ===")
for u, s, d in registros_acessos:
    print(f"Usuário: {u} | Status: {s} | Duração: {d} minutos")

print("\n=== Usuários com acesso bem-sucedido ===")
print(", ".join(usuarios_sucesso) if usuarios_sucesso else "Nenhum usuário teve sucesso.")

print(f"\n=== Tempo total das sessões bem-sucedidas: {tempo_total_sucesso} minutos ===")
