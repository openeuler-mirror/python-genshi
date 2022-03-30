%global _python_bytecompile_extra 1

Name:           python-genshi
Version:        0.7.6
Release:        1
Summary:        Toolkit for stream-based generation of output for the web
License:        BSD
URL:            http://genshi.edgewall.org/
Source0:        https://files.pythonhosted.org/packages/source/G/Genshi/Genshi-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description
Genshi is a Python library that provides an integrated set of 
components for parsing, generating, and processing HTML, XML
or other textual content for output generation on the web.

%package -n python3-genshi
Summary:        Toolkit for stream-based generation of output for the web
BuildArch:      noarch
Requires:       python3-babel >= 0.8

%description -n python3-genshi
Genshi is a Python library that provides an integrated set of 
components for parsing, generating, and processing HTML, XML
or other textual content for output generation on the web.

%prep
%autosetup -n Genshi-%{version} -p1

rm -rf %{modname}.egg-info
rm -rf %{py3dir}
cp -a . %{py3dir}

find examples -type f | xargs chmod a-x

%build
export GENSHI_BUILD_SPEEDUP=0
cd %{py3dir}
%py3_build
cd -

%install
export GENSHI_BUILD_SPEEDUP=0
cd %{py3dir}
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/genshi/tests
rm -rf %{buildroot}%{python3_sitelib}/genshi/{filters,template}/tests
rm -f %{buildroot}%{python3_sitelib}/genshi/*.c
cd -

%check
cd %{py3dir}
%{__python3} setup.py test
cd -

%files -n python3-genshi
%license COPYING
%doc ChangeLog doc examples README.txt
%{python3_sitelib}/Genshi-%{version}-py*.egg-info
%{python3_sitelib}/genshi

%changelog
* Wed Mar 30 2022 xigaoxinyan <xigaoxinyan@huawei.com> - 0.7.6-1
- update to 0.7.6

* Tue Dec 22 2020 lingsheng <lingsheng@huaweu.com> - 0.7.3-7
- Fix wrong source0 url

* Mon Jun 28 2020 Captain Wei <captain.a.wei@gmail.com> - 0.7.3-6
- Upgrade package

* Mon Nov 18 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.7-23
- Package init
