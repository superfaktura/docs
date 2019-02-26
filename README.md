# REST API for SuperFaktúra

This is a language agnostic REST documentation for [SuperFaktúra](https://www.superfaktura.sk).
It is different from documentation for our [PHP API client](https://github.com/superfaktura/apiclient).

Examples are using `curl` (tip: if you are testing via `curl`, you can use `json_pp` or `json_xs` to pretty print responses).


## Content


### Intro

General information - authentication, URLs, how to form request and `X-`headers.


### FAQ

FAQ with tips & tricks.


### Value lists

Value lists (or so called "číselníky" in Slovak and Czech), to tell you possible values and their meanings.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


### [BankAccount](bank-account.md)

Manage bank accounts.


### Cash register item

Manage cash register items.


### Clients

Manage clients.


### Contact people

Manage contact people for clients.


### Expenses

Manage expenses and paying expenses (expense payments).


### Invoice

Manage invoices and paying invoices (invoice payments).


### Stock

Manage stock items and stock movements.


### Tags

Manage tags. These can be added to invoices, expenses and clients.


### Other

Other entities that don't fall into the main categories.
