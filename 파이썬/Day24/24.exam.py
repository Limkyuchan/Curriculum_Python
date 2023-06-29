
"""
< Network >

Network?
- 물리적 연결
- 대화를 주고 받는 것. 환경

서버(Server): 제공하는 주체(서비스 요청에 대한 응답)
클라이언트(Client): 이용하는 주체(서비스를 요청)

P2P (Peer-to-Peer) 
- 동등한 위치
- 어떨 때는 서버의 역할, 어떨 때는 클라이언트의 역할


LAN (Local Area Network)
- 한정된 지역 내에서 여러 컴퓨터와 기기들이 서로 연결되어 정보와 자원을 공유할 수 있는 네트워크 시스템.
- 일반적으로 가까운 거리에 위치한 건물 내, 학교, 기업, 가정 등에서 사용.
- 주요 특징
1) 제한된 범위: LAN은 한정된 지역 내에서만 작동하며, 일반적으로 몇 킬로미터 이내의 거리를 포함.
               거리가 늘어날 수록 신호 감쇠와 지연 시간이 증가하므로, 보통 짧은 거리에서만 사용.
2) 고속 데이터 전송: LAN은 국소 영역 내에서 높은 데이터 전송 속도를 제공. 
                    이더넷(Ethernet) 기술은 대표적인 LAN 기술로, 최대 10Gbps 까지의 속도를 지원.
3) 자원 공유: LAN은 연결된 컴퓨터와 기기들이 파일, 프린터, 인터넷 연결 등의 자원을 공유.
             이로 인해 효율적인 자원 관리와 비용 절감을 실현할 수 있음.
4) 안전성: LAN은 국소 영역 내에서만 작동하기 떄문에, 외부 네트워크와 비교하여 상대적으로 보안성이 높다.
          그러나 LAN 내에서도 적절한 보안 조치를 취해야 한다.
ex) 이더넷(Ethernet) 


WAN (Wide Area Network)
- 넓은 지역을 포함하는 컴퓨터와 기기들이 연결된 네트워크.
- 서로 떨어져 있는 LAN 들을 연결하는 역할을 하며, 광범위한 지리적 영역을 가로지르는
  네트워크 통신을 가능하게 함. 전 세계적인 범위에서 작동할 수 있음.
- 주요 특징
1) 광범위한 지리적 영역
2) 데이터 전송 속도: LAN에 비해 낮은 데이터 전송 속도를 제공.
3) 비용: WAN을 구축하고 유지하는 데에는 높은 비용이 들 수 있음.
4) 종속성: WAN은 전화 회사, 인터넷 서비스 제공자(ISP)등 제 3자의 인프라와 서비스에 의존할 수 있음.
          이로 인해 고장, 지연 시간 및 서비스 수준 계약(SLA)과 같은 요소에 영향을 받을 수 있음.
ex) 인터넷(Internet)


Protocol (통신규약)
- 컴퓨터나 네트워크 장비가 서로 통신하기 위해서 미리 정해놓은 약속.(표준화된 규칙이나 절차)
- 효율성과 안정성을 보장하기 위해 사용되며, 다양한 종류의 시스템이 원활하게 상호작용할 수 있게 해줌.
ex)
IP(Internet Protocol)
HTTP(Hyper Text Transfer Protocol)
HTTPs(Hyper Text Transfer Protocol Secure)
FTP(File Transfer Protocol)
DHCP(Dynam Host Conf Protocol)
DNS(Domain Name System)
SMTP(Simple Main Transfer Protocol)
TELNET
POP
ICMP
SNMP
...



< TCP/IP >
- Transmission Control Protocol / Internet Protocol
- 인터넷에서 가장 널리 사용되는 프로토콜 스택(프로토콜들의 집합).
- TCP/IP는 인터넷의 기반이 되는 통신 규칙으로, 서로 다른 네트워크에서 컴퓨터와 기기들이 효과적으로 정보를 주고 받을 수 있도록 해줌.
- 프로토콜 스택은 여러 계층으로 구성되어 있으며, 각 계층에서 서로 다른 프로토콜들이 작동.
- IP : 데이터 패킷을 송수신 할 때 사용되는 주소 체계를 정의. IP는 각 컴퓨터와 기기에 고유한 IP주소를 할당.
       비신뢰성 프로토콜로 간주되며, 데이터 패킷 전달의 신뢰성을 보장하지 않음.
- TCP : IP와 함께 작동하여 데이터 전송의 신뢰성을 보장. 
       연결 지향적 프로토콜로, 데이터를 전송하기 전에 송신자와 수신자 간에 연결이 설정.

< TCP/IP Model >
- Application
- Transport
- Internet
- Network Interface
  (Hardware)




cmd 인터넷 연결 확인방법
- ipconfig
- ping /? - ping(게이트웨이)














"""