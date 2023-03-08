import traceback
import sys
import shutil
import linecache


class TextStyle:
	# COLORS
	BLUE = "\033[94m"
	AQUA = "\033[96m"
	LIGHT_RED = "\033[91m"
	DARK_RED = "\033[31m"
	YELLOW = "\033[93m"
	GOLD = "\033[33m"
	DARK_GREEN = "\033[32;1m"
	LIGHT_GREEN = "\033[92m"

	# STYLES
	RESET = "\033[0m"
	BOLD = "\033[1m"


class konsole:
	terminal = sys.stdout.write
	style = TextStyle
	debug = True	


	@classmethod
	def format_print(cls, texts: list, title: str = None, title_color = style.YELLOW, text_color = style.GOLD):
		if title != None:
			term_width = shutil.get_terminal_size().columns
			separator = title_color + cls.style.BOLD + "=" * term_width
			header = f"||{title.center(term_width-len(title))}||"
			inner_separator = "-" * (term_width-4)
			formatted_texts = []
			for text in texts:
				if len(text) > term_width - 8:
					lines = [text[i:i+term_width-8] for i in range(0, len(text), term_width-8)]
					formatted_texts.extend([f"|| > {cls.style.RESET}{text_color}{line.ljust(term_width-7)}{title_color}{cls.style.BOLD}||" for line in lines])
				else:
					formatted_texts.append(f"|| > {cls.style.RESET}{text_color}{text.ljust(term_width-7)}{title_color}{cls.style.BOLD}||")
			formatted_texts = "\n".join(formatted_texts)
			
			return f"{separator}\n{header}\n{separator.replace('=', '-')}\n{formatted_texts}\n{separator}"
		else:
			formatted_list = []
			for text in texts:
				formatted_list.append(f"{cls.style.DARK_GREEN}{cls.style.BOLD}> {cls.style.RESET}{cls.style.LIGHT_GREEN}{text}{cls.style.RESET}\n")
			return "".join(formatted_list)


	@classmethod
	def raw(cls, message, from_print = False):
		if message.isspace(): return
		formatted_text = cls.format_print(str(message).split("\n"))
		cls.terminal(f"{formatted_text}{cls.style.RESET}")


	@classmethod
	def info(cls, message):
		formatted_text = cls.format_print(str(message).split("\n"), "INFO", cls.style.BLUE, cls.style.AQUA)
		cls.terminal(f"{formatted_text}{cls.style.RESET}")

	
	@classmethod
	def warn(cls, message):
		formatted_text = cls.format_print(str(message).split("\n"), "WARN", cls.style.GOLD, cls.style.YELLOW)
		cls.terminal(f"{formatted_text}{cls.style.RESET}")
	

	@classmethod
	def error(cls, message):
		formatted_text = cls.format_print(str(message).split("\n"), "ERROR", cls.style.DARK_RED, cls.style.LIGHT_RED)
		cls.terminal(f"{formatted_text}{cls.style.RESET}")


	@classmethod
	def traceback_handler(cls, type, value, tb):
		if cls.debug == False:
			trace = [f"Error type: {type.__name__}\nError message: {str(value)}\nFile: {tb.tb_frame.f_code.co_filename}"]
		else:
			trace = traceback.format_exception(type, value, tb)
		cls.error("".join(trace))


class OverwritePrint:
	def __init__(self, console):
		self.console = console

	def write(self, msg):
		self.console.raw(msg)

	def flush(self):
		pass


console_out = OverwritePrint(konsole)
sys.stdout = console_out
sys.stderr.write = konsole().error
sys.excepthook = konsole().traceback_handler