# Copyright (c) 2015 Antumbra
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

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
