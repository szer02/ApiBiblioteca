import asyncio
from fastapi import FastAPI
from starlette import HTMLResponse
import uvicorn

#from user import Usuario

app = FastAPI()

@app.get('/apiname', response_class = HTMLResponse)
async def apiname() -> str:
    return 'ApiBiblioteca'

async def  main():
    config = uvicorn.Config('main:app', port = 5032, log_level = 'info', reload = True)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())


'''info  = Usuario(
    'Santiago', 
    'santiago',
    '12345678',
    'aluno',
    'santiago@gmail.com',
    '992865400'
)


info.cadastrar_usuario('Cadastrar')
info.consultar_usuario('Listar')
#alterar_usuario('Alterar')'''

