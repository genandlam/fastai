# library book loan 


## Local Testing

You can test your code by building your docker image and running it locally. Then, use Swagger to test your endpoints.

```
docker build -t library-test .
docker run --rm -p 8081:8081 library-test
```

Go to `localhost:8080/docs` for Swagger.
