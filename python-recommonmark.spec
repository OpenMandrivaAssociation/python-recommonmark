%define oname   recommonmark

Name:           python-%{oname}
Version:	0.6.0
Release:	2
Summary:        Docutils compatibility bridge to CommonMark
# https://pypi.org/project/recommonmark/
Source0:	https://files.pythonhosted.org/packages/source/r/recommonmark/recommonmark-%{version}.tar.gz
License:        Python
Group:          Development/Python
Url:            https://recommonmark.readthedocs.io/en/latest/
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools
BuildArch:	noarch

%description
A docutils-compatibility bridge to CommonMark.

This allows you to write CommonMark inside of Docutils & Sphinx projects.

%package -n python2-recommonmark
Summary: %{summary}
BuildRequires: python2-devel

%description -n python2-recommonmark
A docutils-compatibility bridge to CommonMark.

This allows you to write CommonMark inside of Docutils & Sphinx projects.

%prep
%setup -qc 
mv %{oname}-%{version} python2
cp -a python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python} setup.py install --root=%{buildroot}
popd

%files
%{_bindir}/cm2*
%{py_puresitedir}/recommonmark-%{version}-*.egg-info
%{py_puresitedir}/recommonmark*

%files -n python2-recommonmark
%{py2_puresitedir}/recommonmark-%{version}-*.egg-info
%{py2_puresitedir}/recommonmark*
