#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A library for stubbing in Python 2
Summary(pl.UTF-8):	Biblioteka do tworzenia zaślepek w Pythonie 2
Name:		python-pretend
Version:	1.0.8
Release:	3
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/pretend/
Source0:	https://pypi.python.org/packages/source/p/pretend/pretend-%{version}.tar.gz
# Source0-md5:	7147050a95c9f494248557b42b58ad79
URL:		https://github.com/alex/pretend
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pretend is a library to make stubbing with Python easier.

%description -l pl.UTF-8
Pretend to biblioteka ułatwiająca tworzenie zaślepek w Pythonie.

%package -n python3-pretend
Summary:	A library for stubbing in Python 3
Summary(pl.UTF-8):	Biblioteka do tworzenia zaślepek w Pythonie 3
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pretend
Pretend is a library to make stubbing with Python easier.

%description -n python3-pretend -l pl.UTF-8
Pretend to biblioteka ułatwiająca tworzenie zaślepek w Pythonie.

%prep
%setup -q -n pretend-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py_sitescriptdir}/pretend.py[co]
%{py_sitescriptdir}/pretend-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pretend
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py3_sitescriptdir}/pretend.py
%{py3_sitescriptdir}/__pycache__/pretend.cpython-*.py[co]
%{py3_sitescriptdir}/pretend-%{version}-py*.egg-info
%endif
