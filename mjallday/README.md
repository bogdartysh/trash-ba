# mjallday-ba


- Write a test to end to end we can invoke the test by calling `docker-compose up test` to test your integration
  - The test should use the string “my phone number is 057-555-2323 and my credit card is 4961-2765-5327-5913” as the fixture data and assert that the system identifies and redacts the sensitive data within this string
- Write a GRPC service that implements this interface

```
service AnalysisService {
    rpc Analyze(AnalysisRequest) returns (AnalysisReply) {}
}
	
message AnalysisRequest {
    string text = 1;
}
	
message AnalysisReply {
    string text = 2;
}
```
- Add Microsoft Presidio to your `docker-compose.yaml`
- Connect your GRPC service to call Presidio and return the response

## HOWTO 

 
commands needed to start:

```
docker-compose build
docker-compose up -d
docker-compose up test
```

for new protos file:

```
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/analysis.proto
```

# for Production-ready
1. move to Java:-)
2. healthcheck to be added, current entry point is ok fo POC
3. the server hardly checks any errors, to be improved
4. folder structure/code style/docs is OK only for POC
5. improve logging and monitroing (add Prometheus or other)
6. number of threads on server is to be adjustable (in Java JMX)
7. all settings are to be passed as env. variables from docker-compose, not hardcoded in scripts


