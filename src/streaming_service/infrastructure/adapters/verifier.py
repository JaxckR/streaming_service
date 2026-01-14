import bcrypt

from streaming_service.application.ports import Verifier


class VerifierImpl(Verifier):
    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
