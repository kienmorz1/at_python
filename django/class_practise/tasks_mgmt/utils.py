import bcrypt


class BcryptPasswordUtil:
    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode("utf-8")
        if len(password_bytes) > 72:
            raise ValueError("Password must be at most 72 bytes when encoded as UTF-8")
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        password_bytes = password.encode("utf-8")
        if len(password_bytes) > 72 or not hashed_password:
            return False
        return bcrypt.checkpw(password_bytes, hashed_password.encode("utf-8"))
