
import shutil

try:
    shutil.rmtree('sneakers.egg-info')
    shutil.rmtree('build')
    shutil.rmtree('dist')

except Exception:
    print('Cleaning failed.')
