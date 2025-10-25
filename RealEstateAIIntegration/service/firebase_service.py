import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

class FirebaseService:
    def __init__(self, credential_path):
        try:
            cred = credentials.Certificate(credential_path)
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            print("✅ Firebase connected successfully.")
        except Exception as e:
            print(f"⚠️ Firebase init error: {e}")
            self.db = None

    def log_action(self, user, action_type, details):
        if not self.db:
            print("⚠️ Firebase not connected.")
            return

        entry = {
            "user": user,
            "action_type": action_type,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        self.db.collection("logs").add(entry)
