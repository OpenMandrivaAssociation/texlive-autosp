Name:		texlive-autosp
Version:	58211
Release:	1
Summary:	A Preprocessor that generates note-spacing commands for MusiXTeX scores
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autosp
License:	gpl2+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autosp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autosp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This program simplifies the creation of MusiXTeX scores by
converting (non-standard) commands of the form \anotes ... \en
into one or more conventional note-spacing commands, as
determined by the note values themselves, with \sk spacing
commands inserted as necessary. The coding for an entire
measure can be entered one part at a time, without concern for
note-spacing changes within the part or spacing requirements of
other parts. For example, \anotes\qa J\qa K&\ca l\qa m\ca n\en
generates \Notes\qa J\sk\qa K\sk&\ca l\qa m\sk\ca n\en .

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/doc/generic/autosp
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tex2aspc.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tex2aspc.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/autosp.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/autosp.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
