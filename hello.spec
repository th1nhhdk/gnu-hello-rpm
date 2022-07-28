Name:           hello
Version:        2.12.1
Release:        1%{?dist}
Summary:        Prints a friendly greeting

License:        GPLv3+
URL:            https://www.gnu.org/software/%{name}/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  texinfo
Requires: glibc

%description
GNU Hello prints a friendly greeting.  It also serves as a sample GNU
package, showing practices that may be useful for GNU projects.

%prep
%autosetup
mv THANKS THANKS.old
iconv --from-code=ISO-8859-1 --to-code=UTF-8 --output=THANKS THANKS.old

%build
%configure
%make_build

%install
%make_install
rm %{buildroot}/%{_infodir}/dir
%find_lang %{name}

%check
make check

%files -f %{name}.lang
%{_bindir}/hello
%{_mandir}/man1/hello.1.*
%{_infodir}/hello.info.*

%license COPYING
%doc AUTHORS ChangeLog TODO NEWS README THANKS

%changelog
* Thu Jul 28 2022 th1nhhdk <th1nhhdk@tutanota.com> - 2.12.1-1
- Updated to 2.12.1

* Mon Mar 14 2022 th1nhhdk <th1nhhdk@tutanota.com> - 2.12-1
- Phiên bản đầu tiên của gói phần mềm 
