#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-rpmfile
Version  : 1.1.1
Release  : 19
URL      : https://files.pythonhosted.org/packages/df/a1/4ef3aba6c4c23e38b0ec766f0cd01c9db4abbe6febaa557b47541dc18000/rpmfile-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/a1/4ef3aba6c4c23e38b0ec766f0cd01c9db4abbe6febaa557b47541dc18000/rpmfile-1.1.1.tar.gz
Summary  : Read rpm archive files
Group    : Development/Tools
License  : MIT
Requires: pypi-rpmfile-bin = %{version}-%{release}
Requires: pypi-rpmfile-license = %{version}-%{release}
Requires: pypi-rpmfile-python = %{version}-%{release}
Requires: pypi-rpmfile-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# rpmfile
[![Build Status](https://travis-ci.org/srossross/rpmfile.svg?branch=master)](https://travis-ci.org/srossross/rpmfile)
[![Actions Status](https://github.com/srossross/rpmfile/workflows/Tests/badge.svg?branch=master&event=push)](https://github.com/srossross/rpmfile/actions)
[![PyPI version](https://img.shields.io/pypi/v/rpmfile.svg)](https://pypi.org/project/rpmfile)

%package bin
Summary: bin components for the pypi-rpmfile package.
Group: Binaries
Requires: pypi-rpmfile-license = %{version}-%{release}

%description bin
bin components for the pypi-rpmfile package.


%package license
Summary: license components for the pypi-rpmfile package.
Group: Default

%description license
license components for the pypi-rpmfile package.


%package python
Summary: python components for the pypi-rpmfile package.
Group: Default
Requires: pypi-rpmfile-python3 = %{version}-%{release}

%description python
python components for the pypi-rpmfile package.


%package python3
Summary: python3 components for the pypi-rpmfile package.
Group: Default
Requires: python3-core
Provides: pypi(rpmfile)

%description python3
python3 components for the pypi-rpmfile package.


%prep
%setup -q -n rpmfile-1.1.1
cd %{_builddir}/rpmfile-1.1.1
pushd ..
cp -a rpmfile-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679413031
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rpmfile
cp %{_builddir}/rpmfile-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rpmfile/4c2e02efc4825ff20aadf7ef62704c1c14c98ebb || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__pycache__/__init__.cpython-3*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rpmfile

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-rpmfile/4c2e02efc4825ff20aadf7ef62704c1c14c98ebb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
