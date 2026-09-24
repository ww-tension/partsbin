# === Stage 34: Add support for multiple local user profiles ===
# Project: PartsBin
class Profile:
    def __init__(self, name, email, password=None):
        self.name = name
        self.email = email
        self.password = password or ""

class ProfileManager:
    def __init__(self):
        self.profiles = []

    def add_profile(self, name, email, password=None):
        if not any(p.name == name for p in self.profiles):
            self.profiles.append(Profile(name, email, password))
            return True
        return False

    def get_profile(self, name):
        for p in self.profiles:
            if p.name == name:
                return p
        return None

    def list_profiles(self):
        return self.profiles
