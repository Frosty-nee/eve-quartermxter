### ESI Client setup
```
curl -X POST "https://generator.swagger.io/api/gen/clients/python" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"swaggerUrl\":\"https://esi.evetech.net/_latest/swagger.json?datasource=tranquility\"}"
```
then `wget` the link in the returned json and `unzip` to the `python_client` directory.

The docs that CCP provides at `https://developers.eveonline.com/blog/article/swagger-codegen` for setup are somewhat out of date,
and I have found that in order for things to work as expected, you need to `ln -s -d python_client/swagger_client swagger_client`
after following the above instructions.
