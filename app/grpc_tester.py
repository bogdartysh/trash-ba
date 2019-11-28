import sys

import grpc

import analysis_pb2
import analysis_pb2_grpc


if __name__ == '__main__':
  msg = analysis_pb2.AnalysisRequest(text='my phone number is 057-555-2323 and my credit card is 4961-2765-5327-5913')
  with grpc.insecure_channel('grpc-server:80') as channel:
      stub = analysis_pb2_grpc.AnalysisServiceStub(channel)
      feature = stub.Analyze(msg)
      if feature.text == 'my phone number is phone-number and my credit card is credit-cart':
          print('PASSED', feature)
          sys.exit(0)
      else:
          print('FAILED, ' , feature)
          sys.exit(42)







