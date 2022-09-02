


class Colors:
    success = '\033[92m'
    warning = '\033[93m'
    header = '\033[95m'
    error = '\033[91m'
    white = '\033[0m'
    white_bold = '\033[1m'


class Logger():
    """Intern logger to log messages, debugging in cmd with custom colors."""

    @staticmethod
    def success(message_with_color: str, message: str) -> None:
        print(f"$ 🎉 {Colors.success}{message_with_color}: {Colors.white}" + message + '\n')

    @staticmethod
    def warning(message_with_color: str, message: str) -> None:
        print(f"$ ⛔ {Colors.success}{message_with_color}: {Colors.white}" + message + '\n')

    @staticmethod
    def error(message_with_color: str, message: str) -> None:
        print(f"$ 💣 {Colors.error}{message_with_color}: {Colors.white}" + message + '\n')

    @staticmethod
    def doc(message_with_color: str, message: str) -> None:
        print(f"$ ✨ {Colors.success}{message_with_color}: {Colors.white}" + message + '\n')

    @staticmethod
    def header(message_with_color: str, message: str) -> None:
        print(f"$ 🗣️  {Colors.header}{message_with_color}: {Colors.white}" + message + '\n')
