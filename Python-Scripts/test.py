#from dotenv import load_dotenv
from bitcoin.rpc import RawProxy

from pprint import pprint
#RPC remote procedure call

p = RawProxy()

info = p.getblockchaininfo()

pprint(info)


#path = '/home/ghost/rpibots/'
#load_dotenv(path+'.env')

#rpc_user = os.getenv('rpc_user')
#rpc_pass = os.getenv('rpc_pass')
#rpc_host = os.getenv('rpc_host')



