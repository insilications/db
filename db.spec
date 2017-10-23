Name:           db
Version:        5.3.28
Release:        12
License:        Sleepycat
Summary:        Berkeley Database v5
Url:            http://www.oracle.com/technology/products/berkeley-db/db/index.html
Group:          libs
Source0:        http://download.oracle.com/berkeley-db/db-5.3.28.tar.gz
BuildRequires:  libstdc++-dev
Conflicts:      db3

%description
Berkeley Database v5.

%package cxx
Summary:        Berkeley Database v5
Group:          libs

%description cxx
Berkeley Database v5.

%package dev
Summary:        Berkeley Database v5
Group:          devel
Requires:       %{name} = %{version}-%{release}

%description dev
Berkeley Database v5.

%package doc
Summary:        Berkeley Database v5
Group:          doc

%description doc
Berkeley Database v5.

%package bin
Summary:        Berkeley Database v5
Group:          libs

%description bin
Berkeley Database v5.

%prep
%setup -q

%build
cd build_unix
../dist/configure --prefix=/usr \
 --libdir=/usr/lib64 \
 --enable-o_direct \
 --disable-cryptography \
 --disable-queue \
 --disable-replication \
 --disable-verify \
 --enable-compat185 \
 --disable-sql \
 --enable-shared \
 --disable-static \
 --enable-cxx

make %{?_smp_mflags}

%install
cd build_unix
%make_install

# Fix up headers
mkdir -p %{buildroot}%{_includedir}/db51
mv %{buildroot}%{_includedir}/db.h %{buildroot}%{_includedir}/db51/.
mv %{buildroot}%{_includedir}/db_cxx.h %{buildroot}%{_includedir}/db51/.
ln -sf db51/db.h %{buildroot}%{_includedir}/db.h
ln -sf db51/db_cxx.h %{buildroot}%{_includedir}/db_cxx.h

# The docs end up in /usr/docs - not right.
if test -d "%{buildroot}%{_prefix}/docs"
then
    mkdir -p "%{buildroot}%{_prefix}/share"
    test ! -d "%{buildroot}%{_datadir}/doc" || rm -rf "%{buildroot}%{_datadir}/doc"
    mv "%{buildroot}%{_prefix}/docs" "%{buildroot}%{_datadir}/doc"
fi

%files
%{_libdir}/libdb-*.so

%files cxx
%{_libdir}/libdb_cxx-*.so
%{_libdir}/libdb_cxx.so

%files dev
%{_includedir}/db.h
%{_includedir}/db_cxx.h
%{_includedir}/db_185.h
%{_includedir}/db51/db.h
%{_includedir}/db51/db_cxx.h
%{_libdir}/libdb.so

%files doc
%{_datadir}/doc/

%files bin
%{_bindir}/db_deadlock
%{_bindir}/db_tuner
%{_bindir}/db_printlog
%{_bindir}/db_checkpoint
%{_bindir}/db_stat
%{_bindir}/db_upgrade
%{_bindir}/db_verify
%{_bindir}/db_dump
%{_bindir}/db_log_verify
%{_bindir}/db_recover
%{_bindir}/db_archive
%{_bindir}/db_load
%{_bindir}/db_replicate
%{_bindir}/db_hotbackup

