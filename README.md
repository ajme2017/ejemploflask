# ejemploflask
Es necesario que configuren este archivo para que les permita realizar la conexión a postgres desde cualquier cliente.
sudo nano /etc/postgresql/12/main/pg_hba.conf  (AQUI CAMBIAR PEER POR md5)


-Para que puedan crear un nuevo server en postgres es recomendable que lo hagan con el usuario "postgres" y para ello deben cambiarle su constraseña-

para cambiar password del usuario postgres
1.sudo su
2.su postgres
3.psql
4.\password 
5.(ingresar nueva pass)
