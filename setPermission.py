import os
import stat

st = os.stat('swag.py')
os.chmod('swag.py', st.st_mode | stat.S_IEXEC)