%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: devede
Version: 3.11
Release: 1%{?dist}
Summary: DeVeDe is a program to create video DVDs and CDs (VCD, sVCD or CVD)

Group: Applications/Multimedia
License: GPLv3+
URL: http://www.rastersoft.com/programas/devede.html
Source0: http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: python >= 2.4
BuildRequires: gettext
BuildRequires: desktop-file-utils
Requires: mplayer
Requires: mencoder
Requires: dvdauthor
Requires: vcdimager
Requires: mkisofs
Requires: ImageMagick
Requires: python >= 2.4
Requires: pygtk2
Requires: pygtk2-libglade

%description
DeVeDe is a program to create video DVDs and CDs (VCD, sVCD or CVD), 
suitables for home players, from any number of video files, in any 
of the formats supported by Mplayer. The big advantage over other 
utilities is that it only needs Mplayer, Mencoder, DVDAuthor, VCDImager 
and MKisofs (well, and Python 2.4, PyGTK and PyGlade), so its 
dependencies are really small.


%prep
%setup -q

# Fix devede module directory
sed -i 's!/usr/lib/!%{python_sitelib}/!' devede.py


%build


%install
rm -rf $RPM_BUILD_ROOT

./install.sh \
  --uninstall=no \
  --targeted=yes \
  --DESTDIR=$RPM_BUILD_ROOT \
  --prefix=%{_prefix} \
  --libdir=%{python_sitelib} \
  --pkgdocdir=%{_docdir}/%{name}-%{version}

# remove debian files from doc
rm $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{copyright,changelog.Debian}

# rename .desktop file 
desktop-file-install \
  --delete-original \
  --vendor livna \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/devede
%{python_sitelib}/devede
%{_datadir}/devede
%{_datadir}/applications/livna-%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%doc %{_docdir}/%{name}-%{version}


%changelog
* Mon Aug 24 2008 Andrea Musuruane <musuruan@gmail.com> 3.11-1
- Updated to version 3.11.

* Tue Aug 19 2008 Andrea Musuruane <musuruan@gmail.com> 3.10-1
- Updated to version 3.10.

* Sat Jun 28 2008 Andrea Musuruane <musuruan@gmail.com> 3.9-1
- Updated to version 3.9.

* Mon May 26 2008 Andrea Musuruane <musuruan@gmail.com> 3.8c-1
- Updated to version 3.8c.

* Sat Apr 19 2008 Andrea Musuruane <musuruan@gmail.com> 3.7-1
- Updated to version 3.7.

* Wed Dec 12 2007 Andrea Musuruane <musuruan@gmail.com> 3.6-1
- Updated to version 3.6.

* Sun Dec 9 2007 Andrea Musuruane <musuruan@gmail.com> 3.5-1
- Updated to version 3.5.

* Sat Nov 24 2007 Andrea Musuruane <musuruan@gmail.com> 3.4-1
- Updated to version 3.4.

* Fri Oct 26 2007 Andrea Musuruane <musuruan@gmail.com> 3.3-1
- Updated to version 3.3.

* Tue Sep 19 2007 Andrea Musuruane <musuruan@gmail.com> 3.2-1
- Updated to version 3.2.
- License changed to GPLv3 or later.
- Updated icon cache scriptlets to be compliant to new guidelines.

* Sat Aug 25 2007 Andrea Musuruane <musuruan@gmail.com> 3.01-3
- Changed license due to new guidelines.

* Sun Jul 08 2007 Andrea Musuruane <musuruan@gmail.com> 3.01-2
- Removed %%{?dist} tag from changelog.

* Sat Jul 07 2007 Andrea Musuruane <musuruan@gmail.com> 3.01-1
- Updated to version 3.01.
- Cosmetical changes.

* Sun Jun 24 2007 Andrea Musuruane <musuruan@gmail.com> 3.0-1
- Updated to version 3.0.
- Updated icon cache scriptlets to be compliant to new guidelines.
- Minor fixes to desktop file.

* Fri Apr 20 2007 Andrea Musuruane <musuruan@gmail.com> 2.13-1
- Updated to version 2.13.

* Thu Mar 01 2007 Andrea Musuruane <musuruan@gmail.com> 2.12-1
- First release for Livna.

