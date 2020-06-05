%global _hardened_build 1
%global _vpath_builddir build

Name:           libanimation
Version:        3.8.6
Release:        1%{?dist}
Summary:        Library that provides animation calculations
License:        LGPL

%undefine _disable_source_fetch
URL:            https://github.com/hermes83/libanimation
Source0:        https://github.com/hermes83/%{name}/archive/master.tar.gz

BuildRequires:  meson
BuildRequires:  gobject-introspection
BuildRequires:  gmock
BuildRequires:  gtest
Requires:       glib2

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary} .

%prep
%setup -q -T -b 0 -n %{name}-master
if [ ! -d .git ]; then
    git clone --bare --depth 1 https://github.com/hermes83/%{name}.git .git
    git config --local --bool core.bare false
    git reset --hard
fi

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_libdir}/*.so*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/animation/*.h
%{_includedir}/animation/wobbly/*.h
%{_includedir}/animation-glib/*.h
%{_includedir}/animation-glib/wobbly/*.h
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
