%global tl_name autosp
%global tl_revision 77851

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Preprocessor that generates note-spacing commands for MusiXTeX scores
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/autosp
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autosp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autosp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(autosp.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This program simplifies the creation of MusiXTeX scores by converting
(non-standard) commands of the form \anotes ... \en into one or more
conventional note-spacing commands, as determined by the note values
themselves, with \sk spacing commands inserted as necessary. The coding
for an entire measure can be entered one part at a time, without concern
for note-spacing changes within the part or spacing requirements of
other parts. For example, \anotes\qa J\qa K&\ca l\qa m\ca n\en generates
\Notes\qa J\sk\qa K\sk&\ca l\qa m\sk\ca n\en .

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/barsant2.aspc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/barsant2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/geminiani.aspc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/geminiani.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/kinder2.aspc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/kinder2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/quod2.aspc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/quod2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/quod2A.aspc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/quod2A.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/rebar.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/generic/autosp/rebar.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/autosp.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/autosp.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/tex2aspc.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/tex2aspc.man1.pdf
