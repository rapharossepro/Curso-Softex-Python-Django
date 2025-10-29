# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:
    def __init__(self):
        """
        Cria um atributo que receberá a UserModel como composição
        """
        self.user_model = UserModel()

    def _safe_user_data(self, user) -> dict | None:
        """
        Método privado que recebe um usuário do banco.
        Verifica se o usuário existe e retorna ele sem a senha.
        Caso não exista, retorna None.
        """
        if user:
            return {
                'id': user['id'],
                'email': user['email'],
                'nome_completo': user['nome_completo'],
                'perfil_acesso': user['perfil_acesso'],
                'data_criacao': user['data_criacao'],
                'data_atualizacao': user['data_atualizacao']
            }
        return None

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        """
        Verifica permissões do usuário.
        """
        if current_user_profile == 'Diretoria':
            return True
        if not target_user_id:
            return False
        if action == "edit_self":
            return current_user_id == target_user_id
        return False

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        """
        Cria um novo usuário com validações básicas.
        """
        # Validação da senha
        if len(senha) < 8:
            return False, "A senha deve ter no mínimo 8 caracteres."

        # Validação do email
        if len(email) < 10 or "@" not in email or not email.endswith(".com"):
            return False, "E-mail inválido."

        # Validação do nome
        if not nome_completo.replace(" ", "").isalpha():
            return False, "O nome deve conter apenas letras e não pode estar vazio."

        # Criptografa e cria o usuário
        senha_hash = hash_senha(senha)
        return self.user_model.create_user(senha_hash, email, nome_completo, perfil)

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Login do usuário. Verifica e retorna dados seguros.
        """
        if not email or not senha:
            return None, "Email e senha são obrigatórios."

        user = self.user_model.find_user_by_email(email)
        if not user:
            return None, "Usuário não encontrado."

        if verificar_senha(senha, user['senha']):
            return self._safe_user_data(user), "Login bem-sucedido!"
        return None, "Senha incorreta."

    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        """
        Atualiza dados do usuário.
        """
        if not self._is_authorized(current_user_id, current_user_profile, target_user_id, "edit_self"):
            return False, "Acesso negado!"

        update_data = {}

        if new_data.get('senha'):
            if len(new_data['senha']) < 8:
                return False, "A nova senha deve ter no mínimo 8 caracteres."
            update_data['senha'] = hash_senha(new_data['senha'])

        if new_data.get('nome_completo'):
            update_data['nome_completo'] = new_data['nome_completo']

        if new_data.get('email'):
            update_data['email'] = new_data['email']

        if not update_data:
            return False, "Nada para atualizar."

        return self.user_model.update_user_by_id(target_user_id, update_data)

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        """
        Deleta usuários (apenas Diretoria pode).
        """
        if current_user_profile != "Diretoria":
            return False, "Acesso negado!"
        return self.user_model.delete_user_by_id(user_id)

    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Retorna usuário pelo ID (sem senha).
        """
        user = self.user_model.get_user_by_id(user_id)
        return self._safe_user_data(user)

    def get_all_users(self) -> list[dict | None]:
        """
        Retorna todos os usuários (sem senhas).
        """
        users = self.user_model.get_all_users()
        return [self._safe_user_data(u) for u in users if u]
