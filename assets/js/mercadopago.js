import { loadMercadoPago } from "https://sdk.mercadopago.com/js/v2";


await loadMercadoPago();
const mp = new window.MercadoPago("TEST-0cc52ad8-1d45-4308-97b9-64b31e7e08fe");
