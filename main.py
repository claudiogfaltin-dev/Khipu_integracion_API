import requests
import json

url = "https://payment-api.khipu.com/v3/payments"

payload = json.dumps({
  "amount": 5000,
  "currency": "CLP",
  "subject": "Cobro de prueba"
})

headers = {
  'x-api-key': 'b57b93e8-****-****-****-************',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("Respuesta de Khipu:")
print(response.text)
