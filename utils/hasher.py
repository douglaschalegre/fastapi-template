import bcrypt


class Hasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Check if plain password is the one hashed"""
        password_byte_enc = plain_password.encode('utf-8')
        hashed_password_byte = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_byte)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Hash password"""
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode('utf-8')
