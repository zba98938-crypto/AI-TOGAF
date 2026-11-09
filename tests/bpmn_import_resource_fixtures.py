"""Independent fixtures from BPMN 2.0.2 §§8.2.2, 15.3.1 and 15.3.2.

Source oracle: participant.processRef -> Process, callActivity.calledElement
-> CallableElement, messageEventDefinition.messageRef -> Message, and
partnerEntity.participantRef -> Participant. QName is namespace + native ID;
sequenceFlow sourceRef/targetRef are same-document IDREFs (Semantic.xsd).
These expected roles are fixture constants, not imported from the adapter.
"""
import base64
import hashlib

BPMN = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
XSD = 'http://www.w3.org/2001/XMLSchema'
WSDL = 'http://www.w3.org/TR/wsdl20/'
SOURCE_SHA256 = {
    'BPMN20.cmof': '72f5bf035da7bea80dc53131a22e6ba466789abd7437532e64abd3a7cff20139',
    'Semantic.xsd': 'c4318842f7d2bbc262d7954c9452c501db16f0868eac0b8732ec5d7fb384d9a7',
    'BPMN-2.0.2.pdf': 'd3d9258a70bf808c11ac52becea4ce645540a8b881117535f60a56fbf13e22f2',
}


def document(body='', namespace='urn:root'):
    return ('\ufeff<?xml version="1.0" encoding="UTF-8"?>\r\n'
            '<definitions xmlns="'+BPMN+'" xmlns:r="urn:shared" xmlns:s="urn:other" '
            'targetNamespace="'+namespace+'">\r\n'+body+'\r\n</definitions>\r\n').encode('utf-8')


def imported(location='shared/model.bpmn', namespace='urn:shared', kind=BPMN):
    return '<import namespace="'+namespace+'" location="'+location+'" importType="'+kind+'"/>'


def record(path, data):
    return {'path': path, 'payload_encoding': 'base64',
            'content': base64.b64encode(data).decode('ascii'),
            'sha256': hashlib.sha256(data).hexdigest()}


ROOT = document(imported()+'<collaboration id="C"><participant id="A" processRef="r:P"/></collaboration>')
CHILD = document('<process id="P" name="订单处理"/>', 'urn:shared')
