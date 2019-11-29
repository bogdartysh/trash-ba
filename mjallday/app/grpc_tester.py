#!/usr/local/bin/python

import sys

import grpc

import analysis_pb2
import analysis_pb2_grpc

origMsg ='my phone number is 057-555-2323 and my credit card is 4961-2765-5327-5913'
expectedMsg = 'my phone number is phone-number and my credit card is credit-card'

if __name__ == '__main__':
  msg = analysis_pb2.AnalysisRequest(text = origMsg)
  with grpc.insecure_channel('grpc-server:80') as channel:
    try:
      stub = analysis_pb2_grpc.AnalysisServiceStub(channel)
      feature = stub.Analyze(msg)
    except Exception as e:
      print ('UNEXPECTED ERROR ', e)
      sys.exit(43)

    if feature.text == expectedMsg:
      print('PASSED')
      sys.exit(0)
    else:
      print('FAILED: ' , feature.text, " vs ", expectedMsg)
      sys.exit(42)


