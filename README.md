# REST API documentation for SuperFaktúra

This is a language agnostic REST documentation for [SuperFaktúra](https://www.superfaktura.sk)
(and [Czech version](https://www.superfaktura.cz)).
It is different from documentation for our [PHP API client](https://github.com/superfaktura/apiclient).

Examples are using `curl` (tip: if you are testing via `curl`, you can use `json_pp` or `json_xs` to pretty print responses).


## Content


### [Intro](intro.md)

General information - authentication, URLs, how to form request and `X-`headers.


### [FAQ](faq.md)

FAQ with tips & tricks.


### [Value lists](value-lists.md)

Value lists (also called "číselníky" in Slovak and Czech), to tell you possible values and their meanings.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


### [BankAccount](bank-account.md)

Manage bank accounts.


### [Cash register item](cash-register-item.md)

Manage cash register items.


### [Clients](clients.md)

Manage clients.


### [Contact persons](contact-persons.md)

Manage contact persons for clients.


### [Expenses](expenses.md)

Manage expenses and paying expenses (expense payments).


### [Invoice](invoice.md)

Manage invoices and paying invoices (invoice payments).


### [Stock](stock.md)

Manage stock items and stock movements.


### [Tags](tags.md)

Manage tags. These can be added to invoices, expenses and clients.


### [Other](other.md)

Other entities that don't fall into the main categories.
