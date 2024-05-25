from interceptors.LoggerInterceptor import LoggerInterceptor


@LoggerInterceptor()
class BuscarCategoriasQuery:

    async def execute():
        try:
            print("oi")
        except Exception as e:
            raise e
