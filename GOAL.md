
# Faire un man perso pour linux et outils generaux 

## idee 

Creer une DB + server qui va pouvoir servir des pages de manuels pour des outils linux ou C ou autre ( un peu copier man de C )
Plus tard creer un petit client en CLI pour justement reproduire man.

## Fonctionnement: 

- Postgres en DB docker 
- sqlalchemy
- Fastapi


## Objets:
 
    PageManual:
        - id    
        - text ( la page elle meme ) 
        - tags fk  list[ie: reseau, dev , cyber ets ] 
       
    Tag:
        - id 
        - value 
        - pages fk 
