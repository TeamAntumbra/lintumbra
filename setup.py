from distutils.core import setup

setup(name='lintumbra',
      version='0.0.1',
      description="Antumbra Glow client for Linux",
      author="Team Antumbra",
      author_email='contact@antumbra.io',
      url='https://github.com/TeamAntumbra/lintumbra',
      packages=['antumbra'],
      package_dir={'antumbra': '.'},
      scripts=['antumbra'])
