1. Mettre le Home Assistant en SSL et créer deux fichiers de certificats (crt.crt et key.key)
2. Rajouter ces fichiers dans le dossier Escape Rush Connector

2bis. Rajouter les fichier textapi et hello_state dans le dossier custom component de Home Assistant

3. Dans Hassio créer 2 jetons de longue durée, un pour Escape Rush Connector, et un pour Escape Room Master

4. Copier la valeur du jeron dans le fichier token.txt

5. Mettre l'adresse IP de home assistant dans le fichier ipconfig.txt

6. Uploader le dossier Escape Rush Connector via FTP dans le répértoire addons de Home Assistant

7. Dans l'onglet Supervisor / Add On / Faire un refresh

8. Cliquer sur Installer / Start

-----------------

Dans Escape Room Master

Network poll : http://homeassistantip:8000/textapi/states/sensor.escape_rush_operational_status

Envoi MQTT


var data = {
  "payload": "100", 
   "topic": "tracker",
  "qos": 0,
  "retain": 0};
$.ajax({
    url: 'https://192.168.69.100:8123/api/services/mqtt/publish',
    headers: {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlMGI0N2FkZjRkOTI0YTUwYjMzY2U4ZTI5MTI3NzhiZSIsImlhdCI6MTU4NzQ3NDc4NCwiZXhwIjoxOTAyODM0Nzg0fQ.9_025VkvtknZkScUr-FC4dAsz2q7pCqQt87rMkar8Dw"
    },
    dataType: 'json',
    data: JSON.stringify(data),
        contentType: 'application/json',
        type: 'POST',
        success: function(res) {
console.log("success!!!");
          return console.log(res);
        },
        error: function(res) {
console.log("error!!!");
          return console.log(res);
        }
});
