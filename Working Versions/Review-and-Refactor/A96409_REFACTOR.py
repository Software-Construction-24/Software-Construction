class UserManager:
  """Manages user authentication and data processing."""

  def __init__(self):
    self.users = {}  # Empty dictionary to store user data (YAGNI)

  def is_valid_password(self, password):
    """Checks if password meets minimum length requirement."""
    return len(password) >= 8

  def authenticate(self, username, password):
    """Authenticates user based on username and password."""
    if username not in self.users:
      return False  # User not found
    return self.users[username]["password"] == password

  def register(self, username, password, email):
    """Registers a new user and validates password length."""
    if not self.is_valid_password(password):
      return "Password must be at least 8 characters long"
    self.users[username] = {"password": password, "email": email}
    return "User registered successfully"

  def process_data(self, data):
    """Processes data by converting to uppercase (can be extended)."""
    return [item.upper() for item in data]

# Original code for API integration module (unchanged)
class APIIntegration:
  def __init__(self):
    pass
  def fetch_data_from_api(self, endpoint): # API integration logic
    if endpoint == "/users":
      return ["user1", "user2", "user3"]
    else:
      return None
    
# Original usage example (modified)
if __name__ == "__main__":
  # Initialize user manager
  user_manager = UserManager()
  api = APIIntegration()

  # Test user authentication
  print(user_manager.authenticate("admin", "admin"))  # True
  print(user_manager.authenticate("user", "password"))  # False

  # Test user registration (assuming registration is not implemented yet)
  print(user_manager.register("new_user", "short", "email@example.com"))  # Password too short
  print(user_manager.register("another_user", "valid_password", "another@example.com"))  # User registered successfully

  # Test data manipulation
  print(user_manager.process_data(["apple", "banana", "orange"]))  # ['APPLE', 'BANANA', 'ORANGE']

  # Test API integration (unchanged)
  print(api.fetch_data_from_api("/users"))  # ['user1', 'user2', 'user3']
