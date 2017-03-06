import sys
if not sys.version.startswith('3'):
    PY2=True
else:
    PY2=False

if PY2:
    def open(*args,**kw):
        if 'encoding' in kw:
            kw.pop('encoding')
    