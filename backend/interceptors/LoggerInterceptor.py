import logging
from colorama import init, Fore
from datetime import datetime

init()

logging.basicConfig(level=logging.INFO, format="%(message)s")


class LoggerInterceptor:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def __call__(self, cls):
        class_name = cls.__name__

        class WrappedClass:
            def __init__(self, *args, **kwargs):
                self.instance = cls(*args, **kwargs)
                self.logger = logging.getLogger(__name__)

            async def execute(self, *args, **kwargs):
                try:
                    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    self.logger.info(
                        f"{Fore.LIGHTBLUE_EX}[{current_time}] [{class_name}] {Fore.GREEN}Iniciando execução de {class_name} com parametros {args}{Fore.RESET}"
                    )
                    result = await self.instance.execute(*args, **kwargs)
                    self.logger.info(
                        f"{Fore.LIGHTBLUE_EX}[{current_time}] [{class_name}] {Fore.GREEN}{class_name} finalizado com sucesso resultado: {result}{Fore.RESET}"
                    )
                    return result
                except Exception as e:
                    self.logger.error(
                        f"{Fore.LIGHTBLUE_EX}[{current_time}] [{class_name}] {Fore.RED}{class_name} finalizado com erro: {str(e)}{Fore.RESET}"
                    )
                    raise e

        return WrappedClass
