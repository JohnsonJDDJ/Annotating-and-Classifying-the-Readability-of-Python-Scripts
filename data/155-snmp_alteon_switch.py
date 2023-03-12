from pysnmp.hlapi import *

# Alteon Application Switch 3408
# /cfg/sys/ssnmp/cur
# /cfg/sys/ssnmp/snmpv3/cur

# # SNMP 프로토콜 정보
host = 'switch.ip.address'
read_community = 'public'
# write_community = 'private'

# https://www.ibm.com/docs/ko/taddm/7.3.0?topic=sensors-snmp-mib2-sensor
# https://support.radware.com/app/answers/answer_view/a_id/16176/~/alteon-recommended-oids-for-snmp-monitoring
# 현재 장비 버전 /info/sys/general
# Software Version 22.0.7.1
# https://support.radware.com/ci/okcsFattach/get/16176_5
# Alteon version 29.5 MIB
# oid = '.1.3.6.1.4.1.1872.2.5.4.2.5.1.0'  # The maximum number entries in the session table
oid = '.1.3.6.1.4.1.1872.2.5.4.2.5.2.0'  # The Current Number of session in the session table
# oid = '.1.3.6.1.4.1.1872.2.5.4.2.5.3.0'  # The Current Number of session in the session table in the last 4 seconds
identity = ObjectIdentity(oid)

# https://www.circitor.fr/Mibs/Html/S/SNMPv2-MIB.php#sysUpTime
# identity = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)  # Nortel Application Switch 3408
# identity = ObjectIdentity('SNMPv2-MIB', 'sysObjectID', 0)  # SNMPv2-SMI::enterprises.1872.1.13.2.1

# # SNMPv3 보안 인증 정보
# user = 'v1v2only'  # 사용자 이름
# auth_key = None  # 인증 암호
# priv_key = None  # 암호화 암호
#
# # SNMPv3 설정
# snmpv3_user = UsmUserData(userName=user)

gen_snmp = getCmd(
    SnmpEngine(),
    CommunityData(communityIndex=read_community, mpModel=0),  # SNMPv1, SNMPv2c
    # authData=snmpv3_user,  # SNMPv3
    UdpTransportTarget((host, 161), timeout=5, retries=1),
    ContextData(),
    ObjectType(identity),
)

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in gen_snmp:
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))