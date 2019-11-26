Name:           python-genshi
Version:        0.7
Release:        23
Summary:        Python toolkit for generation of output for the web
License:        BSD
URL:            http://genshi.edgewall.org/
Source0:        http://ftp.edgewall.com/pub/genshi/Genshi-%{version}.tar.gz
Patch0000:      python-genshi-0.7-sanitizer-test-fixes.patch
Patch0001:      python-genshi-0.7-disable-speedups-for-python34.patch
Patch0002:      python-genshi-0.7-isstring-helper.patch
Patch0003:      python-genshi-0.7-python34-ast-support.patch
Patch0004:      python-genshi-bug-602-python35-support.patch
Patch0005:      python-genshi-bug-602-python35-support-python27-fix.patch
Patch0006:      python-genshi-py37-stopiteration.patch
Patch0007:      python-genshi-py3-escape-sequence-doctest.patch

BuildRequires:  gcc python2-devel python2-setuptools python3-devel python3-setuptools
Requires:       python2-babel >= 0.8

%description
Genshi is a Python library that provides an integrated set of components
for parsing, generating, and processing HTML, XML
or other textual content for output generation on the web.

%package -n python2-genshi
Summary:        Python toolkit for generation of output for the web
%{?python_provide:%python_provide python2-genshi}

%description -n python2-genshi
Genshi is a Python library that provides an integrated set of components
for parsing, generating, and processing HTML, XML
or other textual content for output generation on the web.

%package -n python3-genshi
Summary:        Python toolkit for generation of output for the web
%{?python_provide:%python_provide python3-genshi}
BuildArch:      noarch
Requires:       python3-babel >= 0.8

%description -n python3-genshi
Genshi is a Python library that provides an integrated set of components
for parsing, generating, and processing HTML, XML
or other textual content for output generation on the web.

%prep
%autosetup -n Genshi-%{version} -p1

rm -rf %{modname}.egg-info
rm -rf %{py3dir}
cp -a . %{py3dir}

chmod a-x examples/*

%build
%{__python2} setup.py build

cd %{py3dir}
%{__python3} setup.py build
cd -

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
cd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
cd -

%check
%{__python2} setup.py test
cd %{py3dir}
%{__python3} setup.py test
cd -

%files -n python2-genshi
%doc ChangeLog doc examples README.txt COPYING
%{python2_sitearch}/Genshi-%{version}-py*.egg-info
%{python2_sitearch}/genshi

%files -n python3-genshi
%doc ChangeLog doc examples README.txt COPYING
%{python3_sitelib}/Genshi-%{version}-py*.egg-info
%{python3_sitelib}/genshi

%changelog
* Mon Nov 18 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.7-23
- Package init
