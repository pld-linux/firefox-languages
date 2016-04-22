# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
../builder -g firefox-languages.spec
V=45.0
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoksa
Name:		firefox-languages
Version:	45.0.2
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	fafd01aed6384b8604dc788a2894abb8
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	7955b042c03803317a37b3a8eab2b3ec
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	f332f0c0caf66fb40c9e7009df29b5d4
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source3-md5:	fe84d0838cc8442cfa6279789f96538d
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source4-md5:	0c55489708e1204546742bab528b4b9e
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source5-md5:	3fcee07e4bb7b45ee9b210d3c7b1811b
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source6-md5:	8bb195520389c517a9185c0ccb307b43
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	5a39a2b069939e9e4a1134aac9e1d354
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	32163bdcfb922b9a5b18692e3ca44eb6
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	949f9658c88f873a15a376d26b89dccf
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	19d07c18eb09775cf2295535f894eeb5
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	28fe33a7235a894e85e86fae95e1db28
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	4dcbcd83a4006a674d898b0d8ebde398
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	684600b815b4f92b959dd6759d1c8370
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	ea85e86ff1cf035bdf1d64fb44af002f
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	fb285bbdda2aa3c8f0314a3711fc384f
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	86d525fec15fb5236f1c81542cf03810
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	b22bc7ff16abeae6b71c834a6e4872b4
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	22d1cb7f3003d76dce0848a4e119802e
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	4c61e7d8d87dde7acbeb2ae4c944571e
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	d464945e6eb4ded178bee02ada2c798d
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	671c107216e130ff6bd03c9b0df029f1
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	960e036978daccb86ed3256c76b07732
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	8e1573a0a704cc520c47e054589d38a8
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	56cbf6b3f2afacfdd4fed4eda5901e6a
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	7dac2a47a4d968d5aef96adf96c77fc6
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	5b22c7cb88c79fc5a6536b7b4f0a1497
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	165ad999f4003f523372670e6c571869
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	f93e6eea6cb9341bcb57cc49cafedc42
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	f4f3897b48489cfad52f3fe48de01705
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	88cf178b6b02112fa0486d8dbd42848f
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	46e8896c883edba5ae21a7d86cfa0f3a
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	d5c1a429d2e3b43dfaf748b2cdcdc93b
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	b22d3b6c5a16d76fd58c76c95f66425d
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	6c1a3e79c0762cdf1207b71db304adad
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	9397ac60943978c87c71656d04399e98
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	9987ec87d146cc5c6e67b30db6d6bcf0
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	654724219ff57ca8a94dfbc57109191b
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gn.xpi
# Source38-md5:	a458992d4e4415fba96aa8bcc127c37a
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source39-md5:	45ae793d1f1e2bd6aaa729b0b6e32ce0
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source40-md5:	46c8ecde1e79f60802d09403a4b0d48a
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source41-md5:	9178065cdea657d033878f0228782434
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source42-md5:	85bcc61690b265828f1bbca62489af42
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source43-md5:	8b8da2ae93d81d07d0b45002ca36b57b
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source44-md5:	bc2ff397d2203ca830db26528b0293f8
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source45-md5:	ee84053c99dca812ccd344c6e879f610
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source46-md5:	882bc168a14e82ab46acd7c3321cfa91
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source47-md5:	da1dfe29fe6da1bc46e958a058c705c0
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source48-md5:	e6c2cc9ec13afcad4d2f07af75284e68
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source49-md5:	f9c63f4811e8b0a2718925d8584ea508
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source50-md5:	bbb8417c0784e1be3332def44e101a26
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source51-md5:	8317a59e0bde805505f9bb2718acef5e
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source52-md5:	50ee91436092043913c3e12bfd7a1085
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source53-md5:	e5481125b3340532ce6085a5ef9cefbd
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source54-md5:	47a2ac2af915dc641aaae26e812b27de
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source55-md5:	427ce55994ef1e5e35727f30687dda0d
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source56-md5:	d03a99cd04c77f83a859ef44ba072440
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source57-md5:	bc10f7f923ef46451ded9f00600c9eb5
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source58-md5:	168fe94ef1d9798c09847a1515b8d520
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source59-md5:	6c70abcc3d104b5975dda28d8a1c1206
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source60-md5:	02d6d980c74cb9a4e4a60d519262332a
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source61-md5:	3e6f34fedc82436672b593ce5cdc0c7b
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source62-md5:	1a15aa90b0f53b7b7f334ba60bec8dfc
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source63-md5:	832b8164d45b3ad0a4ec361aaad8678a
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source64-md5:	b578a256021fffb4cf2ff54896845f68
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source65-md5:	6249cef718ad56cc2ada07f287e687d8
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source66-md5:	62bf73b4d57353f21ceb01ed0dc1bac1
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source67-md5:	be3571c4d32cff1b329c25feaebcf9fe
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source68-md5:	9ecaa76ee8f29a59447b3e405dfad2b7
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source69-md5:	5766d76c0ae282fcd17fc634de2daca2
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source70-md5:	75d1a09e5a1dceb09f0975ce5eca615d
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source71-md5:	667628ca798474bf23a4f26bc22e84b9
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source72-md5:	b1ab809984acd1705f298adfe24da678
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source73-md5:	44f8a919031cde82d460d7ac88bbc0c4
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source74-md5:	abddd73ea310955002e7ee8005faa054
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source75-md5:	e20e7e554b212c63d9445e4f03225828
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source76-md5:	d57bb4b493031dfd44d698ce0e4c09e8
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source77-md5:	14146f556b88d6c0695b3f3a45b7516f
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source78-md5:	81737545e26c1289af29699ab1070ed6
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source79-md5:	1926db57c28ff01db0b9526505b57622
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source80-md5:	5157c8d8ddb77554bf2437ad9838a3b5
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source81-md5:	52e1ca501344a2b7985cd9bfff6b1500
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source82-md5:	50f1379082a3daccf6910f8e4881703e
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source83-md5:	aecab5cb8d0c1c4ca503b767a65b26ad
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source84-md5:	221c58d60a3d58edab67f24867badf31
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source85-md5:	be948567645781e92b80844d833cffdb
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source86-md5:	14fe9253dbe389dc414d0c2a53b880c6
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source87-md5:	cf564ac8a36961834cbc09b51bd64d22
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source88-md5:	63b75baeff46eec5f73e64d519f3b238
Source89:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source89-md5:	8504582690a32e9467feab4c7eff2f8e
URL:		http://www.mozilla.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		firefoxdir	%{_datadir}/firefox

%description
Language packs for Firefox.

%description -l pl.UTF-8
Pakiety językowe dla Firefoksa.

%package -n firefox-lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ach
Obsoletes:	mozilla-firefox-lang-ach

%description -n firefox-lang-ach
Acoli resources for Firefox.

%description -n firefox-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoksa.

%package -n firefox-lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-af
Obsoletes:	mozilla-firefox-lang-af

%description -n firefox-lang-af
Afrikaans resources for Firefox.

%description -n firefox-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoksa.

%package -n firefox-lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-an
Obsoletes:	mozilla-firefox-lang-an

%description -n firefox-lang-an
Aragonese resources for Firefox.

%description -n firefox-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ar
Obsoletes:	mozilla-firefox-lang-ar

%description -n firefox-lang-ar
Arabic resources for Firefox.

%description -n firefox-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoksa.

%package -n firefox-lang-as
Summary:	Assamese resources for Firefox
Summary(pl.UTF-8):	Asamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-as
Obsoletes:	mozilla-firefox-lang-as

%description -n firefox-lang-as
Assamese resources for Firefox.

%description -n firefox-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ast
Obsoletes:	mozilla-firefox-lang-ast

%description -n firefox-lang-ast
Asturian resources for Firefox.

%description -n firefox-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-az
Obsoletes:	mozilla-firefox-lang-az

%description -n firefox-lang-az
Azerbaijani resources for Firefox.

%description -n firefox-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoksa.

%package -n firefox-lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-be
Obsoletes:	mozilla-firefox-lang-be

%description -n firefox-lang-be
Belarusian resources for Firefox.

%description -n firefox-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoksa.

%package -n firefox-lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bg
Obsoletes:	mozilla-firefox-lang-bg

%description -n firefox-lang-bg
Bulgarian resources for Firefox.

%description -n firefox-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoksa.

%package -n firefox-lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bn
Obsoletes:	mozilla-firefox-lang-bn

%description -n firefox-lang-bn
Bengali (Bangladesh) resources for Firefox.

%description -n firefox-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package -n firefox-lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bn_IN
Obsoletes:	mozilla-firefox-lang-bn_IN

%description -n firefox-lang-bn_IN
Bengali (India) resources for Firefox.

%description -n firefox-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n firefox-lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-br
Obsoletes:	mozilla-firefox-lang-br

%description -n firefox-lang-br
Breton resources for Firefox.

%description -n firefox-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoksa.

%package -n firefox-lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bs
Obsoletes:	mozilla-firefox-lang-bs

%description -n firefox-lang-bs
Bosnian resources for Firefox.

%description -n firefox-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoksa.

%package -n firefox-lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ca
Obsoletes:	mozilla-firefox-lang-ca

%description -n firefox-lang-ca
Catalan resources for Firefox.

%description -n firefox-lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description -n firefox-lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description -n firefox-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package -n firefox-lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-cs
Obsoletes:	mozilla-firefox-lang-cs

%description -n firefox-lang-cs
Czech resources for Firefox.

%description -n firefox-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package -n firefox-lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-csb
Obsoletes:	mozilla-firefox-lang-csb

%description -n firefox-lang-csb
Kashubian resources for Firefox.

%description -n firefox-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoksa.

%package -n firefox-lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-cy
Obsoletes:	mozilla-firefox-lang-cy

%description -n firefox-lang-cy
Welsh resources for Firefox.

%description -n firefox-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoksa.

%package -n firefox-lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-da
Obsoletes:	mozilla-firefox-lang-da

%description -n firefox-lang-da
Danish resources for Firefox.

%description -n firefox-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoksa.

%package -n firefox-lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-de
Obsoletes:	mozilla-firefox-lang-de

%description -n firefox-lang-de
German resources for Firefox.

%description -n firefox-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoksa.

%package -n firefox-lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-dsb
Obsoletes:	mozilla-firefox-lang-dsb

%description -n firefox-lang-dsb
Lower Sorbian resources for Firefox.

%description -n firefox-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoksa.

%package -n firefox-lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-el
Obsoletes:	mozilla-firefox-lang-el

%description -n firefox-lang-el
Greek resources for Firefox.

%description -n firefox-lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoksa.

%package -n firefox-lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-en_GB
Obsoletes:	mozilla-firefox-lang-en_GB

%description -n firefox-lang-en_GB
English (British) resources for Firefox.

%description -n firefox-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoksa.

%package -n firefox-lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-en_US
Obsoletes:	mozilla-firefox-lang-en_US

%description -n firefox-lang-en_US
English (American) resources for Firefox.

%description -n firefox-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoksa.

%package -n firefox-lang-en_ZA
Summary:	English (South Africa) resources for Firefox
Summary(pl.UTF-8):	Angielskie pliki językowe dla Firefoksa (wersja dla RPA)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-en_ZA
Obsoletes:	mozilla-firefox-lang-en_ZA

%description -n firefox-lang-en_ZA
English (South Africa) resources for Firefox.

%description -n firefox-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Firefoksa (wersja dla Republiki
Południowej Afryki).

%package -n firefox-lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-eo
Obsoletes:	mozilla-firefox-lang-eo

%description -n firefox-lang-eo
Esperanto resources for Firefox.

%description -n firefox-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoksa.

%package -n firefox-lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es_AR
Obsoletes:	mozilla-firefox-lang-es_AR

%description -n firefox-lang-es_AR
Spanish (Spain) resources for Firefox.

%description -n firefox-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description -n firefox-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description -n firefox-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory).

%package -n firefox-lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es_CL
Obsoletes:	mozilla-firefox-lang-es_CL

%description -n firefox-lang-es_CL
Spanish (Chile) resources for Firefox.

%description -n firefox-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description -n firefox-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description -n firefox-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile).

%package -n firefox-lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es
Obsoletes:	mozilla-firefox-lang-es

%description -n firefox-lang-es
Spanish (Spain) resources for Firefox.

%description -n firefox-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description -n firefox-lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description -n firefox-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii).

%package -n firefox-lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es_MX
Obsoletes:	mozilla-firefox-lang-es_MX

%description -n firefox-lang-es_MX
Spanish (Mexico) resources for Firefox.

%description -n firefox-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description -n firefox-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description -n firefox-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku).

%package -n firefox-lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-et
Obsoletes:	mozilla-firefox-lang-et

%description -n firefox-lang-et
Estonian resources for Firefox.

%description -n firefox-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoksa.

%package -n firefox-lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-eu
Obsoletes:	mozilla-firefox-lang-eu

%description -n firefox-lang-eu
Basque resources for Firefox.

%description -n firefox-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoksa.

%package -n firefox-lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fa
Obsoletes:	mozilla-firefox-lang-fa

%description -n firefox-lang-fa
Persian resources for Firefox.

%description -n firefox-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ff
Obsoletes:	mozilla-firefox-lang-ff

%description -n firefox-lang-ff
Fulah resources for Firefox.

%description -n firefox-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoksa.

%package -n firefox-lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fi
Obsoletes:	mozilla-firefox-lang-fi

%description -n firefox-lang-fi
Finnish resources for Firefox.

%description -n firefox-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoksa.

%package -n firefox-lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fr
Obsoletes:	mozilla-firefox-lang-fr

%description -n firefox-lang-fr
French resources for Firefox.

%description -n firefox-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package -n firefox-lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fy
Obsoletes:	mozilla-firefox-lang-fy

%description -n firefox-lang-fy
Frisian resources for Firefox.

%description -n firefox-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ga
Obsoletes:	mozilla-firefox-lang-ga

%description -n firefox-lang-ga
Irish resources for Firefox.

%description -n firefox-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoksa.

%package -n firefox-lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gd
Obsoletes:	mozilla-firefox-lang-gd

%description -n firefox-lang-gd
Gaelic resources for Firefox.

%description -n firefox-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoksa.

%package -n firefox-lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gl
Obsoletes:	mozilla-firefox-lang-gl

%description -n firefox-lang-gl
Galician resources for Firefox.

%description -n firefox-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-gn
Summary:	Guarani resources for Firefox
Summary(pl.UTF-8):	Pliki językowe guarani dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gn
Obsoletes:	mozilla-firefox-lang-gn

%description -n firefox-lang-gn
Guarani resources for Firefox.

%description -n firefox-lang-gn -l pl.UTF-8
Pliki językowe guarani dla Firefoksa.

%package -n firefox-lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gu
Obsoletes:	mozilla-firefox-lang-gu

%description -n firefox-lang-gu
Gujarati resources for Firefox.

%description -n firefox-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoksa.

%package -n firefox-lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-he
Obsoletes:	mozilla-firefox-lang-he

%description -n firefox-lang-he
Hebrew resources for Firefox.

%description -n firefox-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoksa.

%package -n firefox-lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hi
Obsoletes:	mozilla-firefox-lang-hi

%description -n firefox-lang-hi
Hindi resources for Firefox.

%description -n firefox-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoksa.

%package -n firefox-lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hr
Obsoletes:	mozilla-firefox-lang-hr

%description -n firefox-lang-hr
Croatian resources for Firefox.

%description -n firefox-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoksa.

%package -n firefox-lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hsb
Obsoletes:	mozilla-firefox-lang-hsb

%description -n firefox-lang-hsb
Upper Sorbian resources for Firefox.

%description -n firefox-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoksa.

%package -n firefox-lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hu
Obsoletes:	mozilla-firefox-lang-hu

%description -n firefox-lang-hu
Hungarian resources for Firefox.

%description -n firefox-lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description -n firefox-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoksa.

%package -n firefox-lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hy
Obsoletes:	mozilla-firefox-lang-hy

%description -n firefox-lang-hy
Armenian resources for Firefox.

%description -n firefox-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoksa.

%package -n firefox-lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-id
Obsoletes:	mozilla-firefox-lang-id

%description -n firefox-lang-id
Indonesian resources for Firefox.

%description -n firefox-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-is
Obsoletes:	mozilla-firefox-lang-is

%description -n firefox-lang-is
Icelandic resources for Firefox.

%description -n firefox-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoksa.

%package -n firefox-lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-it
Obsoletes:	mozilla-firefox-lang-it

%description -n firefox-lang-it
Italian resources for Firefox.

%description -n firefox-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ja
Obsoletes:	mozilla-firefox-lang-ja

%description -n firefox-lang-ja
Japanese resources for Firefox.

%description -n firefox-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoksa.

%package -n firefox-lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-kk
Obsoletes:	mozilla-firefox-lang-kk

%description -n firefox-lang-kk
Kazakh resources for Firefox.

%description -n firefox-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoksa.

%package -n firefox-lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-km
Obsoletes:	mozilla-firefox-lang-km

%description -n firefox-lang-km
Khmer resources for Firefox.

%description -n firefox-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoksa.

%package -n firefox-lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-kn
Obsoletes:	mozilla-firefox-lang-kn

%description -n firefox-lang-kn
Kannada resources for Firefox.

%description -n firefox-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoksa.

%package -n firefox-lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ko
Obsoletes:	mozilla-firefox-lang-ko

%description -n firefox-lang-ko
Korean resources for Firefox.

%description -n firefox-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ku
Obsoletes:	mozilla-firefox-lang-ku

%description -n firefox-lang-ku
Kurdish resources for Firefox.

%description -n firefox-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lij
Obsoletes:	mozilla-firefox-lang-lij

%description -n firefox-lang-lij
Ligurian resources for Firefox.

%description -n firefox-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lt
Obsoletes:	mozilla-firefox-lang-lt

%description -n firefox-lang-lt
Lithuanian resources for Firefox.

%description -n firefox-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoksa.

%package -n firefox-lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lv
Obsoletes:	mozilla-firefox-lang-lv

%description -n firefox-lang-lv
Latvian resources for Firefox.

%description -n firefox-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoksa.

%package -n firefox-lang-mai
Summary:	Maithili resources for Firefox
Summary(pl.UTF-8):	Pliki językowe maithili dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-mai
Obsoletes:	mozilla-firefox-lang-mai

%description -n firefox-lang-mai
Maithili resources for Firefox.

%description -n firefox-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Firefoksa.

%package -n firefox-lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-mk
Obsoletes:	mozilla-firefox-lang-mk

%description -n firefox-lang-mk
Macedonian resources for Firefox.

%description -n firefox-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ml
Summary:	Malayalam resources for Firefox
Summary(pl.UTF-8):	Pliki językowe malajalam dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ml
Obsoletes:	mozilla-firefox-lang-ml

%description -n firefox-lang-ml
Malayalam resources for Firefox.

%description -n firefox-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Firefoksa.

%package -n firefox-lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-mr
Obsoletes:	mozilla-firefox-lang-mr

%description -n firefox-lang-mr
Marathi resources for Firefox.

%description -n firefox-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoksa.

%package -n firefox-lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ms
Obsoletes:	mozilla-firefox-lang-ms

%description -n firefox-lang-ms
Malay resources for Firefox.

%description -n firefox-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoksa.

%package -n firefox-lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-nb
Obsoletes:	mozilla-firefox-lang-nb

%description -n firefox-lang-nb
Norwegian Bokmaal resources for Firefox.

%description -n firefox-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoksa.

%package -n firefox-lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-nl
Obsoletes:	mozilla-firefox-lang-nl

%description -n firefox-lang-nl
Dutch resources for Firefox.

%description -n firefox-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoksa.

%package -n firefox-lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-nn
Obsoletes:	mozilla-firefox-lang-nn

%description -n firefox-lang-nn
Norwegian Nynorsk resources for Firefox.

%description -n firefox-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoksa.

%package -n firefox-lang-or
Summary:	Oriya resources for Firefox
Summary(pl.UTF-8):	Pliki językowe orija dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-or
Obsoletes:	mozilla-firefox-lang-or

%description -n firefox-lang-or
Oriya resources for Firefox.

%description -n firefox-lang-or -l pl.UTF-8
Pliki językowe orija dla Firefoksa.

%package -n firefox-lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pa
Obsoletes:	mozilla-firefox-lang-pa

%description -n firefox-lang-pa
Panjabi resources for Firefox.

%description -n firefox-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoksa.

%package -n firefox-lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pl
Obsoletes:	mozilla-firefox-lang-pl

%description -n firefox-lang-pl
Polish resources for Firefox.

%description -n firefox-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoksa.

%package -n firefox-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pt_BR
Obsoletes:	mozilla-firefox-lang-pt_BR

%description -n firefox-lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description -n firefox-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoksa.

%package -n firefox-lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pt
Obsoletes:	mozilla-firefox-lang-pt

%description -n firefox-lang-pt
Portuguese (Portugal) resources for Firefox.

%description -n firefox-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii).

%package -n firefox-lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-rm
Obsoletes:	mozilla-firefox-lang-rm

%description -n firefox-lang-rm
Romansh resources for Firefox.

%description -n firefox-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ro
Obsoletes:	mozilla-firefox-lang-ro

%description -n firefox-lang-ro
Romanian resources for Firefox.

%description -n firefox-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoksa.

%package -n firefox-lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ru
Obsoletes:	mozilla-firefox-lang-ru

%description -n firefox-lang-ru
Russian resources for Firefox.

%description -n firefox-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package -n firefox-lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-si
Obsoletes:	mozilla-firefox-lang-si

%description -n firefox-lang-si
Sinhala resources for Firefox.

%description -n firefox-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoksa.

%package -n firefox-lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sk
Obsoletes:	mozilla-firefox-lang-sk

%description -n firefox-lang-sk
Slovak resources for Firefox.

%description -n firefox-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package -n firefox-lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sl
Obsoletes:	mozilla-firefox-lang-sl

%description -n firefox-lang-sl
Slovene resources for Firefox.

%description -n firefox-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoksa.

%package -n firefox-lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-son
Obsoletes:	mozilla-firefox-lang-son

%description -n firefox-lang-son
Songhai resources for Firefox.

%description -n firefox-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoksa.

%package -n firefox-lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sq
Obsoletes:	mozilla-firefox-lang-sq

%description -n firefox-lang-sq
Albanian resources for Firefox.

%description -n firefox-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoksa.

%package -n firefox-lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sr
Obsoletes:	mozilla-firefox-lang-sr

%description -n firefox-lang-sr
Serbian resources for Firefox.

%description -n firefox-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoksa.

%package -n firefox-lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sv
Obsoletes:	mozilla-firefox-lang-sv

%description -n firefox-lang-sv
Swedish resources for Firefox.

%description -n firefox-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package -n firefox-lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ta
Obsoletes:	mozilla-firefox-lang-ta

%description -n firefox-lang-ta
Tamil (India) resources for Firefox.

%description -n firefox-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n firefox-lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-te
Obsoletes:	mozilla-firefox-lang-te

%description -n firefox-lang-te
Telugu resources for Firefox.

%description -n firefox-lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package -n firefox-lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-th
Obsoletes:	mozilla-firefox-lang-th

%description -n firefox-lang-th
Thai resources for Firefox.

%description -n firefox-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package -n firefox-lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-tr
Obsoletes:	mozilla-firefox-lang-tr

%description -n firefox-lang-tr
Turkish resources for Firefox.

%description -n firefox-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package -n firefox-lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-uk
Obsoletes:	mozilla-firefox-lang-uk

%description -n firefox-lang-uk
Ukrainian resources for Firefox.

%description -n firefox-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoksa.

%package -n firefox-lang-uz
Summary:	Uzbek resources for Firefox
Summary(pl.UTF-8):	Uzbeckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-uz
Obsoletes:	mozilla-firefox-lang-uz

%description -n firefox-lang-uz
Uzbek resources for Firefox.

%description -n firefox-lang-uz -l pl.UTF-8
Uzbeckie pliki językowe dla Firefoksa.

%package -n firefox-lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-vi
Obsoletes:	mozilla-firefox-lang-vi

%description -n firefox-lang-vi
Vietmanese resources for Firefox.

%description -n firefox-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoksa.

%package -n firefox-lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-xh
Obsoletes:	mozilla-firefox-lang-xh

%description -n firefox-lang-xh
Xhosa resources for Firefox.

%description -n firefox-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoksa.

%package -n firefox-lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-zh_CN
Obsoletes:	mozilla-firefox-lang-zh_CN

%description -n firefox-lang-zh_CN
Simplified Chinese resources for Firefox.

%description -n firefox-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoksa.

%package -n firefox-lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-zh_TW
Obsoletes:	mozilla-firefox-lang-zh_TW

%description -n firefox-lang-zh_TW
Traditional Chinese resources for Firefox.

%description -n firefox-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

%package -n firefox-lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-zu
Obsoletes:	mozilla-firefox-lang-zu

%description -n firefox-lang-zu
Zulu resources for Firefox.

%description -n firefox-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoksa.

%prep
unpack() {
	local args="$1" file="$2"
	cp -p $file .
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 89 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{firefoxdir}/browser/extensions
for a in *.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{firefoxdir}/browser/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n firefox-lang-ach
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ach@firefox.mozilla.org.xpi

%files -n firefox-lang-af
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n firefox-lang-an
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-an@firefox.mozilla.org.xpi

%files -n firefox-lang-ar
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n firefox-lang-as
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n firefox-lang-ast
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n firefox-lang-az
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-az@firefox.mozilla.org.xpi

%files -n firefox-lang-be
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n firefox-lang-bg
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n firefox-lang-bn
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n firefox-lang-bn_IN
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n firefox-lang-br
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n firefox-lang-bs
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n firefox-lang-ca
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n firefox-lang-cs
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-cs@firefox.mozilla.org.xpi

#%files -n firefox-lang-csb
#%defattr(644,root,root,755)
#%{firefoxdir}/browser/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n firefox-lang-cy
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n firefox-lang-da
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n firefox-lang-de
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n firefox-lang-dsb
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files -n firefox-lang-el
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n firefox-lang-en_GB
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n firefox-lang-en_US
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n firefox-lang-en_ZA
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n firefox-lang-eo
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n firefox-lang-es_AR
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n firefox-lang-es_CL
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n firefox-lang-es
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n firefox-lang-es_MX
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n firefox-lang-et
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n firefox-lang-eu
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n firefox-lang-fa
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n firefox-lang-ff
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ff@firefox.mozilla.org.xpi

%files -n firefox-lang-fi
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n firefox-lang-fr
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n firefox-lang-fy
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n firefox-lang-ga
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n firefox-lang-gd
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n firefox-lang-gl
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n firefox-lang-gn
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-gn@firefox.mozilla.org.xpi

%files -n firefox-lang-gu
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n firefox-lang-he
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n firefox-lang-hi
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n firefox-lang-hr
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n firefox-lang-hsb
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files -n firefox-lang-hu
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n firefox-lang-hy
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n firefox-lang-id
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n firefox-lang-is
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n firefox-lang-it
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n firefox-lang-ja
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n firefox-lang-kk
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n firefox-lang-km
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-km@firefox.mozilla.org.xpi

%files -n firefox-lang-kn
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n firefox-lang-ko
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ko@firefox.mozilla.org.xpi

#%files -n firefox-lang-ku
#%defattr(644,root,root,755)
#%{firefoxdir}/browser/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n firefox-lang-lij
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n firefox-lang-lt
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n firefox-lang-lv
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n firefox-lang-mai
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n firefox-lang-mk
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n firefox-lang-ml
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n firefox-lang-mr
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n firefox-lang-ms
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ms@firefox.mozilla.org.xpi

%files -n firefox-lang-nb
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n firefox-lang-nl
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n firefox-lang-nn
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n firefox-lang-or
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n firefox-lang-pa
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n firefox-lang-pl
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n firefox-lang-pt_BR
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n firefox-lang-pt
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n firefox-lang-rm
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n firefox-lang-ro
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n firefox-lang-ru
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n firefox-lang-si
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n firefox-lang-sk
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n firefox-lang-sl
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n firefox-lang-son
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n firefox-lang-sq
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n firefox-lang-sr
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n firefox-lang-sv
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n firefox-lang-ta
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n firefox-lang-te
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n firefox-lang-th
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n firefox-lang-tr
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n firefox-lang-uk
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n firefox-lang-uz
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-uz@firefox.mozilla.org.xpi

%files -n firefox-lang-vi
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n firefox-lang-xh
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-xh@firefox.mozilla.org.xpi

%files -n firefox-lang-zh_CN
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n firefox-lang-zh_TW
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

#%files -n firefox-lang-zu
#%defattr(644,root,root,755)
#%{firefoxdir}/browser/extensions/langpack-zu@firefox.mozilla.org.xpi
