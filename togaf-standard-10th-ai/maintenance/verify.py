#!/usr/bin/env python3
"""Run existing provenance checks using corpus-local maintenance contracts."""
import runpy
import sys
from publish import CORPUS, ROOT, guard

sys.dont_write_bytecode = True
sys.addaudithook(guard)
sys.argv = ['validate_architecture.py', '--corpus', str(CORPUS)]
try:
    runpy.run_path(str(CORPUS / 'maintenance/pipeline/validate_architecture.py'), run_name='__main__')
except SystemExit as exc:
    if exc.code not in (None,0):raise
import verify_extended
raise SystemExit(verify_extended.main())
