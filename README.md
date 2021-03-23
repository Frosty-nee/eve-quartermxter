### ESI Client setup
```
curl -X POST "https://generator.swagger.io/api/gen/clients/python" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"swaggerUrl\":\"https://esi.evetech.net/_latest/swagger.json?datasource=tranquility\"}"
```
then wget the link in the returned json and `unzip` to the `python_client` directory.


