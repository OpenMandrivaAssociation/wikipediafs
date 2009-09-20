Summary: View and edit Wikipedia articles as if they were real files
Name:	wikipediafs
Version: 0.3
Release: %mkrel 3
License: GPLv2+
Group:	System/Base
Source: http://downloads.sourceforge.net/wikipediafs/%name-%version.tar.bz2
URL:	http://wikipediafs.sourceforge.net/
Buildroot: %_tmppath/%name-%version-root
%py_requires -d
BuildArchitectures: noarch
BuildRequires: python => 2.4
BuildRequires: fuse => 2.6.3
BuildRequires: python-fuse => 0.2
Requires: python-fuse => 0.2

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

