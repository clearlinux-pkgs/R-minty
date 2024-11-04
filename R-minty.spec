#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-minty
Version  : 0.0.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/minty_0.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/minty_0.0.1.tar.gz
Summary  : Minimal Type Guesser
Group    : Development/Tools
License  : MIT
Requires: R-minty-lib = %{version}-%{release}
Requires: R-cpp11
Requires: R-tzdb
BuildRequires : R-cpp11
BuildRequires : R-hms
BuildRequires : R-tzdb
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# minty <img src="man/figures/logo.png" align="right" height="138" alt = ""/>
<!-- badges: start -->

%package lib
Summary: lib components for the R-minty package.
Group: Libraries

%description lib
lib components for the R-minty package.


%prep
%setup -q -n minty

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716765862

%install
export SOURCE_DATE_EPOCH=1716765862
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/minty/DESCRIPTION
/usr/lib64/R/library/minty/INDEX
/usr/lib64/R/library/minty/LICENSE
/usr/lib64/R/library/minty/Meta/Rd.rds
/usr/lib64/R/library/minty/Meta/features.rds
/usr/lib64/R/library/minty/Meta/hsearch.rds
/usr/lib64/R/library/minty/Meta/links.rds
/usr/lib64/R/library/minty/Meta/nsInfo.rds
/usr/lib64/R/library/minty/Meta/package.rds
/usr/lib64/R/library/minty/NAMESPACE
/usr/lib64/R/library/minty/R/minty
/usr/lib64/R/library/minty/R/minty.rdb
/usr/lib64/R/library/minty/R/minty.rdx
/usr/lib64/R/library/minty/R/sysdata.rdb
/usr/lib64/R/library/minty/R/sysdata.rdx
/usr/lib64/R/library/minty/help/AnIndex
/usr/lib64/R/library/minty/help/aliases.rds
/usr/lib64/R/library/minty/help/figures/logo.png
/usr/lib64/R/library/minty/help/figures/logo.svg
/usr/lib64/R/library/minty/help/minty.rdb
/usr/lib64/R/library/minty/help/minty.rdx
/usr/lib64/R/library/minty/help/paths.rds
/usr/lib64/R/library/minty/html/00Index.html
/usr/lib64/R/library/minty/html/R.css
/usr/lib64/R/library/minty/tests/testthat.R
/usr/lib64/R/library/minty/tests/testthat/_snaps/edition-2/col-spec.md
/usr/lib64/R/library/minty/tests/testthat/test-col-spec.R
/usr/lib64/R/library/minty/tests/testthat/test-collectors.R
/usr/lib64/R/library/minty/tests/testthat/test-locale.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing-character.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing-datetime.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing-factors.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing-logical.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing-numeric.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing-time.R
/usr/lib64/R/library/minty/tests/testthat/test-parsing.R
/usr/lib64/R/library/minty/tests/testthat/test-type-convert.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/minty/libs/minty.so
