#SRARAH NSEREKO A96409
class UserAuthentication:
    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD = "admin"

    @staticmethod
    def perform_login(username, password):
        """Authenticate user."""
        return username == UserAuthentication.DEFAULT_USERNAME and password == UserAuthentication.DEFAULT_PASSWORD

    @staticmethod
    def register(username, password, email):
        """Register a new user."""
        if len(password) < 8:
            return "Password must be at least 8 characters long"
        return "User registered successfully"

class DataManipulation:
    def __init__(self):
        pass
    
    def process_data(self, data):
        # Data processing logic
        processed_data = [item.upper() for item in data]
        return processed_data


class APIIntegration:
    def __init__(self):
        pass
    
    def fetch_data_from_api(self, endpoint):
        # API integration logic
        if endpoint == "/users":
            return ["user1", "user2", "user3"]
        else:
            return None


if __name__ == "__main__":
    # Initialize modules
    auth = UserAuthentication()
    data_processor = DataManipulation()
    api = APIIntegration()

    # Test user authentication
    print(auth.perform_login("admin", "admin"))  # True
    print(auth.perform_login("user", "password"))  # False

    # Test data manipulation
    print(data_processor.process_data(["apple", "banana", "orange"]))  # ['APPLE', 'BANANA', 'ORANGE']

    # Test API integration
    print(api.fetch_data_from_api("/users"))  # ['user1', 'user2', 'user3']
