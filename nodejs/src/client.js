const soap = require("soap");

const url = "http://localhost:8000/?wsdl"; // URL do WSDL do servidor SOAP

const args = {
  peso: 70,
  altura: 1.75,
};

soap.createClient(url, (err, client) => {
  if (err) {
    console.error("Erro ao criar cliente SOAP:", err);
    return;
  }

  client.calcular_imc(args, (err, result) => {
    if (err) {
      console.error("Erro ao chamar método SOAP:", err);
      return;
    }

    console.log("Resultado do IMC:", result);
  });
});
