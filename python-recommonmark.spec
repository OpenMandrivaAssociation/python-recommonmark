%define oname   recommonmark

Name:           python-%{oname}
Version:	0.7.1
Release:	3
Summary:        Docutils compatibility bridge to CommonMark
# https://pypi.org/project/recommonmark/
Source0:	https://files.pythonhosted.org/packages/1c/00/3dd2bdc4184b0ce754b5b446325abf45c2e0a347e022292ddc44670f628c/%{oname}-%{version}.tar.gz
License:        Python
Group:          Development/Python
Url:            https://recommonmark.readthedocs.io/en/latest/
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
A docutils-compatibility bridge to CommonMark.

This allows you to write CommonMark inside of Docutils & Sphinx projects.

%files
%dir %{py_puresitedir}/%{oname}
%{_bindir}/cm2*
%{py_puresitedir}/%{oname}-%{version}-*.egg-info
%{py_puresitedir}/%{oname}/*
