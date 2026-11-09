"""Refresh only the six business examples from the packaged raw materials."""
import hashlib
import json
from pathlib import Path
import sys

C=Path(__file__).resolve().parents[1]
S=C/'skills/_shared'
sys.path.insert(0,str(S/'scripts'))
from planning_case_examples import install,PROFILE_IDS,MATERIAL


def main():
    path=S/'capabilities.json'
    caps=json.loads(path.read_text())
    install(caps)
    path.write_text(json.dumps(caps,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'profiles':list(PROFILE_IDS),'raw_material_sha256':hashlib.sha256(MATERIAL.read_bytes()).hexdigest(),
                      'business_acceptance':False},ensure_ascii=False))


if __name__=='__main__':main()
