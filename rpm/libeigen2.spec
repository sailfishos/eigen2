#define _with_check -DEIGEN_BUILD_TESTS=ON -DEIGEN_TEST_NO_FORTRAN=ON -DEIGEN_TEST_NOQT=ON

Name:           libeigen2-headers
License:        GPL v2 or later; LGPL v3 or later
Group:          Development/Libraries
Summary:        Lightweight linear algebra C++ template library
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url:            http://eigen.tuxfamily.org/
Version:        2.0.17
Release:        10.1
Source:         eigen-%{version}.tar.bz2
BuildRequires:  fdupes, cmake
#BuildRequires:  doxygen, graphviz
#BuildRequires:  tex(latex)
BuildArch: noarch

%description
Eigen is a lightweight C++ template library for vector and matrix math,
a.k.a. linear algebra.

%files
%defattr(-,root,root)
%{_includedir}/eigen2/*
%{_datadir}/pkgconfig/*

%package doc
Summary: Documentation for %{name}
Group: Documentation

%description doc
%{summary}.

%files doc
%defattr(-,root,root)
%doc COPYING COPYING.LESSER
# %{_docdir}/eigen2


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr %{?_with_check}
make %{?_smp_mflags}
#make doc

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_docdir}/eigen2
#cp -R doc/html %{buildroot}/%{_docdir}/eigen2
%fdupes %{buildroot}/%{_includedir}
#%fdupes %{buildroot}/%{_docdir}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig
test "$(pkg-config --modversion eigen2)" = "%{version}"
%if 0%{?_with_check:1}
( cd test; ctest )
%endif
