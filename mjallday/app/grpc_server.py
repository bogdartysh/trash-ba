#!/usr/local/bin/python

from concurrent import futures
from io import BytesIO

import pycurl
import json


import grpc

import analysis_pb2
import analysis_pb2_grpc

url2api = 'http://presidio-api:8080/api/v1/'
apiproject = '1'
anonymizetemplateid = 'trashbaanonymizer'
analyzetemplateid = 'trashbaanalyzer'


def getResp(msg):
      data = BytesIO()
      c = pycurl.Curl()
      c.setopt(c.URL, url2api + 'projects/' + apiproject + '/anonymize')
      c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept: */*'])
      c.setopt(c.WRITEFUNCTION, data.write)
      c.setopt(c.POSTFIELDS, '{"text":"' + msg +'", "AnalyzeTemplateId":"' + analyzetemplateid + '", "AnonymizeTemplateId":"' + anonymizetemplateid +'"}')
      c.perform()
      print("for: ", msg, " got: ", data.getvalue())
      return json.loads(data.getvalue())['text']

class AnalysisServiceServicer(analysis_pb2_grpc.AnalysisServiceServicer):
  def Analyze(self, req, cntxt):
      return analysis_pb2.AnalysisReply(text = getResp(req.text))

if __name__ == '__main__':
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=9))
  analysis_pb2_grpc.add_AnalysisServiceServicer_to_server(AnalysisServiceServicer(), server)
  server.add_insecure_port('[::]:80')
  server.start()
  server.wait_for_termination()







