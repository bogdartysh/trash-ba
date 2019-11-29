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

= HOWTO = 
commands needed:
```
docker-compose build
docker-compose up -d
docker-compose up test
```
