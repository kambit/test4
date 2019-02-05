from boa.interop.Neo.Blockchain import GetHeader
from boa.interop.Neo.Header import GetHash, GetConsensusData, GetNextConsensus 


def Main(height):
    header = GetHeader(height)
    consensus = header.ConsensusData
    return consensus
