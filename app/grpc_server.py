from concurrent import futures
import time
import math
import logging

import grpc

import analysis_pb2
import analysis_pb2_grpc


class AnalysisServiceServicer(analysis_pb2_grpc.AnalysisServiceServicer):
  """Provides methods that implement functionality of route guide server."""
  def Analyze(self, req, cntxt):
      resp = analysis_pb2.AnalysisReply(text = req.text + '_SERVER')
      return resp
if __name__ == '__main__':
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  analysis_pb2_grpc.add_AnalysisServiceServicer_to_server(AnalysisServiceServicer(), server)
  server.add_insecure_port('[::]:80')
  server.start()
  server.wait_for_termination()







