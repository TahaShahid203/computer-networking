from dnslib import DNSRecord, RR, QTYPE, A
from socketserver import UDPServer, BaseRequestHandler

# Custom DNS Records (Modify as needed)
DNS_MAPPING = {
    "test.local.": "192.168.1.100",
    "myserver.local.": "192.168.1.50",
}

class DNSHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        request = DNSRecord.parse(data)
        reply = request.reply()
        
        qname = str(request.q.qname)
        qtype = request.q.qtype
        
        if qtype == QTYPE.A and qname in DNS_MAPPING:
            ip_address = DNS_MAPPING[qname]
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(ip_address)))
        
        socket.sendto(reply.pack(), self.client_address)

# Run the DNS Server on port 53 (Requires admin rights)
server = UDPServer(("0.0.0.0", 53), DNSHandler)
print("Local DNS Server is running on port 53...")
server.serve_forever()
