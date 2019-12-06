#!/usr/local/bin/python

from concurrent import futures
from io import BytesIO

import pycurl
import json

import grpc

import analysis_pb2
import analysis_pb2_grpc

MAX_WORKERS = 9
URL_API = 'http://presidio-api:8080/api/v1/'
API_PROJECT = '1'
ANONYMIZE_TEMPLATEID = 'trashbaanonymizer'
ANALYZE_TEMPLATEID = 'trashbaanalyzer'
HEADERS = ['Content-Type: application/json', 'Accept: */*']
URL_ANONYMIZER = URL_API + 'projects/' + API_PROJECT + '/anonymize'


def get_presido_anonymizer_response(msg):
    print ('handling ', msg)
    data = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, URL_ANONYMIZER)
    c.setopt(c.HTTPHEADER, HEADERS)
    c.setopt(c.WRITEFUNCTION, data.write)
    c.setopt(c.POSTFIELDS, '{"text":"' + msg
             + '", "AnalyzeTemplateId":"' + ANALYZE_TEMPLATEID
             + '", "AnonymizeTemplateId":"' + ANONYMIZE_TEMPLATEID + '"}'
             )
    c.perform()
    print ('for: ', msg, ' got: ', data.getvalue())
    return json.loads(data.getvalue())['text']


class AnalysisServiceServicer(analysis_pb2_grpc.AnalysisServiceServicer):
    def Analyze(self, req, cntxt):
        return analysis_pb2.AnalysisReply(text=get_presido_anonymizer_response(req.text))


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = MAX_WORKERS))
    analysis_pb2_grpc.add_AnalysisServiceServicer_to_server(AnalysisServiceServicer(),
            server)
    server.add_insecure_port('[::]:80')
    server.start()
    server.wait_for_termination()
