from concurrent import futures
import requests

import grpc

import analysis_pb2
import analysis_pb2_grpc

url2api = 'http://presidio-api:8080/api/v1/'
apiproject = '1'
anonymizetemplateid = 'trashbaanonymizer'
analyzetemplateid = 'trashbaanalyzer'


class AnalysisServiceServicer(analysis_pb2_grpc.AnalysisServiceServicer):
  def Analyze(self, req, cntxt):
      txt =  requests.post (url2api + 'projects/' + apiproject + '/anonymize', json='{"text":"' + req.text +'", "AnalyzeTemplateId":"' + analyzetemplateid + '", "AnonymizeTemplateId":"' + anonymizetemplateid +'"}').text
      resp = analysis_pb2.AnalysisReply(text = txt)
      return resp

if __name__ == '__main__':
  
  requests.post (url2api + 'templates/' + apiproject + '/analyze/' + analyzetemplateid, json='{"allFields":true}')
  requests.post (url2api + 'templates/' + apiproject + '/anonymize/' + anonymizetemplateid, json='{"fieldTypeTransformations":[{"fields":[{"name":"PHONE_NUMBER"}],"transformation":{"replaceValue":{"newValue":"phone-number"}}},{"fields":[{"name":"CREDIT_CARD"}],"transformation":{"newValue":"credit-card"}}]}')


  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  analysis_pb2_grpc.add_AnalysisServiceServicer_to_server(AnalysisServiceServicer(), server)
  server.add_insecure_port('[::]:80')
  server.start()
  server.wait_for_termination()







