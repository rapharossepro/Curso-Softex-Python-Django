import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email
    
    @property
    def email(self):
        """Getter para ler o email"""
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        """Setter com validação de @"""
        if "@" not in novo_email:
            print("Erro: Email inválido! Deve conter '@'")
            print("O email não foi alterado.")
            return
        self.__email = novo_email
        print("Email atualizado com sucesso!")


class CanalEnvio:
    def enviar(self, mensagem):
        raise NotImplementedError("Método enviar() deve ser implementado na subclasse")


class Email(CanalEnvio):
    def enviar(self, mensagem):
        print(f"Enviando para servidor de email: {mensagem}")


class SMS(CanalEnvio):
    def enviar(self, mensagem):
        print(f"Enviando para operadora telefônica: {mensagem}")


class SistemaAlerta:
    def __init__(self, usuario, canal):
        self.usuario = usuario
        self.canal = canal
    
    def disparar(self, texto):
        print(f"\nNotificando {self.usuario.nome}...", end="")
        time.sleep(1)
        print(" [OK]")
        time.sleep(0.5)
        self.canal.enviar(texto)
        time.sleep(0.5)
        print("Alerta enviado!\n")


def criar_usuario_interativo():
    print("\n" + "=" * 60)
    print("Cadastrar Novo Usuário")
    print("=" * 60)
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    
    print("\nProcessando...", end="")
    time.sleep(1)
    print(" [OK]")
    
    usuario = Usuario(nome, email)
    print(f"\nUsuário '{usuario.nome}' cadastrado!")
    print(f"Email: {usuario.email}")
    time.sleep(1)
    
    return usuario


def alterar_email_interativo(usuario):
    print("\n" + "=" * 60)
    print("Alterar Email")
    print("=" * 60)
    print(f"Email atual: {usuario.email}")
    novo_email = input("Digite o novo email: ")
    
    print("\nValidando...", end="")
    time.sleep(1)
    print(" [OK]")
    
    usuario.email = novo_email
    time.sleep(0.5)


def enviar_alerta_interativo(usuario):
    print("\n" + "=" * 60)
    print("Enviar Alerta")
    print("=" * 60)
    print("Escolha o canal de envio:")
    print("1 - Email")
    print("2 - SMS")
    
    opcao = input("\nOpção: ")
    
    if opcao == "1":
        canal = Email()
        tipo = "Email"
    elif opcao == "2":
        canal = SMS()
        tipo = "SMS"
    else:
        print("Opção inválida!")
        time.sleep(1)
        return
    
    mensagem = input("\nDigite a mensagem do alerta: ")
    
    print(f"\nPreparando envio via {tipo}...", end="")
    time.sleep(1)
    print(" [OK]")
    
    sistema = SistemaAlerta(usuario, canal)
    sistema.disparar(mensagem)
    time.sleep(1)


def menu_interativo():
    usuario = None
    
    while True:
        print("\n" + "=" * 60)
        print("MENU INTERATIVO")
        print("=" * 60)
        print("1 - Cadastrar novo usuário")
        print("2 - Alterar email do usuário")
        print("3 - Enviar alerta")
        print("4 - Exibir dados do usuário")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            usuario = criar_usuario_interativo()
        
        elif opcao == "2":
            if usuario is None:
                print("\nErro: Nenhum usuário cadastrado!")
                time.sleep(1)
            else:
                alterar_email_interativo(usuario)
        
        elif opcao == "3":
            if usuario is None:
                print("\nErro: Nenhum usuário cadastrado!")
                time.sleep(1)
            else:
                enviar_alerta_interativo(usuario)
        
        elif opcao == "4":
            if usuario is None:
                print("\nErro: Nenhum usuário cadastrado!")
                time.sleep(1)
            else:
                print("\n" + "=" * 60)
                print("DADOS DO USUÁRIO")
                print("=" * 60)
                print(f"Nome: {usuario.nome}")
                print(f"Email: {usuario.email}")
                time.sleep(2)
        
        elif opcao == "0":
            print("\nEncerrando sistema...", end="")
            time.sleep(1)
            print(" [OK]")
            print("Sistema encerrado.")
            break
        
        else:
            print("\nOpção inválida!")
            time.sleep(1)


if __name__ == "__main__":
    print("=" * 60)
    print("Testes do Sistema de Notificações - POO em Python")
    print("=" * 60)
    
    print("\n[TESTE 1] Segurança do Encapsulamento")
    print("-" * 60)
    
    print("\nCriando usuário...")
    time.sleep(1)
    usuario1 = Usuario("João Silva", "joao@empresa.com")
    print(f"Usuário criado: {usuario1.nome}")
    print(f"Email atual: {usuario1.email}")
    
    print("\n>>> Tentando alterar para email INVÁLIDO (sem @)...")
    time.sleep(1)
    usuario1.email = "emailinvalido.com"
    print(f"Email após tentativa: {usuario1.email}")
    
    print("\n>>> Tentando alterar para email VÁLIDO...")
    time.sleep(1)
    usuario1.email = "joao.novo@empresa.com"
    print(f"Email após alteração: {usuario1.email}")
    
    time.sleep(2)
    
    print("\n" + "=" * 60)
    print("[TESTE 2] Envio via Email")
    print("-" * 60)
    
    print("\nInstanciando canal Email...")
    time.sleep(1)
    canal_email = Email()
    
    print("Criando SistemaAlerta com canal Email...")
    time.sleep(1)
    sistema_email = SistemaAlerta(usuario1, canal_email)
    
    print("\nDisparando alerta via Email...")
    time.sleep(1)
    sistema_email.disparar("Servidor principal voltou ao normal")
    
    time.sleep(2)
    
    print("=" * 60)
    print("[TESTE 3] Polimorfismo - Trocando para SMS")
    print("-" * 60)
    
    print("\nInstanciando canal SMS...")
    time.sleep(1)
    canal_sms = SMS()
    
    print("Criando SistemaAlerta com canal SMS...")
    time.sleep(1)
    sistema_sms = SistemaAlerta(usuario1, canal_sms)
    
    print("\nDisparando alerta via SMS...")
    time.sleep(1)
    sistema_sms.disparar("Pagamento aprovado com sucesso")
    
    time.sleep(2)
    
    print("=" * 60)
    print("Teste concluído!")
    print("=" * 60)
    
    print("\nObservações importantes:")
    print("  1. Encapsulamento: O email está protegido com '__' e validação")
    print("  2. Herança: Email e SMS herdam de CanalEnvio")
    print("  3. Polimorfismo: Trocamos Email por SMS sem mudar o código do sistema")
    print("  4. Composição: SistemaAlerta usa objetos Usuario e Canal")
    
    time.sleep(2)
    
    print("\n" + "=" * 60)
    print("Modo Interativo - Teste você mesmo!")
    print("=" * 60)
    
    menu_interativo()