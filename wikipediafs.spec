Summary:	View and edit Wikipedia articles as if they were real files
Name:		wikipediafs
Version:	0.4
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Base
Source:		http://downloads.sourceforge.net/wikipediafs/%name-%version.tar.bz2
URL:		http://wikipediafs.sourceforge.net/
Buildroot:	%_tmppath/%name-%version-root
%py_requires -d
BuildArch:	noarch
BuildRequires:	python => 2.4
BuildRequires:	fuse => 2.6.3
BuildRequires:	python-fuse => 0.2
Requires:	python-fuse => 0.2

%description
WikipediaFS is a mountable Linux virtual file system that allows to read and
edit articles from Wikipedia (or any Mediawiki-based site) as if they were real
files.

It is thus possible to view and edit articles using your favourite text-editor.
Text-editors tend to be more convenient than a simple browser form when it
comes to editing large texts and they generally include useful features such as
Mediawiki syntax highlighting and spell checking.

Open your article, perform your modifications and save ! That's it, Wikipedia
has been updated for you!

Advance usage of WikipediaFS includes easy development of scripts and bots.
Programs simply have to deal with normal files because this is WikipediaFS
which takes care of the HTTP layer. For example, it would be possible to use
WikipediaFS to perform a massive content migration from an existing site to a
Mediawiki.

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,man,755)
%doc NEWS doc/*.htm
%attr(755,root,root) %_bindir/mount.wikipediafs
%python_sitelib/wikipediafs*
%_mandir/man1/mount.wikipediafs.*



%changelog
* Tue Mar 08 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.4-1mdv2011.0
+ Revision: 642893
- new version

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.3-5mdv2011.0
+ Revision: 590585
- rebuild for python 2.7

* Mon Feb 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3-4mdv2010.1
+ Revision: 509737
- fix mixed space and tabs

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.3-3mdv2010.0
+ Revision: 445781
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.3-2mdv2009.1
+ Revision: 326119
- rebuild

* Thu Aug 21 2008 Funda Wang <fwang@mandriva.org> 0.3-1mdv2009.0
+ Revision: 274676
- fix BR

  + Thierry Vignaud <tv@mandriva.org>
    - import wikipediafs


* Thu Aug 21 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2009.0
- initial release
