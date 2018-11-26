import json
class Response:

    def get_response_ok(self, code, message="ok"):
        return {
            "response": code,
            "alert": message,
        }
    def get_response_error(self, code, message="error"):
        return {
            "response": code,
            "error": message,
        }

    def toJson(self):
        try:
            json.dump(self.get_message())
        except Exception:
            print("Ошибка в конвертации в json")