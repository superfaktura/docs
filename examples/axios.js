const axios = require('axios');

const API_URL = 'https://moja.superfaktura.sk';
const AUTH_EMAIL = '';
const AUTH_API_KEY = '';
const AUTH_COMPANY_ID = '';
const AUTH_MODULE = 'YOUR_MODULE_NAME';


// Authorization header
// Please notice Content-Type
// And all parameters in Authorization
const config = {
    headers: {
        'Authorization': `SFAPI email=${AUTH_EMAIL}&apikey=${AUTH_API_KEY}&company_id=${AUTH_COMPANY_ID}&module=${AUTH_MODULE}`,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
};


// In this example we will first create our client
// This is necessary only the first time
const clientBody = {
    "Client":{
        "name":"Superfaktura s.r.o.",
        "ico": "46655034",
    }
};


// Invoice body
// Notice we are sending ICO of existing client
const invoiceBody = {
    "Invoice":{
        "name": "Test API",
    },
    "InvoiceItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10,
        }
    ],
    "Client":{
        "ico": "46655034",
    }
};




// First let's create our client
// Please notice how data is sent.
// Don't send pure JSON.
axios.post(`${API_URL}/clients/create`, 'data=' + JSON.stringify(clientBody), config)
    .then(result => {
        console.debug(result)


        // Once your client is created, it's enough to send this request to create invoice
        //
        // Please notice how data is sent.
        // Don't send pure JSON.
        axios.post(`${API_URL}/invoices/create`, 'data=' + JSON.stringify(invoiceBody, null, 2), config)
            .then(result => { console.debug(result); })
            .catch(err => { console.error(err); });
    })
    .catch(err => { console.error(err) });
