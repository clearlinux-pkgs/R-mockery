#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mockery
Version  : 0.4.2
Release  : 31
URL      : https://cran.r-project.org/src/contrib/mockery_0.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mockery_0.4.2.tar.gz
Summary  : Mocking Library for R
Group    : Development/Tools
License  : MIT
Requires: R-testthat
BuildRequires : R-testthat
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# mockery
[![Travis-CI Build Status](https://travis-ci.org/r-lib/mockery.svg?branch=master)](https://travis-ci.org/r-lib/mockery)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/mockery/master.svg)](https://codecov.io/github/r-lib/mockery?branch=master)
[![CRAN version](http://www.r-pkg.org/badges/version/mockery)](https://CRAN.r-project.org/package=mockery)
[![Downloads](http://cranlogs.r-pkg.org/badges/mockery)](https://CRAN.r-project.org/package=mockery)

%prep
%setup -q -c -n mockery

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571868122

%install
export SOURCE_DATE_EPOCH=1571868122
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockery
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockery
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockery
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mockery || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mockery/DESCRIPTION
/usr/lib64/R/library/mockery/INDEX
/usr/lib64/R/library/mockery/LICENSE
/usr/lib64/R/library/mockery/Meta/Rd.rds
/usr/lib64/R/library/mockery/Meta/features.rds
/usr/lib64/R/library/mockery/Meta/hsearch.rds
/usr/lib64/R/library/mockery/Meta/links.rds
/usr/lib64/R/library/mockery/Meta/nsInfo.rds
/usr/lib64/R/library/mockery/Meta/package.rds
/usr/lib64/R/library/mockery/Meta/vignette.rds
/usr/lib64/R/library/mockery/NAMESPACE
/usr/lib64/R/library/mockery/NEWS.md
/usr/lib64/R/library/mockery/R/mockery
/usr/lib64/R/library/mockery/R/mockery.rdb
/usr/lib64/R/library/mockery/R/mockery.rdx
/usr/lib64/R/library/mockery/doc/index.html
/usr/lib64/R/library/mockery/doc/mocks-and-testthat.R
/usr/lib64/R/library/mockery/doc/mocks-and-testthat.Rmd
/usr/lib64/R/library/mockery/doc/mocks-and-testthat.html
/usr/lib64/R/library/mockery/help/AnIndex
/usr/lib64/R/library/mockery/help/aliases.rds
/usr/lib64/R/library/mockery/help/mockery.rdb
/usr/lib64/R/library/mockery/help/mockery.rdx
/usr/lib64/R/library/mockery/help/paths.rds
/usr/lib64/R/library/mockery/html/00Index.html
/usr/lib64/R/library/mockery/html/R.css
/usr/lib64/R/library/mockery/tests/testthat.R
/usr/lib64/R/library/mockery/tests/testthat/test-mock-object.R
/usr/lib64/R/library/mockery/tests/testthat/test_stub.R
