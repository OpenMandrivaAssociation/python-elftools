Summary:	Python library for parsing and anaylizing ELF files and DWARF debugging information
Name:		python-elftools
Version:	0.27
Release:	1
Group:		Development/Python
License:	BSD
Url:		https://pypi.org/project/pyelftools/
Source0:	https://files.pythonhosted.org/packages/source/p/pyelftools/pyelftools-%{version}.tar.gz
Patch0:		dwarf5-constants.patch
Patch1:		dwarf5.patch
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(sphinx)
BuildArch:	noarch

%description
Python library for parsing and anaylizing ELF files and DWARF debugging information

%files
%{_bindir}/readelf.py
%{py_puresitedir}/elftools
%{py_puresitedir}/pyelftools*.egg-info

#------------------------------------------------------------
%prep
%autosetup -p1 -n pyelftools-%{version}

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1

%check
%{__python} setup.py \
	check
