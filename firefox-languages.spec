# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
../builder -g firefox-languages.spec
V=45.0
U=http://releases.mozilla.org/pub/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoksa
Name:		firefox-languages
Version:	51.0
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	498e4bdd806dd6daae3e6633929a4c5c
Source1:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	cd101ad2186cfcd54517cc362d4557ca
Source2:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	541228b99af11d256b47e60dd11f0fa2
Source3:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source3-md5:	e6ad16f9f01793cc096febc04abb43df
Source4:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source4-md5:	a072f5086f38f8efc70ee2a31cdb9007
Source5:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source5-md5:	65aae22068f209b04755c75a51a11007
Source6:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source6-md5:	8daf97e5b09f80caa40e87c327584703
Source7:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source7-md5:	44fa78e7c95b88d73cb8411341a3054a
Source8:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source8-md5:	c2895ce469457e52c24072e81179fa67
Source9:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source9-md5:	47066dc66380506aedc12af3254a631d
Source10:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source10-md5:	2ab2d6de2d12b4dd2d9e83c1fddd0eb3
Source11:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source11-md5:	efc2926a23c8a7cdd3b4d178d141afc6
Source12:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source12-md5:	08cb9bb820076e46bc601576c1ea4507
Source13:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cak.xpi
# Source13-md5:	edc681068314cfae3091b9ded4e61dfe
Source14:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	ebc88bf908d18dc7b342500aa03e0cb3
Source15:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	a320703f3b68beb57ed6dd879efa8625
Source16:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	6d15cad59f503772347d541eb1ab2a15
Source17:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	6cac30c13da04bbd599a1568b308bfc8
Source18:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	282758242641fbc1d6db3f49a0dbf24b
Source19:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	1db8c82ce8d394550bc368ab44e04ed9
Source20:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	49737cf5a4b9a1be359b804ec92c9ffd
Source21:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	dba60eaf2f411268b95807eae79d6413
Source22:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	6e29336f06cb76c7f6cc560c5bb3d301
Source23:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	b31502539ef37280f45ce39cdc3f330c
Source24:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	7a04dc1a3124297ec0169365f6da239e
Source25:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	1b7a2d602153b35c37e287480649b6ca
Source26:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	6aae4ce661d4cb3e12d563e3d3109704
Source27:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	57233260aa687ac753135830408e858d
Source28:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	74637245d1c86a51582339e85967328e
Source29:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	bc29e0825f88c9652f45624538476469
Source30:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	5ed3bce75da865b4abd15a5c83c84888
Source31:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	3f9aaccaf4591d256a11189048b97e64
Source32:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	0ec7adb8c2ba9692889921c5c14894f9
Source33:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	4b03e1205878e939eefbbad67e486373
Source34:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	c726a21c516e9de56c0feddf25d20a64
Source35:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	4444a01c79f52b1836a0458a18959e59
Source36:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	e114de7f0e80cb5e9510c4b89141c359
Source37:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	0a308d8d7d274709860fffcae66f366c
Source38:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gn.xpi
# Source38-md5:	68002029022cded2479e3dfdbb9efd92
Source39:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source39-md5:	bcc8332f33afb7e650ac0ce15d368789
Source40:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source40-md5:	997ac6b5556db3e3accd698ee277e0bd
Source41:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source41-md5:	d058ac0d597effb52883258fa443fabd
Source42:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source42-md5:	33167139a4eddd12793ca5d622329843
Source43:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source43-md5:	7977dd604884040d76f22d053fbb63fa
Source44:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source44-md5:	60326e1262b4c89f8c4eb93a7b72ffea
Source45:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source45-md5:	201d6f58a509af06b1f82aa8faae595d
Source46:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source46-md5:	41f47a0069ad9c11ce2396d9c6d398bd
Source47:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source47-md5:	1aff72883f5a9ad8543a73c9e15917ae
Source48:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source48-md5:	90d5db9361a9d1053b3757f7458348a7
Source49:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source49-md5:	a2bcf9e1c1e96c8634442df6dff68de8
Source50:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source50-md5:	8732608599481ece33b68277aebaaaa6
Source51:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source51-md5:	4ce37a6e7231c471c97ab3f3397373fb
Source52:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source52-md5:	050ba7be5982510e01fb1b6f10191c6e
Source53:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source53-md5:	eddd9d6deb1a2801bccd4528689cbd74
Source54:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source54-md5:	5167fa71b55cdb63e2fc4429cfefa7d6
Source55:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source55-md5:	fcda515c9f3f241665c6c6f7dc28a57a
Source56:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source56-md5:	8f57d959da89d3c46f52009ad6d04ad6
Source57:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source57-md5:	380f314b8e937bc512de0273bee0644f
Source58:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source58-md5:	7ee7301cb006562f6df971a3803c225b
Source59:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source59-md5:	5746d41624461b12c900c545b8a15064
Source60:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source60-md5:	2579fd42c3d44ad5f754a4f2b6582667
Source61:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source61-md5:	1faf9c9060d13fe2308ea4dde662b7de
Source62:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source62-md5:	1d5ee7b62a4d8b1ffefc541c209ba15d
Source63:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source63-md5:	f864671372a943b24d279654e6042f82
Source64:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source64-md5:	98d8c44904b2a55c652d593617eb1dd5
Source65:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source65-md5:	b857a3c46aabf6a3f51bc63a2cd72a03
Source66:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source66-md5:	9bc4f4deaf39da84d99aa12762d805e0
Source67:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source67-md5:	31e4ca227ca8f52cba6b7995ad75bd8f
Source68:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source68-md5:	38de915f39c801685564319d975e47de
Source69:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source69-md5:	9a3238e5e40f940b62ae85f0ab0067fb
Source70:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source70-md5:	ca01c48e4c53f883ac65804c279491df
Source71:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source71-md5:	fdd23d657acf511520cca2a46e32267c
Source72:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source72-md5:	2b87cebc155b60edee4162ad3e834d8b
Source73:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source73-md5:	e11c9f74954ed7ee147c995c82dd94bc
Source74:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source74-md5:	4e99e30c5e7f60c7c4b26d75318eefbc
Source75:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source75-md5:	df11b30b2292d24f0f1a5af518ea8f38
Source76:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source76-md5:	4fccf005b023d7776c157d8717c2dfe3
Source77:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source77-md5:	5d5f9a9e2e2a796955a69f9c1015eea4
Source78:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source78-md5:	945a04e859cdca7e12a40afcad3ecede
Source79:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source79-md5:	6d4c7272032b846e0f145c7571393cd3
Source80:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source80-md5:	1b4325a0a9ffdabc573c73a59991057e
Source81:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source81-md5:	63a06c93bcaee283ec77812ae0928c79
Source82:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source82-md5:	7ee708ec4ef6d90cf41474678b7e159a
Source83:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source83-md5:	8bacf320d268c8fcb23d1b7f7c88b71e
Source84:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source84-md5:	2c7d16d5f98d64a0a06f352c45d2db8d
Source85:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source85-md5:	82d37b1adfe74e5b374f2afdb8504dac
Source86:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source86-md5:	6c8eab6180ba5378cf347ab4c3d73253
Source87:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source87-md5:	78617021144dc15d2d989d371dbc0552
Source88:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source88-md5:	8df492f74b28372aa589c26c217840ec
Source89:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source99-md5:	7171470273eb3058dd9df066314036c8
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

%package -n firefox-lang-cak
Summary:	Kaqchikel resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kaqchikel dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}

%description -n firefox-lang-cak
Kaqchikel resources for Firefox.

%description -n firefox-lang-cak -l pl.UTF-8
Pliki językowe kaqchikel dla Firefoksa.

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

%files -n firefox-lang-cak
%defattr(644,root,root,755)
%{firefoxdir}/browser/extensions/langpack-cak@firefox.mozilla.org.xpi

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
