import mercadopago
import dotenv
import os

class mercadopagoAPI:
    dotenv.load_dotenv()
    ACCES_TOKEN= os.environ.get("YOUR_ACCESS_TOKEN")
    CARDS_TOKEN= os.environ.get("CARD_TOKEN")

    sdk = mercadopago.SDK(ACCES_TOKEN)

    #payment_data = {
    #    "transaction_amount": 100,
    #    "token": CARDS_TOKEN,
    #    "description": "Payment description",
    #    "payment_method_id": 'visa',
    #    "installments": 1,
    #    "payer": {
    #        "email": 'test_user_123456@testuser.com'
    #    }
    #}
    #result = sdk.payment().create(payment_data)
    #payment = result["response"]

    #print()
    #print(payment)




    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': 'f856a8s46as895324'
    }

    payment_data = {
        "transaction_amount": 100,
        "token": 'ff8080814c11e237014c1ff593b57b4d',
        "installments": 1,
        "payer": {
            "type": "customer",
            "id": "123456789-jxOV430go9fx2e"
        }
    }

    payment_response = sdk.payment().create(payment_data, request_options)
    payment = payment_response["response"]

    print()
    print(payment)


