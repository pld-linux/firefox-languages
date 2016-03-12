# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
../builder -g firefox-languages.spec
V=33.0
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoxa
Name:		firefox-languages
Version:	45.0
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	38b1fa50dca0d74c068c7fadf55b8a83
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	5cb7b06e3afdce998a6fd5646f678f4a
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	a890a8db061a1a809664cd4d5d8f9cb1
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	a99021d3d9e753fd316d93cea0b2ab9e
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	7f8d7c5402514ac7f414e4a58ec2ceae
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	ddac17c4dd6d56032a5919bc927ff610
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	5c2900511237af1f021859cca977fbfd
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	a7be82050e732193523bed08d59d7b90
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	e055faae24e2fbaefcc8e11822ecd060
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	e0e7b1f2939777fc3dd675df58844aad
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	c487b8516aae3431fd05abe2001f9eb4
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	7599f69363885fa2490ee2599380030c
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	56c7fece51c2f5a38a8517e71599ab3d
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	a0e4232f207d1df5acf9492b508c907b
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	5ca53afbe58fee97a9ff9acddc818208
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	6e2ad4adfba92a74dcf685795bb9a7b8
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	28edce5532007582cd04346463aa23fb
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	f43edc08a5ce4a7846ab4e7cde2b925d
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	4b71b944e987e8272859e808862adaaf
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	b12b05f7d9a1028cff7563a3f2868749
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	8bc9af34f01b420c35fdbbf29716ce44
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	b5d06e513c8bd153fcdc5a22c78b4c37
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	f003a3fd57a2551165ec1404ecaa200d
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	600ee805ffaa99e269a027484fb69b1d
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	160009f212ea89f3c98f0cf74ee261e4
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	085827f7f1102ecf865f12261f5d3f12
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	9ff8e9ec33aa392ee73e1aebbfb3e8f4
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	55fc4dc689583c72a6c6ad23070abb6a
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	3c0eaa4de9bee7d489e3bd4005b21146
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	40cb4a1d7eafb34740b2f8ffd9076d18
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	a6c820eb030f35c6cc5939c2fc966fa9
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	11efed13c61322989aeea51f95ff3b23
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	12074740f7bfbc72111a18db55968561
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	859fa63b0deb7028dad0f7d4c7997fff
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	426a3bb9617d69a8efcd2fea270b9aec
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	1ba9fcf993f38749d6c17ae180e6fc68
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	ba174a1130caa2eec542f1553462d30c
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	1070faf23bed225f58febe0318bf6649
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source38-md5:	8fb0c8160dc03dc2b8d69cea11e31e58
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source39-md5:	687131ce3291b1258e8c1e4f807730e8
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source40-md5:	eb02ef64afde081aec56c1f73b60af21
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source41-md5:	dc990f375aa786245c2116f37db49bd3
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source42-md5:	5e756111b21646609f30e17e4761f359
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source43-md5:	9ff89dbeb3a85aef4bf38d124bcc110c
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source44-md5:	91c53508073ad42c74bf87a81b9f1c1c
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source45-md5:	a32cd4c4a16badc4da40f8072b21aab1
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source46-md5:	42bbffbf72b2c95f0527f4425ba272fe
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source47-md5:	5220eb51e86a57354783f1c7829d0f89
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source48-md5:	acb01b1e397f21e3e5d210d073e54581
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source49-md5:	dbfef44791096e59063cf8f7ade5a484
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source50-md5:	36c14baa018233ba9e92aa1267281192
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source51-md5:	b2d927fe42e8f87a1b2a5e1d70f0b529
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source52-md5:	b6f1cd5fafaa12fc2eb70478ca5638a2
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source53-md5:	3c5f1dfcc78489c3e72a0c09dbfd3f0a
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source54-md5:	7416b5a36552ca7506b253e1597ecaba
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source55-md5:	1bc2be183fa1622b8d86fd74d74e0242
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source56-md5:	dadc502d47fe59cf3f042a2efa8745fd
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source57-md5:	470017ad9fc48869db5af640f99abf37
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source58-md5:	a4bda6e91c85bad512136c3eb4757acc
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source59-md5:	b79d1e8355b434d0aa235df7c24a9b9e
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source60-md5:	50850d8546be2b61ef5fc7639c6f108c
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source61-md5:	e8221ab17aa5ad9b739b175d10bb7e64
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source62-md5:	897af4e6f29f88d4c619472dff1ac5a6
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source63-md5:	d06b0d817c1623d9f8552a8fe4d3b708
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source64-md5:	4ae773dc89a822f4cc4a2e68b6e68845
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source65-md5:	e7183eaafc6e9c83670766745f10fd86
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source66-md5:	618e6b9c30558510da3ad301b41b0821
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source67-md5:	3e5d1c2d647f3ae63f71f6898868b29d
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source68-md5:	a926c8db9fc7946241889826f3fa360a
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source69-md5:	87e3fe1982b40adf7c90f90fe5f97e56
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source70-md5:	7396642b1796b9c13cfb1fe2b3e3c83b
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source71-md5:	3fd9e6dca70122d05b2fcbbcf7312963
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source72-md5:	3c124b407faf050491a7d2b5f608827c
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source73-md5:	1951ee4e61cd41f314983491f8c93588
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source74-md5:	49784903501f6d407ddffc1306d0cff3
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source75-md5:	bbe4b0942cfa7e3ad2c00f13e9614fdf
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source76-md5:	a9a007345d5f80882583c037cc68a716
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source77-md5:	abd2eccabfdcf5b3686626e642a8cbe1
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source78-md5:	db7187ce5b20bfe83182c680076deb7e
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source79-md5:	4d7841f00103d7633eb0cebfb245dac1
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source80-md5:	f8a0ecb92085ad4d6ac08f9d01bb8537
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source81-md5:	eda72422ac015d73acc97e0cfde798b0
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source82-md5:	ee44db88b448c25c2a7ee5a992b96597
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source83-md5:	dc2c7c459c03fadcc49d95a0e1a0676f
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source84-md5:	03ab392caa7b176f4ecb095b71d060e0
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source85-md5:	08820a40735daec972a1941b76b16e32
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source86-md5:	3cd79364acc17bb6137039e35da3e5a0
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source87-md5:	daea224923e60f5a74790b721475fe95
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source88-md5:	ba2a4a8fe7c95954216df3110a4086f3
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
Pakiety językowe dla Firefoxa.

%package -n firefox-lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ach

%description -n firefox-lang-ach
Acoli resources for Firefox.

%description -n firefox-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoxa.

%package -n firefox-lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-af

%description -n firefox-lang-af
Afrikaans resources for Firefox.

%description -n firefox-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoxa.

%package -n firefox-lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-an

%description -n firefox-lang-an
Aragonese resources for Firefox.

%description -n firefox-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ar

%description -n firefox-lang-ar
Arabic resources for Firefox.

%description -n firefox-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoxa.

%package -n firefox-lang-as
Summary:	Assamese resources for Firefox
Summary(pl.UTF-8):	Asamskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-as

%description -n firefox-lang-as
Assamese resources for Firefox.

%description -n firefox-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ast

%description -n firefox-lang-ast
Asturian resources for Firefox.

%description -n firefox-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-az

%description -n firefox-lang-az
Azerbaijani resources for Firefox.

%description -n firefox-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoxa.

%package -n firefox-lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-be

%description -n firefox-lang-be
Belarusian resources for Firefox.

%description -n firefox-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoxa.

%package -n firefox-lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bg

%description -n firefox-lang-bg
Bulgarian resources for Firefox.

%description -n firefox-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoxa.

%package -n firefox-lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoxa (wersja dla Bangladeszu)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bn

%description -n firefox-lang-bn
Bengali (Bangladesh) resources for Firefox.

%description -n firefox-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoxa (wersja dla Bangladeszu).

%package -n firefox-lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoxa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bn_IN

%description -n firefox-lang-bn_IN
Bengali (India) resources for Firefox.

%description -n firefox-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoxa (wersja dla Indii).

%package -n firefox-lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-br

%description -n firefox-lang-br
Breton resources for Firefox.

%description -n firefox-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoxa.

%package -n firefox-lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bs

%description -n firefox-lang-bs
Bosnian resources for Firefox.

%description -n firefox-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoxa.

%package -n firefox-lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoxa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ca

%description -n firefox-lang-ca
Catalan resources for Firefox.

%description -n firefox-lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description -n firefox-lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description -n firefox-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoxa.

%package -n firefox-lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-cs

%description -n firefox-lang-cs
Czech resources for Firefox.

%description -n firefox-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoxa.

%package -n firefox-lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-csb

%description -n firefox-lang-csb
Kashubian resources for Firefox.

%description -n firefox-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoxa.

%package -n firefox-lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-cy

%description -n firefox-lang-cy
Welsh resources for Firefox.

%description -n firefox-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoxa.

%package -n firefox-lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-da

%description -n firefox-lang-da
Danish resources for Firefox.

%description -n firefox-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoxa.

%package -n firefox-lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-de

%description -n firefox-lang-de
German resources for Firefox.

%description -n firefox-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoxa.

%package -n firefox-lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-dsb

%description -n firefox-lang-dsb
Lower Sorbian resources for Firefox.

%description -n firefox-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoxa.

%package -n firefox-lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-el

%description -n firefox-lang-el
Greek resources for Firefox.

%description -n firefox-lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoxa.

%package -n firefox-lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-en_GB

%description -n firefox-lang-en_GB
English (British) resources for Firefox.

%description -n firefox-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoxa.

%package -n firefox-lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-en_US

%description -n firefox-lang-en_US
English (American) resources for Firefox.

%description -n firefox-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoxa.

%package -n firefox-lang-en_ZA
Summary:	English (South Africa) resources for Firefox
Summary(pl.UTF-8):	Angielskie pliki językowe dla Firefoxa (wersja dla RPA)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-en_ZA

%description -n firefox-lang-en_ZA
English (South Africa) resources for Firefox.

%description -n firefox-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Firefoxa (wersja dla Republiki
Południowej Afryki).

%package -n firefox-lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-eo

%description -n firefox-lang-eo
Esperanto resources for Firefox.

%description -n firefox-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoxa.

%package -n firefox-lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoxa (wersja dla Andory)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es_AR

%description -n firefox-lang-es_AR
Spanish (Spain) resources for Firefox.

%description -n firefox-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description -n firefox-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description -n firefox-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoxa (wersja dla Andory).

%package -n firefox-lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoxa (wersja dla Chile)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es_CL

%description -n firefox-lang-es_CL
Spanish (Chile) resources for Firefox.

%description -n firefox-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description -n firefox-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description -n firefox-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoxa (wersja dla Chile).

%package -n firefox-lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoxa (wersja dla Hiszpanii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es

%description -n firefox-lang-es
Spanish (Spain) resources for Firefox.

%description -n firefox-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description -n firefox-lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description -n firefox-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoxa (wersja dla Hiszpanii).

%package -n firefox-lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoxa (wersja dla Meksyku)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es_MX

%description -n firefox-lang-es_MX
Spanish (Mexico) resources for Firefox.

%description -n firefox-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description -n firefox-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description -n firefox-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoxa (wersja dla Meksyku).

%package -n firefox-lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-et

%description -n firefox-lang-et
Estonian resources for Firefox.

%description -n firefox-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoxa.

%package -n firefox-lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-eu

%description -n firefox-lang-eu
Basque resources for Firefox.

%description -n firefox-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoxa.

%package -n firefox-lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fa

%description -n firefox-lang-fa
Persian resources for Firefox.

%description -n firefox-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ff

%description -n firefox-lang-ff
Fulah resources for Firefox.

%description -n firefox-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoxa.

%package -n firefox-lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fi

%description -n firefox-lang-fi
Finnish resources for Firefox.

%description -n firefox-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoxa.

%package -n firefox-lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fr

%description -n firefox-lang-fr
French resources for Firefox.

%description -n firefox-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoxa.

%package -n firefox-lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fy

%description -n firefox-lang-fy
Frisian resources for Firefox.

%description -n firefox-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ga

%description -n firefox-lang-ga
Irish resources for Firefox.

%description -n firefox-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoxa.

%package -n firefox-lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-gd

%description -n firefox-lang-gd
Gaelic resources for Firefox.

%description -n firefox-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoxa.

%package -n firefox-lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-gl

%description -n firefox-lang-gl
Galician resources for Firefox.

%description -n firefox-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-gu

%description -n firefox-lang-gu
Gujarati resources for Firefox.

%description -n firefox-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoxa.

%package -n firefox-lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-he

%description -n firefox-lang-he
Hebrew resources for Firefox.

%description -n firefox-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoxa.

%package -n firefox-lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hi

%description -n firefox-lang-hi
Hindi resources for Firefox.

%description -n firefox-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoxa.

%package -n firefox-lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hr

%description -n firefox-lang-hr
Croatian resources for Firefox.

%description -n firefox-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoxa.

%package -n firefox-lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hsb

%description -n firefox-lang-hsb
Upper Sorbian resources for Firefox.

%description -n firefox-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoxa.

%package -n firefox-lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hu

%description -n firefox-lang-hu
Hungarian resources for Firefox.

%description -n firefox-lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description -n firefox-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoxa.

%package -n firefox-lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hy

%description -n firefox-lang-hy
Armenian resources for Firefox.

%description -n firefox-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoxa.

%package -n firefox-lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-id

%description -n firefox-lang-id
Indonesian resources for Firefox.

%description -n firefox-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-is

%description -n firefox-lang-is
Icelandic resources for Firefox.

%description -n firefox-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoxa.

%package -n firefox-lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-it

%description -n firefox-lang-it
Italian resources for Firefox.

%description -n firefox-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ja

%description -n firefox-lang-ja
Japanese resources for Firefox.

%description -n firefox-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoxa.

%package -n firefox-lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-kk

%description -n firefox-lang-kk
Kazakh resources for Firefox.

%description -n firefox-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoxa.

%package -n firefox-lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-km

%description -n firefox-lang-km
Khmer resources for Firefox.

%description -n firefox-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoxa.

%package -n firefox-lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-kn

%description -n firefox-lang-kn
Kannada resources for Firefox.

%description -n firefox-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoxa.

%package -n firefox-lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ko

%description -n firefox-lang-ko
Korean resources for Firefox.

%description -n firefox-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ku

%description -n firefox-lang-ku
Kurdish resources for Firefox.

%description -n firefox-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lij

%description -n firefox-lang-lij
Ligurian resources for Firefox.

%description -n firefox-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lt

%description -n firefox-lang-lt
Lithuanian resources for Firefox.

%description -n firefox-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoxa.

%package -n firefox-lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lv

%description -n firefox-lang-lv
Latvian resources for Firefox.

%description -n firefox-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoxa.

%package -n firefox-lang-mai
Summary:	Maithili resources for Firefox
Summary(pl.UTF-8):	Pliki językowe maithili dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-mai

%description -n firefox-lang-mai
Maithili resources for Firefox.

%description -n firefox-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Firefoxa.

%package -n firefox-lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-mk

%description -n firefox-lang-mk
Macedonian resources for Firefox.

%description -n firefox-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ml
Summary:	Malayalam resources for Firefox
Summary(pl.UTF-8):	Pliki językowe malajalam dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ml

%description -n firefox-lang-ml
Malayalam resources for Firefox.

%description -n firefox-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Firefoxa.

%package -n firefox-lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-mr

%description -n firefox-lang-mr
Marathi resources for Firefox.

%description -n firefox-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoxa.

%package -n firefox-lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ms

%description -n firefox-lang-ms
Malay resources for Firefox.

%description -n firefox-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoxa.

%package -n firefox-lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nb

%description -n firefox-lang-nb
Norwegian Bokmaal resources for Firefox.

%description -n firefox-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoxa.

%package -n firefox-lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nl

%description -n firefox-lang-nl
Dutch resources for Firefox.

%description -n firefox-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoxa.

%package -n firefox-lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nn

%description -n firefox-lang-nn
Norwegian Nynorsk resources for Firefox.

%description -n firefox-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoxa.

%package -n firefox-lang-or
Summary:	Oriya resources for Firefox
Summary(pl.UTF-8):	Pliki językowe orija dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-or

%description -n firefox-lang-or
Oriya resources for Firefox.

%description -n firefox-lang-or -l pl.UTF-8
Pliki językowe orija dla Firefoxa.

%package -n firefox-lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pa

%description -n firefox-lang-pa
Panjabi resources for Firefox.

%description -n firefox-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoxa.

%package -n firefox-lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoxa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pl

%description -n firefox-lang-pl
Polish resources for Firefox.

%description -n firefox-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoxa.

%package -n firefox-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pt_BR

%description -n firefox-lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description -n firefox-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoxa.

%package -n firefox-lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoxa (wersja dla Portugalii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pt

%description -n firefox-lang-pt
Portuguese (Portugal) resources for Firefox.

%description -n firefox-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoxa (wersja dla Portugalii).

%package -n firefox-lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-rm

%description -n firefox-lang-rm
Romansh resources for Firefox.

%description -n firefox-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ro

%description -n firefox-lang-ro
Romanian resources for Firefox.

%description -n firefox-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoxa.

%package -n firefox-lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ru

%description -n firefox-lang-ru
Russian resources for Firefox.

%description -n firefox-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoxa.

%package -n firefox-lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-si

%description -n firefox-lang-si
Sinhala resources for Firefox.

%description -n firefox-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoxa.

%package -n firefox-lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sk

%description -n firefox-lang-sk
Slovak resources for Firefox.

%description -n firefox-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoxa.

%package -n firefox-lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sl

%description -n firefox-lang-sl
Slovene resources for Firefox.

%description -n firefox-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoxa.

%package -n firefox-lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-son

%description -n firefox-lang-son
Songhai resources for Firefox.

%description -n firefox-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoxa.

%package -n firefox-lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sq

%description -n firefox-lang-sq
Albanian resources for Firefox.

%description -n firefox-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoxa.

%package -n firefox-lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sr

%description -n firefox-lang-sr
Serbian resources for Firefox.

%description -n firefox-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoxa.

%package -n firefox-lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sv

%description -n firefox-lang-sv
Swedish resources for Firefox.

%description -n firefox-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoxa.

%package -n firefox-lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoxa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ta

%description -n firefox-lang-ta
Tamil (India) resources for Firefox.

%description -n firefox-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoxa (wersja dla Indii).

%package -n firefox-lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-te

%description -n firefox-lang-te
Telugu resources for Firefox.

%description -n firefox-lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoxa.

%package -n firefox-lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-th

%description -n firefox-lang-th
Thai resources for Firefox.

%description -n firefox-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoxa.

%package -n firefox-lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-tr

%description -n firefox-lang-tr
Turkish resources for Firefox.

%description -n firefox-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoxa.

%package -n firefox-lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-uk

%description -n firefox-lang-uk
Ukrainian resources for Firefox.

%description -n firefox-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoxa.

%package -n firefox-lang-uz
Summary:	Uzbek resources for Firefox
Summary(pl.UTF-8):	Uzbeckie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-uz

%description -n firefox-lang-uz
Uzbek resources for Firefox.

%description -n firefox-lang-uz -l pl.UTF-8
Uzbeckie pliki językowe dla Firefoxa.

%package -n firefox-lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-vi

%description -n firefox-lang-vi
Vietmanese resources for Firefox.

%description -n firefox-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoxa.

%package -n firefox-lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-xh

%description -n firefox-lang-xh
Xhosa resources for Firefox.

%description -n firefox-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoxa.

%package -n firefox-lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-zh_CN

%description -n firefox-lang-zh_CN
Simplified Chinese resources for Firefox.

%description -n firefox-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoxa.

%package -n firefox-lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-zh_TW

%description -n firefox-lang-zh_TW
Traditional Chinese resources for Firefox.

%description -n firefox-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoxa.

%package -n firefox-lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoxa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-zu

%description -n firefox-lang-zu
Zulu resources for Firefox.

%description -n firefox-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoxa.

%prep
unpack() {
	local args="$1" file="$2"
	cp -p $file .
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 88 | xargs)

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
