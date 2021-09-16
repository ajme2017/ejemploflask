# ejemploflask
Es necesario que configuren este archivo para que les permita realizar la conexión a postgres desde cualquier cliente.<br /> 
sudo nano /etc/postgresql/12/main/pg_hba.conf  (AQUI CAMBIAR PEER POR md5)


-Para que puedan crear un nuevo server en postgres es recomendable que lo hagan con el usuario "postgres" y para ello deben cambiarle su constraseña- <br /> 

para cambiar password del usuario postgres <br /> 
1.sudo su  <br /> 
2.su postgres <br /> 
3.psql <br /> 
4.\password  <br /> 
5.(ingresar nueva pass) <br /> 
