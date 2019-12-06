#!/usr/local/bin/python

import sys

import grpc

import analysis_pb2
import analysis_pb2_grpc

ORIGINAL_MESSAGE = \
    'my phone number is 057-555-2323 and my credit card is 4961-2765-5327-5913'
EXPECTED_MESSAGE = \
    'my phone number is phone-number and my credit card is credit-card'

if __name__ == '__main__':
    msg = analysis_pb2.AnalysisRequest(text = ORIGINAL_MESSAGE)
    with grpc.insecure_channel('grpc-server:80') as channel:
        try:
            stub = analysis_pb2_grpc.AnalysisServiceStub(channel)
            feature = stub.Analyze(msg)
        except Exception as err:
            print ('UNEXPECTED ERROR ', err)
            sys.exit(43)

        if feature.text == EXPECTED_MESSAGE:
            print ('PASSED')
            sys.exit(0)
        else:
            print ('FAILED: ', feature.text, ' vs ', EXPECTED_MESSAGE)
            sys.exit(42)
            
