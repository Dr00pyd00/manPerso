
# Personal MAN 

> This is API backend for a `man` system with postgres and http requests.     

When I code in C it's confortable to have `man` Linux commande for see documentation really fast.  
In this project I want to create a similar system for add some personnal documentation with app with 
TCP, HTTP protocol, server and in other hand: a CLI client ! 

## Stack 

- Python Fastapi 
- uvicorn 
- Postrgresql 
- uv ( for python env )

## Installation 

```bash 
mkdir ~/manPerso
cd ~/manPerso 

git clone https://github.com/Dr00pyd00/manPerso.git

```  
TODO: finir installion 


## Routes 

It is a CRUD for ManPage / Tags.

> Bonus: when you create ManPage you can autogenerate tags inside ! 

### ManPage 

- `GET http://127.0.0.1:8000/ ` : return a list of all manpages in DB 
- `GET http://127.0.0.1:8000/id/{id}` : return manpage by ID or 404 
- `GET http://127.0.0.1:8000/{manpage_name}` : return manpage by name or 404 

- `POST http://127.0.0.1:8000/` : create a manpage 

- `PATCH http://127.0.0.1:8000/{manpage_id}` : update a manpage by ID 

- `DELETE http://127.0.0.1:8000/{manpage_id}` : delete a manpage by ID 


