#!/bin/bash
until [[ $(curl --silent --head http://presidio-api:8080) ]]; do
    printf '.'
    sleep 5
done

curl -H "Content-Type: application/json"  -X POST -d '{"allFields":true}' http://presidio-api:8080/api/v1/templates/1/analyze/trashbaanalyzer
curl -H "Content-Type: application/json"  -X POST -d '{"fieldTypeTransformations":[{"fields":[{"name":"PHONE_NUMBER"}],"transformation":{"replaceValue":{"newValue":"phone-number"}}},{"fields":[{"name":"CREDIT_CARD"}],"transformation":{"replaceValue":{"newValue":"credit-card"}}}]}' http://presidio-api:8080/api/v1/templates/1/anonymize/trashbaanonymizer
curl -H "Content-Type: application/json"  -X POST -d '{"text":"We met yesterday morning in Seattle and his phone number is (212) 555 1234", "AnalyzeTemplateId":"trashbaanalyzer"  }'  http://presidio-api:8080/api/v1/templates/1/analyze
curl  -H "Content-Type: application/json" -v -X POST -d '{"text":"We met yesterday morning in Seattle and his phone number is (212) 555 1234", "AnalyzeTemplateId":"trashbaanalyzer", "AnonymizeTemplateId": "trashbaanonymizer"  }'  http://presidio-api:8080/api/v1/projects/1/anonymize

python app/grpc_server.py >> /var/log/grpc_server.log



