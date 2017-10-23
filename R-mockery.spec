#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mockery
Version  : 0.3.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/mockery_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mockery_0.3.0.tar.gz
Summary  : Mocking Library for R
Group    : Development/Tools
License  : MIT
Requires: R-markdown
BuildRequires : R-markdown
BuildRequires : clr-R-helpers

%description
The two main functionalities of this package are creating mock
    objects (functions) and selectively intercepting calls to a given
    function that originate in some other function. It can be used
    with any testing framework available for R. Mock objects can
    be injected with either this package's own stub() function or a
    similar with_mock() facility present in the testthat package.

%prep
%setup -q -c -n mockery

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505672558

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1505672558
export LANG=C
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
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockery
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mockery
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
