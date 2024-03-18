# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from hfc.protos.peer import proposal_pb2 as hfc_dot_protos_dot_peer_dot_proposal__pb2
from hfc.protos.peer import proposal_response_pb2 as hfc_dot_protos_dot_peer_dot_proposal__response__pb2


class EndorserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessProposal = channel.unary_unary(
                '/protos.Endorser/ProcessProposal',
                request_serializer=hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.SerializeToString,
                response_deserializer=hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.FromString,
                )


class EndorserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessProposal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EndorserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessProposal,
                    request_deserializer=hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.FromString,
                    response_serializer=hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.Endorser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Endorser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessProposal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Endorser/ProcessProposal',
            hfc_dot_protos_dot_peer_dot_proposal__pb2.SignedProposal.SerializeToString,
            hfc_dot_protos_dot_peer_dot_proposal__response__pb2.ProposalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
