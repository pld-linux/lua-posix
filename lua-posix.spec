%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}

Summary:	A POSIX library for Lua
Name:		lua-posix
Version:	5.1.9
Release:	1

License:	Public Domain
Group:		Development/Libraries
URL:		http://luaforge.net/projects/luaposix/
Source0:	http://luaforge.net/frs/download.php/4808/luaposix-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-devel >= %{luaver}
Requires:	lua >= %{luaver}

%description
This is a POSIX library for Lua which provides access to many POSIX
features to Lua programs.

%prep
%setup -q -n luaposix

%build
%{__make} %{?_smp_mflags} PREFIX=%{_prefix} LUALIB=%{lualibdir} LUABIN=%{_bindir} LUAINC=%{_includedir}/lua51

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LUALIB=%{lualibdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc README
%{lualibdir}/*
