# ldap.gv.at definitions as specified in:
# http://www.ref.gv.at/AG-IZ-PVP2-Version-2-1-0-2.2754.0.html
LDAPGVAT_OID = 'urn:oid:1.2.40.0.10.2.1.1.'

UCL_DIR_PILOT = 'urn:oid:0.9.2342.19200300.100.1.'
X500ATTR_OID = 'urn:oid:2.5.4.'
LDAPGVAT_UCL_DIR_PILOT = UCL_DIR_PILOT
LDAPGVAT_X500ATTR_OID = X500ATTR_OID
NETSCAPE_LDAP = 'urn:oid:2.16.840.1.113730.3.1.'
PKCS_9 = 'urn:oid:1.2.840.113549.1.9.1.'
SCHAC = 'urn:oid:1.3.6.1.4.1.25178.1.2.'
SIS = 'urn:oid:1.2.752.194.10.2.'
UMICH = 'urn:oid:1.3.6.1.4.1.250.1.57.'
XMLSOAP_IMI = 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/'

# openosi-0.82.schema http://www.openosi.org/osi/display/ldap/Home
OPENOSI_OID = 'urn:oid:1.3.6.1.4.1.27630.2.1.1.'


MAP = {
    'identifier': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
    'fro': {
        NETSCAPE_LDAP+'39': 'preferredLanguage',
        NETSCAPE_LDAP+'241': 'displayName',
        PKCS_9+'1': 'email',
        SCHAC+'2': 'gender',
        UCL_DIR_PILOT+'1': 'uid',
        UCL_DIR_PILOT+'3': 'mail',
        LDAPGVAT_OID+'261.100': 'orgSourcePin',
        X500ATTR_OID+'3': 'cn',
        X500ATTR_OID+'4': 'sn',
        X500ATTR_OID+'6': 'c',
        X500ATTR_OID+'7': 'l',
        X500ATTR_OID+'8': 'st',
        X500ATTR_OID+'9': 'street',
        X500ATTR_OID+'10': 'o',
        X500ATTR_OID+'11': 'ou',
        X500ATTR_OID+'12': 'title',
        X500ATTR_OID+'16': 'postalAddress',
        X500ATTR_OID+'17': 'postalCode',
        X500ATTR_OID+'18': 'postOfficeBox',
        X500ATTR_OID+'20': 'telephoneNumber',
        X500ATTR_OID+'42': 'givenName',
        'urn:oid:1.3.88': 'gln',
        XMLSOAP_IMI+'givenname': 'imi_givenName',
        XMLSOAP_IMI+'surname': 'imi_surname',
        XMLSOAP_IMI+'emailaddress': 'imi_emailaddress',
        XMLSOAP_IMI+'gender': 'imi_gender',
        XMLSOAP_IMI+'dateofbirth': 'imi_dateofbirth',
        XMLSOAP_IMI+'displayname': 'imi_displayname',
        XMLSOAP_IMI+'name': 'imi_uniquename',
        XMLSOAP_IMI+'upn': 'imi_upn',
        'http://schemas.xmlsoap.org/claims/CommonName': 'imi_commonName',
        'http://wirtschaftsportalverbund.at/ns/identity/claims/2016/04/authenticationClass': 'authenticationClass',
        'http://wirtschaftsportalverbund.at/ns/identity/claims/2016/04/registrationClassOrg': 'registrationClassOrg',
        'http://wirtschaftsportalverbund.at/ns/identity/claims/2016/04/registrationClassUser': 'registrationClassUser',
        'http://schemas.wko.at/ws/2011/12/identity/claims/adobjectguidbase64': 'wkis_gid',
        'http://schemas.wko.at/ws/2014/06/identity/claims/possiblerole': 'wkis_possiblerole',
        'http://schemas.wko.at/ws/2014/02/identity/claims/redirect': 'wkis_redirect',
        'http://schemas.wko.at/ws/2014/02/identity/claims/roledescription': 'wkis_roledescription',
        'http://schemas.wko.at/ws/2014/02/identity/claims/roleextendeddescription': 'wkis_roleextendeddescription',
        'http://schemas.wko.at/ws/2014/02/identity/claims/roletypeid': 'wkis_roletypeid',
        'http://schemas.wko.at/ws/2013/11/identity/claims/title': 'wkis_title',
    },
    'to': {
        'c': X500ATTR_OID+'6',
        'cn': X500ATTR_OID+'3',
        'displayName': NETSCAPE_LDAP+'241',
        'email': PKCS_9+'1',
        'gender': SCHAC+'2',
        'givenName': X500ATTR_OID+'42',
        'initials': X500ATTR_OID+'43',
        'l': X500ATTR_OID+'7',
        'mail': UCL_DIR_PILOT+'3',
        'o': X500ATTR_OID+'10',
        'ou': X500ATTR_OID+'11',
        'owner': X500ATTR_OID+'32',
        'physicalDeliveryOfficeName': X500ATTR_OID+'19',
        'postOfficeBox': X500ATTR_OID+'18',
        'postalAddress': X500ATTR_OID+'16',
        'postalCode': X500ATTR_OID+'17',
        'preferredLanguage': NETSCAPE_LDAP+'39',
        'sn': X500ATTR_OID+'4',
        'st': X500ATTR_OID+'8',
        'street': X500ATTR_OID+'9',
        'telephoneNumber': X500ATTR_OID+'20',
        'title': X500ATTR_OID+'12',
        'uid': UCL_DIR_PILOT+'1',
        'gln': 'urn:oid:1.3.88',
        'orgSourcePin': LDAPGVAT_OID+'261.100',
        'imi_givenName': XMLSOAP_IMI + 'givenname',
        'imi_surname': XMLSOAP_IMI + 'surname',
        'imi_emailaddress': XMLSOAP_IMI + 'emailaddress',
        'imi_gender': XMLSOAP_IMI + 'gender',
        'imi_dateofbirth': XMLSOAP_IMI + 'dateofbirth',
        'imi_displayname': XMLSOAP_IMI + 'name',
        'imi_uniquename': XMLSOAP_IMI + 'name',
        'imi_upn': XMLSOAP_IMI + 'upn',
        'authenticationClass': 'http://wirtschaftsportalverbund.at/ns/identity/claims/2016/04/authenticationClass',
        'registrationClassOrg': 'http://wirtschaftsportalverbund.at/ns/identity/claims/2016/04/registrationClassOrg',
        'registrationClassUser': 'http://wirtschaftsportalverbund.at/ns/identity/claims/2016/04/registrationClassUser',
        'wkis_gid': 'http://schemas.wko.at/ws/2011/12/identity/claims/adobjectguidbase64',
        'wkis_redirect': 'http://schemas.wko.at/ws/2014/02/identity/claims/redirect',
        'wkis_possiblerole': 'http://schemas.wko.at/ws/2014/06/identity/claims/possiblerole',
        'wkis_roledescription': 'http://schemas.wko.at/ws/2014/02/identity/claims/roledescription',
        'wkis_roleextendeddescription': 'http://schemas.wko.at/ws/2014/02/identity/claims/roleextendeddescription',
        'wkis_roletypeid': 'http://schemas.wko.at/ws/2014/02/identity/claims/roletypeid',
        'wkis_title': 'http://schemas.wko.at/ws/2013/11/identity/claims/title',
    }
}

