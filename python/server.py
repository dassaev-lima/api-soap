from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class IMCService(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def calcular_imc(ctx, peso, altura):
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        imc = peso / (altura * altura)
        return imc

application = Application(
    [IMCService],
    'spyne.examples.imc',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_application)  # '0.0.0.0' permite acesso de outras máquinas na mesma rede
    print("SOAP server is running on http://0.0.0.0:8000")
    server.serve_forever()
