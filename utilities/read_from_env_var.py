import os


class ReadFromEnvironmentVariable:
    def read_env_var_phone(self):
        env_var_PhoneNumber = os.getenv('phone_number')
        return env_var_PhoneNumber

    def read_env_var_password(self):
        env_var_Password = os.environ.get('daraz_password')
        return env_var_Password